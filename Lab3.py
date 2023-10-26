class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    def calculate_branch_sums(node, current_sum):
        if node is None:
            return 0

        current_sum += node.value

        # Ïåðåâ³ðÿºìî, ÷è âóçîë º ë³âèì ëèñòêîì
        if node.left is None and node.right is None:
            return current_sum

        left_sum = calculate_branch_sums(node.left, current_sum)
        right_sum = calculate_branch_sums(node.right, current_sum)

        return left_sum + right_sum

    return calculate_branch_sums(root, 0)


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

result = branchSums(root)
print(result)
