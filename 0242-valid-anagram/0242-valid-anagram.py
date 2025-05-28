class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        SbucketsArr, TbucketsArr= [0] * 26, [0] * 26
        
        for i in range(len(s)):
            SbucketIndex = ord(s[i]) - 97
            SbucketsArr[SbucketIndex] = SbucketsArr[SbucketIndex] + 1

            TbucketIndex = ord(t[i]) - 97
            TbucketsArr[TbucketIndex] = TbucketsArr[TbucketIndex] + 1
        if SbucketsArr == TbucketsArr:
            return True
        return False

        