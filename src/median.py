class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        size = len(nums1) + len(nums2)
        mid = size // 2
        # if total size is even, e.g., 2, mid = 1; if odd, e.g., 5 mid is 2
        index1, index2 = 0, 0
        for _ in range(mid):
            index1, index2 = self.calcNewIndices(
                self, nums1, nums2, index1, index2)
        # if we are here, index1 + index2 == mid
        val = 0
        if size % 2 == 0:
            val += self.calcNextValue(self, nums1, nums2, index1, index2)
            index1, index2 = calcNewIndices(self, nums1, nums2, index1, index2)
            val += self.calcNextValue(self, nums1, nums2, index1, index2)
        else:
            val += 2 * self.calcNextValue(self, nums1, nums2, index1, index2)
        return val / 2

    def calcNewIndices(self, nums1: list[int], nums2: list[int], index1: int, index2: int) -> (int, int):
        if index1 >= len(nums1):
            index2 += 1
        elif index2 >= len(nums2):
            index1 += 1
        elif nums1[index1] >= nums2[index2]:
            index2 += 1
        else:
            index1 += 1
        return index1, index2

    def calcNextValue(self, nums1: list[int], nums2: list[int], index1: int, index2: int) -> int:
        if index1 >= len(nums1):
            return nums2[index2]
        if index2 >= len(nums2):
            return nums1[index1]
        if nums1[index1] >= nums2[index2]:
            return nums2[index2]
        else:
            return nums1[index1]


if __name__ == "__main__":
    print(Solution.findMedianSortedArrays([1, 3], [2]))
