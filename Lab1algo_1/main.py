def is_subarray(nums1, nums2):
    if not nums1:
        return True

    i, j = 0, 0
    counter = 0

    while j < len(nums2):

        counter += 1

        if nums1[i] == nums2[j]:
            i += 1
            if i == len(nums1):
                return True
        j += 1

    print(counter)

    return False


nums1 = [1, 2, 3]
nums2 = [1, 2, 3, 4]
print(is_subarray(nums1, nums2))  # True

nums1 = [4, 2]
nums2 = [1, 2, 3, 4]
print(is_subarray(nums1, nums2))  # False

nums1 = [1, 3, 4]
nums2 = [1, 2, 3, 4]
print(is_subarray(nums1, nums2))  # True

nums1 = [1, 3, 6]
nums2 = [1, 2, 3, 4, 5]
print(is_subarray(nums1, nums2))  # False


