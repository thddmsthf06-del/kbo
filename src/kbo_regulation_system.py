import pandas as pd
from chatbot import KboChatbot
from injury_list_calculator import InjuryListCalculator
from game_status_logic import GameStatusLogic

class KboRegulationSystem:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.chatbot = KboChatbot(self.df)
        self.calculator = InjuryListCalculator(self.df)
        self.status_logic = GameStatusLogic(self.df)

    def ask_pitch_clock(self):
        # 기능 1: 피치클락 질문 답변 
        return self.chatbot.get_penalty_info()

    def check_il_return(self, last_game_days_ago, removal_date):
        # 기능 2: 부상자 명단 복귀 계산 
        return self.calculator.calculate_return_date(last_game_days_ago, removal_date)

    def analyze_situation(self, inning, top_bottom, rain, abs_fail):
        # 기능 3: 경기 상태 판정 
        return self.status_logic.determine_game_status(inning, top_bottom, rain, abs_fail)

if __name__ == "__main__":
    system = KboRegulationSystem('data/regulations.csv')
    print("=== KBO 규정 통합 시스템 가동 ===")
    print(system.analyze_situation(5, '초', True, True))
