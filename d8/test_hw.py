# ...existing code...
from hw import *
import hw  # 모킹을 위해 모듈도 참조

def test_enter_system(monkeypatch):
    """
    enter_system 함수의 동작을 테스트합니다.
    """
    # Mocking
    usr = user(logged=True, entered=False)
    wb = web()
    sc = script()
    sv = server()

    # 서버 응답을 모킹
    def mock_enter_api(response=False):
        sv.response_code = 200 if response else 400
        return sv.response_code == 200

    monkeypatch.setattr(sv, "enter_api", mock_enter_api)

    # 테스트 실행
    hw.enter_system(user=usr, web=wb, script=sc, server=sv)

    # 결과 검증
    assert usr.entered == True
    assert wb.alert == True
    assert wb.alert_message == "Welcome!"
    assert sc.enter_api_called == True
    assert sv.enter_api_check == True