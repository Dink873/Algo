from collections import deque


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_left_leaves(root):
    if root is None:
        return 0

    left_sum = 0

    queue = deque()

    queue.append(root)

    while queue:
        node = queue.popleft()
 
        if node.left and not node.left.left and not node.left.right:
            left_sum += node.left.value

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
########### стек ################
    #stack = [root]

    #while stack:
    #    node = stack.pop()
     #   if node.left and not node.left.left and not node.left.right:
      #      left_sum += node.left.value
       # if node.left:
        #    stack.append(node.left)
        #if node.right:
         #   stack.append(node.right)
##########  рекурсивно ###############
    #if root.left and not root.left.left and not root.left.right:
    #    left_sum += root.left.value

    #left_sum += sum_left_leaves(root.left)
    #left_sum += sum_left_leaves(root.right)

    return left_sum

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

result = sum_left_leaves(root)
print(result)
