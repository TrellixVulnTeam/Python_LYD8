from spider.test import PyTest, CTest


# from http://json.org/JSON_checker/test/pass2.json
JSON = r'''
[[[[[[[[[[[[[[[[[[["Not too deep"]]]]]]]]]]]]]]]]]]]
'''

class TestPass2:
    def test_parse(self):
        # test in/out equivalence and parsing
        res = self.loads(JSON)
        out = self.dumps(res)
        self.assertEqual(res, self.loads(out))


class TestPyPass2(TestPass2, PyTest): pass
class TestCPass2(TestPass2, CTest): pass
