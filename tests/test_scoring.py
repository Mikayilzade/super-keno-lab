import unittest
from src.rules import RuleSet
from src.evaluator import score_ticket

class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.draw=tuple(range(1,21))

    def test_ten_hits(self):
        r=score_ticket(tuple(range(1,11)),self.draw)
        self.assertEqual(r['hits'],10)
        self.assertEqual(r['payout'],100000.0)

    def test_one_hit(self):
        r=score_ticket((1,21,22,23,24,25,26,27,28,29),self.draw)
        self.assertEqual(r['hits'],1)
        self.assertEqual(r['payout'],1.0)
        self.assertEqual(r['pl'],0.0)

    def test_four_hits_no_prize(self):
        r=score_ticket((1,2,3,4,21,22,23,24,25,26),self.draw)
        self.assertEqual(r['hits'],4)
        self.assertEqual(r['payout'],0.0)

    def test_multiplier(self):
        rules=RuleSet(multiplier=5)
        r=score_ticket(tuple(range(1,11)),self.draw,rules)
        self.assertEqual(r['cost'],5.0)
        self.assertEqual(r['payout'],500000.0)

    def test_tax_model(self):
        rules=RuleSet()
        self.assertAlmostEqual(rules.net_cash_for_hits(9),1400.1,places=6)

if __name__=='__main__':
    unittest.main()
