import unittest

from main import rabin_karp_search


class TestRabinKarpSearch(unittest.TestCase):
    def test_empty_strings(self):
        haystack = ""
        needle = ""
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_needle(self):
        haystack = "ababcababcabcabc"
        needle = ""
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_haystack(self):
        haystack = ""
        needle = "abc"
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result, [])




if __name__ == '__main__':
    unittest.main()
