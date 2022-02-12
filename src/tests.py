import unittest
from tokenizer import Tokenizer
from stopper import Stopper
from stemmer import Stemmer

class TestCases(unittest.TestCase):
    def test_abbreviation_positive(self):
        self.assertTrue(Tokenizer.abbreviate("u.s.a."))
        self.assertTrue(Tokenizer.abbreviate("n.a.s.a."))
        self.assertTrue(Tokenizer.abbreviate("r.o.k."))
        self.assertTrue(Tokenizer.abbreviate("t.e.s.t."))
        self.assertTrue(Tokenizer.abbreviate("b.i.g."))
        self.assertTrue(Tokenizer.abbreviate("a.d."))
        self.assertTrue(Tokenizer.abbreviate("b.s."))
        self.assertTrue(Tokenizer.abbreviate("b.c."))
        self.assertTrue(Tokenizer.abbreviate("a.b.c.d.e.f.g."))

    
    def test_abbreviation_negative(self):
        self.assertFalse(Tokenizer.abbreviate('a.'))
        self.assertFalse(Tokenizer.abbreviate('a.bc'))
        self.assertFalse(Tokenizer.abbreviate('ab.c'))
        self.assertFalse(Tokenizer.abbreviate('ab.c.d.ef'))
        self.assertFalse(Tokenizer.abbreviate('a.9.e.'))
        self.assertFalse(Tokenizer.abbreviate('abcd'))
        self.assertFalse(Tokenizer.abbreviate(''))
        self.assertFalse(Tokenizer.abbreviate('a.a.f.b.w.ed.a.'))
        self.assertFalse(Tokenizer.abbreviate('u.s.a'))

    
    def test_stopper_positive(self):
        stopper = Stopper()
        self.assertTrue(stopper.check('meanwhile'))
        self.assertTrue(stopper.check('afterwards'))
        self.assertTrue(stopper.check('below'))
        self.assertTrue(stopper.check('exclusive'))
        self.assertTrue(stopper.check('sake'))

    
    def test_stopper_negative(self):
        stopper = Stopper()
        self.assertFalse(stopper.check('important'))
        self.assertFalse(stopper.check('snowboard'))
        self.assertFalse(stopper.check('snow'))
        self.assertFalse(stopper.check('phone'))
        self.assertFalse(stopper.check('water'))

    
    def test_stemmer_a(self):
        self.assertTrue(Stemmer.stem_a("stresses") == "stress")
        self.assertTrue(Stemmer.stem_a("stress") == "stress")
        self.assertTrue(Stemmer.stem_a("gaps") == "gap")
        self.assertTrue(Stemmer.stem_a("gas") == "gas")
        self.assertTrue(Stemmer.stem_a("ties") == "tie")
        self.assertTrue(Stemmer.stem_a("cries") == "cri")
        self.assertTrue(Stemmer.stem_a("corpus") == "corpus")
        self.assertTrue(Stemmer.stem_a("cats") == "cat")
        self.assertTrue(Stemmer.stem_a("cat") == "cat")
        self.assertTrue(Stemmer.stem_a("caresses") == "caress")
        self.assertTrue(Stemmer.stem_a("ponies") == "poni")
        self.assertTrue(Stemmer.stem_a("caress") == "caress")

    
    def test_stemmer_b(self):
        self.assertTrue(Stemmer.stem_b("feed") == "feed")
        self.assertTrue(Stemmer.stem_b("agreed") == "agree")
        self.assertTrue(Stemmer.stem_b("plastered") == "plaster")
        self.assertTrue(Stemmer.stem_b("bled") == "bled")
        self.assertTrue(Stemmer.stem_b("motoring") == "motor")
        self.assertTrue(Stemmer.stem_b("sing") == "sing")
        self.assertTrue(Stemmer.stem_b("fizzed") == "fizz")
        self.assertTrue(Stemmer.stem_b("filling") == "fill")
        self.assertTrue(Stemmer.stem_b("filing") == "file")
        self.assertTrue(Stemmer.stem_b("hissing") == "hiss")
        self.assertTrue(Stemmer.stem_b("sized") == "size")
        self.assertTrue(Stemmer.stem_b("troubled") == "trouble")
        self.assertTrue(Stemmer.stem_b("hoping") == "hope")


if __name__ == '__main__':
    unittest.main()
    print(Stemmer.stem_b("feed"))