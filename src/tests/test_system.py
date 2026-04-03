import unittest
import pandas as pd
from src.kbo_regulation_system import KboRegulationSystem

class TestKboSystem(unittest.TestCase):
    def setUp(self):
        self.system = KboRegulationSystem('data/regulations.csv')

    def test_pitch_clock_penalty(self):
        # 피치클락 답변에 ID 4, 5가 포함되는지 확인 
        response = self.system.ask_pitch_clock()
        self.assertIn("ID 4", response)
        self.assertIn("ID 5", response)

    def test_injury_logic(self):
        # 3일 전 경기 출전 시 소급 불가 판정 테스트 
        # (calculator 구현 내용에 따라 매개변수는 조정 필요)
        result = self.system.check_il_return(last_game_days_ago=3, removal_date="2026-04-03")
        self.assertIn("소급 적용 불가", result)
        self.assertIn("10일", result)

    def test_suspended_logic(self):
        # 5회초 강우 중단 시 서스펜디드 판정 테스트 
        result = self.system.analyze_situation(5, '초', rain=True, abs_fail=True)
        self.assertIn("서스펜디드 게임", result)
        self.assertIn("ID 2", result) # ABS 대체 판정 포함 여부

if __name__ == '__main__':
    unittest.main()
