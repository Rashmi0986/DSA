class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        k = 0 
        mat = []
        for i in range(m):
            sub = []
            for j in range(n):
                if k < len(original):
                    sub.append(original[k])
                    k+=1
            mat.append(sub)
        return mat 

"""
In the above algorith the K is the pointer to the 1D array index 
Sub is sublist containing the elements to be added to the matrix . 


"""
