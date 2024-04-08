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
