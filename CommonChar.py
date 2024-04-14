word = "abc"
mask = 0
for c in word:
  mask |= (1 << (ord(c) - ord('a')))
 
word = "edf"
mask2 = 0
for c in word:
  mask2 |= (1 << (ord(c) - ord('a')))


print((mask&mask2) > 0 )

# tested and working 
# tip from ---https://www.techinterviewhandbook.org/algorithms/string/
 



 
