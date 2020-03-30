class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index=m+n-1
        index1=m-1
        index2=n-1
        while index1>=0 or index2>=0:
            if index1<0:
                nums1[index]=nums2[index2]
                index-=1
                index2-=1
            elif index2<0:
                break
            else:
                if nums1[index1]>nums2[index2]:
                    nums1[index]=nums1[index1]
                    index-=1
                    index1-=1
                else:
                    nums1[index]=nums2[index2]
                    index-=1
                    index2-=1
        return nuns1