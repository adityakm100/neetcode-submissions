class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        out = []
        leftn = 0
        leftm = 0

        if not nums1 and not nums2:
            return 0.0

        while leftn <= len(nums1) - 1 and leftm <= len(nums2) - 1:
            ngreat = nums1[leftn] > nums2[leftm]
            if ngreat:
                out.append(nums2[leftm])
                leftm += 1
            else:
                out.append(nums1[leftn])
                leftn += 1
        while leftn != len(nums1):
            out.append(nums1[leftn])
            leftn += 1
        while leftm != len(nums2):
            out.append(nums2[leftm])
            leftm += 1

        left, right = 0, len(out) - 1
        if len(out) % 2 == 0:
            mid1 = (left + right) // 2
            mid2 = ((left + right) // 2) + 1
            return (out[mid1] + out[mid2]) / 2
        else:
            return out[(left + right) // 2]
            