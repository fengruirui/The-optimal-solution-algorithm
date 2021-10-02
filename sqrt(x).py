class Solution:
    def mySqrt(self, x: int) -> int:
        # if x == 0:return 0
        # if x < 4 :return 1
        # if x == 4:return 2
        # l,r = 1,x//2
        # while l <= r:
        #     mid = (l+r)//2
        #     if mid**2<=x and (mid**2+1)>x:  wrong!
        #         return mid
        #     elif mid**2>x:
        #         r = mid
        #     else:
        #         l = mid
        # return l
      
        if x==0: return 0
        if x<=3: return 1
        if x==4: return 2
        # when x>4 x<x^2/4, so sqrt(x)<x/2
        l, r = 1, x//2
        # 循环不变量Cyclic invariant  l<= sqrt <r
        while l<=r:
            mid = (l+r)//2 # 取更靠左，因为向下取整 
            if mid**2<=x and (mid+1)**2>x:
                return mid
            elif mid**2>x: # sqrt<mid 所以令 r=mid
                r=mid
            else: # else说明(mid+1)^2<=x, sqrt>=mid+1, l=mid+1
                l=mid+1
        return l
