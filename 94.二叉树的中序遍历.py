# @before-stub-for-debug-begin
from python3problem94 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        cur = root
        while len(stack) > 0 or cur:
            # 当前节点到左节点依次入栈
            while cur:
                stack.append(cur)
                cur = cur.left
            # 左节点到当前节点依次出栈
            cur = stack.pop()
            result.append(cur.val)
            # 访问右节点
            cur = cur.right
        return result
# @lc code=end

