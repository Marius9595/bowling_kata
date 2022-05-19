import unittest


def calculate_score_for(roll_sequence: list) -> int:
    parsed_roll_sequence = list(map(parse_symbols_in, roll_sequence))

    score = 0
    for i, frame in enumerate(parsed_roll_sequence):
        if i < len(parsed_roll_sequence)-1:
            next_frame = parsed_roll_sequence[i+1]

        is_strike = len(frame) == 1
        if is_strike:
            score += 10 + evaluate_strike("".join(parsed_roll_sequence[i+1:i+3])[:2])
        else:
            partial_score_frame = int(frame[0]) + int(frame[1])
            score += partial_score_frame

            is_spare = len(frame) == 2 and partial_score_frame == 10
            if is_spare:
                score += int(next_frame[0])

    return score

def evaluate_strike(window_frames_for_strike):
     return sum(map(lambda x: 10 if x == "X" else int(x), window_frames_for_strike))



def parse_symbols_in(frame):
    return frame if frame == 'X' else frame.replace("-", "0")\
        .replace("/", str(10 - int(frame[0])))




"""
["1-","0-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 1  EASIEST --DONE
["23","0-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 5  NORMAL  -- DONE
["1-","2-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 3  SUM ISOLATED FRAMES --DONE
["2/","4-","0-","0-","1-","0-","0-","0-","0-","0-"]  -> 19 SPARE -- DONE
["3/","2/","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 22 CONSECUTIVE SPARES -- DONE
["X","0-","0-","0-","0-","0-","0-","0-","0-","0-"]   -> 10 ISOLATED STRIKE --DONE  
["X","23","4-","0-","0-","0-","0-","0-","0-","0-"]   -> 24 STRIKE WITH SOME HITS --DONE
["X","2/","24","0-","0-","0-","0-","0-","0-","0-"]   -> 38 STRIKE + SPARE + NORMAL
["X","X","54","0-","0-","0-","0-","0-","0-","0-"]    -> 53 CONSECUTIVE STRIKES
["0-","0-","0-","0-","0-","0-","0-","0-","0-","3/1"] -> 12 SPARE IN THE FINAL SHOT
["0-","0-","0-","0-","0-","0-","0-","0-","0-","XXX"] -> 30 STRIKE IN THE FINAL SHOT
["X","X","X","X","X","X","X","X","X","X","X","X"]    -> 300 ALL STRIKES
"""


class BowlingShould(unittest.TestCase):
    def test_sum_scores_without_spares_or_strikes(self):
        self.assertEqual(calculate_score_for(["1-", "0-", "0-", "0-", "0-", "0-", "0-", "0-", "0-", "0-"]), 1)
        self.assertEqual(calculate_score_for(["23","0-","0-","0-","0-","0-","0-","0-","0-","0-"]), 5)
        self.assertEqual(calculate_score_for(["1-","2-","0-","0-","0-","0-","0-","0-","0-","0-"]), 3)

    def test_sum_scores_with_spares(self):
        self.assertEqual(calculate_score_for(["2/","4-","0-","0-","1-","0-","0-","0-","0-","0-"]), 19)
        self.assertEqual(calculate_score_for(["3/","2/","0-","0-","0-","0-","0-","0-","0-","0-"]), 22)

    def test_sum_scores_with_strikes(self):
        self.assertEqual(calculate_score_for(["X","0-","0-","0-","0-","0-","0-","0-","0-","0-"]), 10)
        self.assertEqual(calculate_score_for(["X","23","4-","0-","0-","0-","0-","0-","0-","0-"]), 24)
        self.assertEqual(calculate_score_for(["X","2/","24","0-","0-","0-","0-","0-","0-","0-"]), 38)
        self.assertEqual(calculate_score_for(["X","X","54","0-","0-","0-","0-","0-","0-","0-"]), 53)

if __name__ == '__main__':
    unittest.main()
