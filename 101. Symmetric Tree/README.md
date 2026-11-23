# 101. Symmetric Tree

### Difficulty: Easy

## Description
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 
Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true


Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


 
Constraints:


	The number of nodes in the tree is in the range [1, 1000].
	-100 <= Node.val <= 100


 
Follow up: Could you solve it both recursively and iteratively?

## Submission Details
- **Status**: Accepted
- **Runtime**: 1
- **Memory**: 12468000
- **Language**: python

## Code
```python
class Solution:
    def isSymmetric(self, root):
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val and
                mirror(left.left, right.right) and
                mirror(left.right, right.left)
            )
        return mirror(root.left, root.right)
```
