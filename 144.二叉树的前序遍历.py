#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        cur = root
        while len(stack) > 0 or cur:
            while cur:
                # 将当前节点的值存入结果
                result.append(cur.val)
                # 入栈
                stack.append(cur)
                # 访问左节点
                cur = cur.left
            # 出栈
            cur = stack.pop()
            # 访问右节点
            cur = cur.right
        return result
# @lc code=end

