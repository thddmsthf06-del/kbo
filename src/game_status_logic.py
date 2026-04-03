import pandas as pd

class GameStatusLogic:
    def __init__(self, df_regulations):
        self.df = df_regulations

    def determine_game_status(self, inning, top_bottom, rain_stop=False, abs_failure=False):
        """
        경기 상황에 따른 최종 상태 판정
        - inning: 현재 회수 (int)
        - top_bottom: '초' 또는 '말'
        - rain_stop: 강우 중단 여부 (bool)
        - abs_failure: ABS 고장 여부 (bool)
        """
        results = []
        
        # 1. ABS 고장 체크 (ID 2) 
        if abs_failure:
            reg_2 = self.df[self.df['id'] == 2]['content'].values[0]
            results.append(f"[규정 ID 2 적용]: {reg_2} -> 주심 판정으로 경기 속행 가능.")

        # 2. 강우 중단 시 상태 판정
        if rain_stop:
            # 강우 콜드 요건 체크 (ID 24) 
            # 요건: 5회말 종료 후 또는 5회초 종료 시 홈팀 리드
            is_cold_game = False
            if inning > 5:
                is_cold_game = True
            elif inning == 5 and top_bottom == '말':
                # 실제 로직에서는 점수 비교가 필요하나, 규정상 5회말 종료 기준
                is_cold_game = True
            
            if is_cold_game:
                reg_24 = self.df[self.df['id'] == 24]['content'].values[0]
                return f"{' / '.join(results)}\n결과: [규정 ID 24] 강우 콜드게임 성립 가능."
            else:
                # 콜드 요건 미달 시 서스펜디드 (ID 23) 
                reg_23 = self.df[self.df['id'] == 23]['content'].values[0]
                return f"{' / '.join(results)}\n결과: [규정 ID 23] 강우 콜드 요건 미달로 인한 '서스펜디드 게임' 선언."
        
        return "경기 진행 중"
