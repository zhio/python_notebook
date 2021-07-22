# array = []

# array.append(2)
# array.append(3)
# array.append(1)
# array.append(0)
# array.append(2)

# #链表
# class ListNode:
#     def __init__(self, x):
#         self.val = x        # 节点值
#         self.next = None    # 后继节点引用

# n1 = ListNode(4)
# n2 = ListNode(5)
# n3 = ListNode(1)

# n1.next = n2
# n2.next = n3

# # 栈
# stack = []

# stack.append(1)
# stack.append(2)
# stack.pop()
# stack.pop()

# # 队列

# from collections import deque

# queue  = deque()

# queue.append(1)
# queue.append(2)
# queue.popleft()
# queue.popleft()

# # 树
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# n1 = TreeNode(3)
# n2 = TreeNode(4)
# n3 = TreeNode(5)
# n4 = TreeNode(1)
# n5 = TreeNode(2)

# n1.left = n2
# n2.right = n3
# n2.left = n4
# n2.right = n5

# # 堆

# from heapq import heappush, heappop

# # 初始化小顶堆
# heap = []

# # 元素入堆
# heappush(heap, 1)
# heappush(heap, 4)
# heappush(heap, 2)
# heappush(heap, 6)
# heappush(heap, 8)

# # 元素出堆（从小到大）
# heappop(heap) # -> 1
# heappop(heap) # -> 2
# heappop(heap) # -> 4
# heappop(heap) # -> 6
# heappop(heap) # -> 8

import requests

url = "https://bfabaicup.oss-cn-beijing.aliyuncs.com/headimg/5e8791b2efb066822fdc5c7bbd356644.jpeg"
response = requests.get(url)
img = response.content

with open("./a.jpg",'wb') as f:
    f.write(img)