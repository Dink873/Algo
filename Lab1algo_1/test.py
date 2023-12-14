import unittest

from main import is_subarray


class TestIsSubarrayFunction(unittest.TestCase):





    def test_partial_subarray(self):
        nums1 = [1, 3, 6]
        nums2 = [1, 2, 3, 4, 5]
        self.assertFalse(is_subarray(nums1, nums2))

    def test_subarray_at_end(self):
        nums1 = [3, 4, 5]
        nums2 = [1, 2, 3, 4, 5]
        self.assertTrue(is_subarray(nums1, nums2))

    def test_subarray_at_beginning(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4, 5]
        self.assertTrue(is_subarray(nums1, nums2))

if __name__ == '__main__':
    unittest.main()
