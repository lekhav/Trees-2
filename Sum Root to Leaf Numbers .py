
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# time: O(N)
# space: O(1) + Recursion call stack 
class Solution:
    def sum_Root_to_Leaf(self, root):
        return self.helper(root, 0)
    
    def helper(self, root, value):
        # BASE CASE
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return value*10 + root.key

        # LOGIC
        root.left = self.helper(root.left, value*10 + root.key)
        root.right = self.helper(root.right, value*10 + root.key)
        return root.left + root.right



a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(25)
a.left.left = TreeNode(13)
a.left.right = TreeNode(18)
a.right.left = TreeNode(24)
a.right.right = TreeNode(27)
a.left.left.left = TreeNode(10)
a.left.left.right = TreeNode(14)
a.left.right.left = TreeNode(16)
a.left.right.right = TreeNode(19)

obj = Solution()
print(obj.sum_Root_to_Leaf(root = a))