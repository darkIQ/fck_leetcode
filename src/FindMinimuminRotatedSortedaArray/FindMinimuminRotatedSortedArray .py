class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        low=0
        high=len(num)-1
        ans=num[0]
        while low<=high:
            mid=(high+low)/2
            if num[mid]<=num[high]:
               high= mid-1
            else:
                low=mid+1
            ans=min(ans,num[mid])
        return ans              