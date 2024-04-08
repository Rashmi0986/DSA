def traverse(m):
  output = []

  for i in range(len(m[0])):
    for j in range(len(m) - 1, -1, -1):
      output.append(m[j][i])

  return output
  
 
m = [[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]
 
res = traverse(m)
print(res)

#####
Results 
[7, 4, 1, 8, 5, 2, 9, 6, 3]
######

Column wise Bottom-to-top right-to-left 
Output should be - [9, 6, 3, 8, 5, 2, 7, 4, 1]

m = [[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]

def traverse(m):
  output = []
  cols = len(m[0])
  rows = len(m)

  for i in range(cols - 1, -1, -1):
    for j in range(rows - 1, -1, -1):
      output.append(m[j][i])

  return output

m = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
 
res = traverse(m)
print(res)
