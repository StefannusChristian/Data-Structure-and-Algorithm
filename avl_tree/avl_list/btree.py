class AVLTree:
    def __init__(self):
        self.root = None
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def insert(tree, value):
    new_node = Node()
    new_node.data = value
    if tree.root is None:
        tree.root = new_node
        return 
    else:
        node = tree.root
    
    position,left = search(node, value)

    if left:
        position.left = new_node
    else:
        position.right = new_node
    unbalance_node = unbal_node(tree.root)

    while unbalance_node is not None:
        parent = findParent(unbalance_node,tree)
        node  = rebalance(unbalance_node)
        if parent == 'root':
            tree.root = node
            break
        else:
            parent,place = parent

        if place == 'left':
            parent.left = node
        elif place == 'right':
            parent.right = node
        else:
            tree.root = node
        unbalance_node = unbal_node(tree.root)

def search(node, value):
    left = value <= node.data
    right = value > node.data

    if left: # put the value on the left side of the AVL tree
        if node.left is None:
            return [node,True] 
        elif node.left is not None:
            return search(node.left, value)
    
    if right: # put the value on the right side of the AVL tree
        if node.right is None:
            return [node,False]
        elif node.right is not None:
            return search(node.right, value)

def find(tree ,value, bt = True):
    if bt == True:
        tree = tree.root
    if tree == None:
        return False
    if tree.data == value:
        return True
    if value < tree.data:
        return find(tree.left,value,bt = False)
    else:
        return find(tree.right,value,bt = False)

def height(node):
    if node is None:
        return -1
    elif node.left is None and node.right is None:
        return 0
    else:
        left = -1
        right = -1
        if node.left is not None:
            left = height(node.left)
        if node.right is not None:
            right = height(node.right)
        return max(left,right) + 1

def unbal_node(node):
    if node.left is None and node.right is None:
        return
    left,right = None,None
    if node.left is not None:
        left = unbal_node(node.left)
    if node.right is not None:
        right =  unbal_node(node.right)
    if left is not None:
        return left
    elif right is not None:
        return right
    if abs(height(node.left) - height(node.right)) > 1:
        return node

def leftleft(node):
    pivot = node.left
    node.left = pivot.right
    pivot.right = node
    return pivot

def leftright(node):
    pivot = node.left.right
    node.left.right = pivot.left
    pivot.left = node.left
    node.left = pivot
    return leftleft(node)

def rightright(node):
    pivot = node.right
    node.right = pivot.left
    pivot.left = node
    return pivot

def rightleft(node):
    pivot = node.right.left
    node.right.left = pivot.right
    pivot.right = node.right
    node.right = pivot
    return rightright(node)

def rebalance(node):
    current = node
    unbal_type = ''
    for i in range(2):
        if height(current.left) >= height(current.right):
            unbal_type = unbal_type + 'left'
            current = current.left
        elif height(current.right) >= height(current.left):
            unbal_type = unbal_type + 'right'
            current = current.right

    if unbal_type == 'leftleft':
        return leftleft(node)
    elif unbal_type == 'leftright':
        return leftright(node)
    elif unbal_type == 'rightright':
        return rightright(node)
    elif unbal_type == 'rightleft':
        return rightleft(node)

def findParent(node, tree):
    parent = tree.root
    if node == parent:
        return 'root'
    while node not in (parent.left,parent.right):
        if node.data <= parent.data:
            parent = parent.left
        elif node.data >= parent.data:
            parent = parent.right
        if parent is None:
            return
    if node.data <= parent.data:
        return (parent,'left')
    elif node.data >= parent.data:
        return (parent,'right')
    
def recrToListDfs(node, avl_list):
    if node is None:
        return
    avl_list.append(node.data)
    recrToListDfs(node.left, avl_list)
    recrToListDfs(node.right, avl_list)

def toListDfs(tree):
    avl_list = []
    recrToListDfs(tree.root, avl_list)
    return avl_list
