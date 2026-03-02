import requests
import json
import time


# --- 1. API 통신을 담당하는 래퍼 클래스 ---
class HotelAPI:
    """
    호텔 예약 서버와의 모든 API 통신을 담당합니다.
    """

    def __init__(self, base_url, x_auth_token):
        self.base_url = base_url
        self.x_auth_token = x_auth_token
        self.auth_key = None

    def start(self, problem):
        """ /start API 호출 (시뮬레이션 시작) """
        url = f"{self.base_url}/start"
        headers = {
            'X-Auth-Token': self.x_auth_token,
            'Content-Type': 'application/json'
        }
        data = {'problem': problem}
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            raise Exception(f"Start API Error: {response.status_code} {response.text}")

        result = response.json()
        self.auth_key = result['auth_key']
        print(f"시나리오 {problem} 시작. Auth Key: {self.auth_key}")
        return result['day']

    def _get_auth_headers(self):
        """ 공통 인증 헤더 반환 """
        return {
            'Authorization': self.auth_key,
            'Content-Type': 'application/json'
        }

    def get_new_requests(self):
        """ /new_requests API 호출 (새 예약 요청 조회) """
        url = f"{self.base_url}/new_requests"
        response = requests.get(url, headers=self._get_auth_headers())
        if response.status_code != 200:
            raise Exception(f"NewRequests API Error: {response.status_code} {response.text}")
        return response.json()

    def reply(self, replies):
        """ /reply API 호출 (예약 승낙/거절 답변) """
        url = f"{self.base_url}/reply"
        data = {'replies': replies}
        response = requests.put(url, headers=self._get_auth_headers(), data=json.dumps(data))
        if response.status_code != 200:
            raise Exception(f"Reply API Error: {response.status_code} {response.text}")
        return response.json()

    def simulate(self, room_assigns):
        """ /simulate API 호출 (객실 배정 및 날짜 진행) """
        url = f"{self.base_url}/simulate"
        data = {'room_assign': room_assigns}
        response = requests.put(url, headers=self._get_auth_headers(), data=json.dumps(data))
        if response.status_code != 200:
            raise Exception(f"Simulate API Error: {response.status_code} {response.text}")
        return response.json()

    def get_score(self):
        """ /score API 호출 (최종 점수 확인) """
        url = f"{self.base_url}/score"
        response = requests.get(url, headers=self._get_auth_headers())
        if response.status_code != 200:
            raise Exception(f"Score API Error: {response.status_code} {response.text}")
        return response.json()


