class RegulationDatabase:
    def __init__(self):
        self.regulations = {
            1: "Regulation description for 1",
            2: "Regulation description for 2",
            4: "Regulation description for 4",
            5: "Regulation description for 5",
            8: "Regulation description for 8",
            9: "Regulation description for 9",
            10: "Regulation description for 10",
            23: "Regulation description for 23",
            24: "Regulation description for 24",
        }

    def get_regulation(self, regulation_id):
        return self.regulations.get(regulation_id, "Regulation not found.")

class PitchClockChatbot:
    def __init__(self):
        self.database = RegulationDatabase()

    def answer_pitch_clock_penalty(self, regulation_id):
        if regulation_id == 4:
            return "Answer for pitch clock penalty based on Regulation 4: " + self.database.get_regulation(4)
        elif regulation_id == 5:
            return "Answer for pitch clock penalty based on Regulation 5: " + self.database.get_regulation(5)
        else:
            return "No information available for this regulation ID."
