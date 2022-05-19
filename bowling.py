import unittest


def calculate_score_for(roll_sequence: list) -> int:
    parsed_roll_sequence = list(map(lambda frame: frame.replace("-", "0"), roll_sequence))

    score = 0
    for frame in parsed_roll_sequence:
        score += int(frame[0]) + int(frame[1])

    return score


"""
["1-","0-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 1  EASIEST
["23","0-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 5  NORMAL 
["1-","2-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 3  SUM ISOLATED FRAMES
["2/","4-","0-","0-","1-","0-","0-","0-","0-","0-"]  -> 19 SPARE
["3/","2/","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 22 CONSECUTIVE SPARES 
["X","0-","0-","0-","0-","0-","0-","0-","0-","0-"]   -> 10 ISOLATED STRIKE   
["X","23","4-","0-","0-","0-","0-","0-","0-","0-"]   -> 24 STRIKE WITH SOME HITS
["X","2/","24","0-","0-","0-","0-","0-","0-","0-"]   -> 38 STRIKE + SPARE + NORMAL
["X","X","54","0-","0-","0-","0-","0-","0-","0-"]    -> 53 CONSECUTIVE STRIKES
["0-","0-","0-","0-","0-","0-","0-","0-","0-","3/1",] -> 12 SPARE IN THE FINAL SHOT
["0-","0-","0-","0-","0-","0-","0-","0-","0-","XXX",] -> 30 STRIKE IN THE FINAL SHOT
["X","X","X","X","X","X","X","X","X","X","X","X"]    -> 300 ALL STRIKES
"""


class BowlingShould(unittest.TestCase):
    def test_sum_scores_without_spares_or_strikes(self):
        self.assertEqual(calculate_score_for(["1-", "0-", "0-", "0-", "0-", "0-", "0-", "0-", "0-", "0-"]), 1)
        self.assertEqual(calculate_score_for(["23","0-","0-","0-","0-","0-","0-","0-","0-","0-"]), 5)
        self.assertEqual(calculate_score_for(["1-","2-","0-","0-","0-","0-","0-","0-","0-","0-"]), 3)

    def test_sum_scores_with_spares(self):
        self.assertEqual(calculate_score_for(["2/","4-","0-","0-","1-","0-","0-","0-","0-","0-"]), 19)

if __name__ == '__main__':
    unittest.main()
