# Implement a Binary Search Tree (BST) in a Class

class BinarySearchTree:
    def __init__(self, values=[]):
        self.values = values

    # 2i + 1
    def _left_child_index(self, parent_index):
        return parent_index * 2 + 1

    # 2i + 2
    def _right_child_index(self, parent_index):
        return parent_index * 2 + 2

    # (i - 1) // 2
    def _parent_index(self, child_index):
        return (child_index -1)//2

    def _is_index_valid(self, index):
        # index must be >= 0, index must be within length of list (values)
        # Expression:
            return index < len(self.values) and index >= 0
        # if index >= len(self.values) or index < 0:
        #     return False
        # else:
        #     return True
    
    def print(self, index = 0, depth = 0):
        if not self._is_index_valid(index):
            return
        
        # print left sub-tree
        left_index = self._left_child_index(index)
        self.print(left_index, depth + 1)

        # print the current node
        print('\t' * depth, self.values[index])

        # print right sub-tree
        right_index = self._right_child_index(index)
        self.print(right_index, depth + 1)

bst = BinarySearchTree([10, 7, 15, 1, 9, 12, 20])
bst.print()