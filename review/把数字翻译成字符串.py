"""
@Time:2022/7/2 10:39
@Author:deanywang
@File:把数字翻译成字符串.py
@return:""
"""
#
#
# class Solution:
#     def solve(self, nums):
#         newNums = []
#         count = 1
#         for i in nums:
#             newNums.append(i)
#         for j in range(len(newNums)):
#             for k in range(j + 1, len(newNums)):
#                 if newNums[j] < 3 and newNums[]:
#
#
# Solution().solve("31717126241541717")



class Solution:
    def solve(self , nums: str) -> int:
        nums=[m for m in nums]
        lenth=len(nums)
        if lenth==0 and nums[0]=='0':
            return 0
            #如果字符串的长度或者字符串的第一个数为'0'，则无法译码为字母，返回0
        dp=[0 for _ in nums]
        #初始化dp数组，长度和nums一致并且全部数值初始化为0
        dp[0]=1
        for i in range(1,lenth):
            if nums[i]!='0':
                dp[i]=dp[i-1]
                #如果当前字符不是0，则至少可以翻译为a-i之间的一个字母，此时有dp[i-1]种译码结果
            num=int(nums[i-1])*10+int(nums[i])
            #计算当前字符和前一个字符组合在一起时的数值
            if num>=10 and num<=26:
            #当这个数值在10-26之间时，可以译码成字母
                if i==1:
                    dp[i]=dp[i]+1
                #如果i=1，只有两种译码结果
                else:
                    dp[i]=dp[i]+dp[i-2]
                #i>1时，译码结果应该加入dp[i-2]的结果
        return dp[-1]
        #和爬楼梯的题相似


print(Solution().solve("31717126241541717"))