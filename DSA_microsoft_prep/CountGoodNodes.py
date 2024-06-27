class TreeNode:
3    def __init__(self, val=0, left=None, right=None):
4        self.val = val
5        self.left = left
6        self.right = right
7
8class Solution:
9    def goodNodes(self, root: TreeNode) -> int:
10        # Inner function to perform depth-first search (DFS) on the tree.
11        def dfs(node: TreeNode, max_val: int):
12            # Base case: if the current node is None, return from the function.
13            if node is None:
14                return
15          
16            # Using nonlocal keyword to modify the 'good_nodes_count'
17            # variable defined in the parent function's scope
18            nonlocal good_nodes_count
19          
20            # If the current node's value is greater than or equal
21            # to the max value encountered so far, it is a 'good' node.
22            if max_val <= node.val:
23                # Increment count of 'good' nodes.
24                good_nodes_count += 1
25                # Update max value to current node's value.
26                max_val = node.val
27          
28            # Recursively call dfs for the left child with updated max value.
29            dfs(node.left, max_val)
30            # Recursively call dfs for the right child with updated max value.
31            dfs(node.right, max_val)
32
33        # Initialize count of 'good' nodes to 0.
34        good_nodes_count = 0
35        # Invoke dfs with the root of the tree and a very small initial max value.
36        dfs(root, float('-inf'))
37        # Return final count of 'good' nodes.
38        return good_nodes_count
39
