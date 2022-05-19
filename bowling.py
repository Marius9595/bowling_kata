import unittest


def bowling(roll_sequence: list) -> int:
    return 1


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
        self.assertEqual(bowling(["1-", "0-", "0-", "0-", "0-", "0-", "0-", "0-", "0-", "0-"]), 1)
        self.assertEqual(bowling(["23","0-","0-","0-","0-","0-","0-","0-","0-","0-"]),5)

if __name__ == '__main__':
    unittest.main()