# --- 2. 문제 해결 로직을 담당하는 메인 클래스 ---
class HotelSolver:
    """
    호텔 예약 문제를 해결하는 핵심 로직을 담당합니다.
    """

    def __init__(self, api, h, w, max_days):
        self.api = api
        self.H = h  # 층 수
        self.W = w  # 층당 객실 수
        self.MAX_DAYS = max_days

        # [day][floor][room] -> 0 (free) or reservation_id (occupied)
        # 날짜 인덱스를 1부터 MAX_DAYS + 1 까지 사용하기 위해 +2
        self.hotel_grid = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(max_days + 2)]

        # 관리할 예약 목록
        self.pending_requests = {}  # {id: req_info}
        self.accepted_requests = {}  # {id: assign_info}

    def _get_room_number(self, floor_idx, room_idx):
        """ 0-based 인덱스를 API가 요구하는 객실 번호로 변환 (예: 10075) """
        # 객실 번호는 항상 3자리 0-padding (예: 1 -> 001, 75 -> 075)
        return int(f"{floor_idx + 1}{room_idx + 1:03d}")

    def _find_assignment(self, req):
        """
        'First-Fit' 전략으로 예약 가능한 첫 번째 위치를 찾습니다.
        (floor_idx, room_start_idx) 를 반환하거나, 없으면 None을 반환합니다.
        """
        req_id = req['id']
        amount = req['amount']
        check_in = req['check_in_date']
        check_out = req['check_out_date']  # check_out 날짜는 포함되지 않음

        for f in range(self.H):
            for r_start in range(self.W - amount + 1):
                is_valid_spot = True

                # 해당 기간 동안 이 블록이 모두 비어있는지 확인
                for d in range(check_in, check_out):
                    # Python의 any()를 사용하여 더 빠르게 체크
                    if any(self.hotel_grid[d][f][r] != 0 for r in range(r_start, r_start + amount)):
                        is_valid_spot = False
                        break  # 이 날짜가 막혔으므로 다음 방(r_start) 탐색

                if is_valid_spot:
                    # 이 블록(f, r_start)은 모든 기간(d) 동안 비어있음
                    return (f, r_start)

        # 모든 층, 모든 방을 탐색했으나 적합한 위치를 찾지 못함
        return None

    def _book_assignment(self, req, floor, r_start):
        """
        hotel_grid에 예약을 확정(기록)합니다.
        """
        req_id = req['id']
        amount = req['amount']
        check_in = req['check_in_date']
        check_out = req['check_out_date']

        for d in range(check_in, check_out):
            for r in range(r_start, r_start + amount):
                self.hotel_grid[d][floor][r] = req_id

    def run_simulation(self):
        """
        시뮬레이션 전체를 실행합니다.
        """
        try:
            current_day = self.api.start(SCENARIO)

            while current_day <= self.MAX_DAYS:
                print(f"--- Day {current_day} / {self.MAX_DAYS} ---")

                # 1. 새 예약 요청 받기
                new_reqs_data = self.api.get_new_requests()
                for req in new_reqs_data['reservations_info']:
                    # 데드라인 계산
                    req['deadline'] = min(current_day + 14, req['check_in_date'] - 1)
                    self.pending_requests[req['id']] = req

                # 2. 오늘이 데드라인인 예약들 결정하기
                must_decide_today = []
                other_pending = {}

                for req_id, req in self.pending_requests.items():
                    if req['deadline'] == current_day:
                        must_decide_today.append(req)
                    else:
                        other_pending[req_id] = req

                self.pending_requests = other_pending  # 다음 날로 이월

                # 3. 우선순위 정렬 (가치 = 객실수 * 기간)
                must_decide_today.sort(
                    key=lambda r: r['amount'] * (r['check_out_date'] - r['check_in_date']),
                    reverse=True
                )

                # 4. 예약 처리 (승낙/거절)
                replies_to_send = []
                for req in must_decide_today:
                    assignment = self._find_assignment(req)

                    if assignment:
                        # (승낙) 배정 성공
                        floor_idx, room_start_idx = assignment
                        self._book_assignment(req, floor_idx, room_start_idx)

                        replies_to_send.append({"id": req['id'], "reply": "accepted"})
                        # 나중에 체크인 시 배정 정보를 사용하기 위해 저장
                        self.accepted_requests[req['id']] = {
                            "req": req,
                            "floor": floor_idx,
                            "room_start": room_start_idx
                        }
                    else:
                        # (거절) 배정 실패
                        replies_to_send.append({"id": req['id'], "reply": "refused"})

                # 5. API로 답변 전송 (답변할 것이 있을 때만)
                if replies_to_send:
                    self.api.reply(replies_to_send)
                    print(
                        f"  [답변] {len(replies_to_send)}건 처리 (승낙: {sum(1 for r in replies_to_send if r['reply'] == 'accepted')}, 거절: {sum(1 for r in replies_to_send if r['reply'] == 'refused')})")

                # 6. 오늘 체크인하는 손님들 방 배정
                room_assignments_today = []

                # Python 3.7+ 에서는 dict 순회가 삽입 순서를 보장하지만,
                # 혹시 모르니 체크인할 ID 목록을 먼저 만듭니다.
                ids_to_check_in = [
                    rid for rid, data in self.accepted_requests.items()
                    if data['req']['check_in_date'] == current_day
                ]

                for req_id in ids_to_check_in:
                    assign_info = self.accepted_requests[req_id]
                    room_num = self._get_room_number(assign_info['floor'], assign_info['room_start'])
                    room_assignments_today.append({"id": req_id, "room_number": room_num})

                print(f"  [체크인] {len(room_assignments_today)}팀 배정")

                # 7. 하루 진행 (Simulate)
                # API 호출 간 딜레이 (초당 10회 제한)
                time.sleep(0.1)

                sim_result = self.api.simulate(room_assignments_today)
                current_day = sim_result['day']

                if sim_result['fail_count'] > 0:
                    # 우리 로직이 완벽하다면 이 숫자는 0이어야 합니다.
                    print(f"  !!! 치명적 오류: {sim_result['fail_count']}건 배정 실패 !!!")

                if current_day > self.MAX_DAYS:
                    break

            # 8. 시뮬레이션 종료 후 점수 확인
            print("\n--- 시뮬레이션 종료 ---")
            final_score = self.api.get_score()
            print(json.dumps(final_score, indent=2))

        except Exception as e:
            print(f"시뮬레이션 중단: {e}")
            # 실패 시에도 점수 확인 시도
            try:
                score = self.api.get_score()
                print("--- 현재까지 점수 ---")
                print(json.dumps(score, indent=2))
            except:
                pass


# --- 3. 실행 코드 ---
if __name__ == "__main__":
    # !!! 실행 전 본인의 토큰으로 수정하세요 !!!
    X_AUTH_TOKEN = "7dad8ec88cc0eb24caa2e2f6"
    BASE_URL = "https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api"

    SCENARIO = 1  # 1 또는 2

    if SCENARIO == 1:
        H, W, MAX_DAYS = 3, 20, 200
    else:
        H, W, MAX_DAYS = 10, 200, 1000

    try:
        api = HotelAPI(BASE_URL, X_AUTH_TOKEN)
        solver = HotelSolver(api, H, W, MAX_DAYS)
        solver.run_simulation()

    except Exception as e:
        print(f"실행 오류: {e}")