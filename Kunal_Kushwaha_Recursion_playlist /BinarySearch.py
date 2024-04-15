class BinarySearch:
    def binarySearch(self,nums, target, s , e):
        #if the start pointer is going beyond end pointer then target not found 
        # base condition 
        if s > e:
            return -1 

        # find the mid 
        m = s +  (e - s) //2

        if nums[m] == target:
            return m

        if target < nums[m]:
            return self.binarySearch(nums, target , s , m-1) # missed the return keyword  here 

        return self.binarySearch(nums, target , m+1, e) # missed the return keyword  here 

    # Mistake Missed return in the code 
    # must not repeat this mistake 

#print(binarySearch(nums, target, 0 , n ))

import unittest
class Test_BinarySearch(unittest.TestCase):
    def testBinarySearch(self, func):
        nums = [1,2,3,5,6,7]
        target = 7
        n = len(nums)
        target = 7
        self.assertEqual(func(nums ,target ,0 ,n ), 5)


        target = 1
        self.assertEqual(func(nums ,target ,0 ,n ), 0)

        
        print("All Tests passed!!")

if __name__ == "__main__":
    binarySearchObj = BinarySearch()
    TestObj = Test_BinarySearch()
    
    TestObj.testBinarySearch(binarySearchObj.binarySearch)
    



