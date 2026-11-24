# 104. Maximum Depth of Binary Tree

### Difficulty: Easy

## Description
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3


Example 2:


Input: root = [1,null,2]
Output: 2


 
Constraints:


	The number of nodes in the tree is in the range [0, 104].
	-100 <= Node.val <= 100

## Submission Details
- **Status**: Accepted
- **Runtime**: 11
- **Memory**: 24708000
- **Language**: python

## Code
```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right))
```
