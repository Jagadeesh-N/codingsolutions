#problem link
#https://practice.geeksforgeeks.org/problems/midori-and-chocolates2438/1/?problemStatus=solved&page=1&query=problemStatussolvedpage1
class Solution:
    def leftShops (self, i, L):
        # code here 
        return (2**L)-i



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        i, L = input().split()
        i = int(i)
        L = int(L)
        ob = Solution()
        print(ob.leftShops(i, L))
# } Driver Code Ends
