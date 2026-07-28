class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s=[]
        m={}

        for i in range(len(nums2)-1,-1,-1):
            while s and s[-1]< nums2[i]:
                s.pop()
            if s:
                m[nums2[i]]=s[-1]
            else:
                m[nums2[i]]=-1
            s.append(nums2[i])
        r=[]
        for i in nums1:
            r.append(m[i])
        return r
