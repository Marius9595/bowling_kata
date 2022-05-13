import unittest

def bowling():
    pass


"""
["1-","0-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 1  EASIEST
["23","0-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 5  NORMAL 
["1-","2-","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 3  SUM ISOLATED FRAMES
["2/","4-","0-","0-","1-","0-","0-","0-","0-","0-"]  -> 19 SPARE
["3/","2/","0-","0-","0-","0-","0-","0-","0-","0-"]  -> 23 CONSECUTIVE SPARES 
["X","0-","0-","0-","0-","0-","0-","0-","0-","0-"]   -> 10 ISOLATED STRIKE   
["X","23","4-","0-","1-","0-","0-","0-","0-","0-"]   -> 25 STRIKE WITH SOME HITS
["X","2/","24","0-","0-","0-","0-","0-","0-","0-"]   -> 38 STRIKE + SPARE + NORMAL
["X","X","54","0-","0-","0-","0-","0-","0-","0-"]    -> 53 CONSECUTIVE STRIKES
["X","X","X","X","X","X","X","X","X","X","X","X"]    -> 
"""
class BowlingShould(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
