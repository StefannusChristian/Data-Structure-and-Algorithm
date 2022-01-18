# Class
class Node:
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None


# Binary Tree untuk DFS dan to_list
bin_tree = BinaryTree()

node_1 = Node()
node_2 = Node()
node_3 = Node()
node_4 = Node()
node_5 = Node()
node_6 = Node()

node_1.data = 25
node_2.data = 10
node_3.data = 50
node_4.data = 20
node_5.data = 60
node_6.data = 1

node_1.left = node_2  # 10
node_1.right = node_3  # 50
node_2.left = node_6  # 1
node_2.right = node_4  # 20
node_3.right = node_5  # 60
#  25 --> 10 --> 1 --> 20 --> 50 --> 60 (Atas)
#  1 --> 20 --> 10--> 60 --> 50 --> 25 (Bawah)
bin_tree.root = node_1


def dfsLeftAtas(node):
    print(node.data)
    if node.left is None:
        return
    if node.left is not None:
        return dfsLeftAtas(node.left)


def dfsLeftBawah(node):
    if node.left is None:
        print(node.data)
        return
    if node.left is not None:
        dfsLeftBawah(node.left)
        print(node.data)


def dfsRightAtas(node):
    print(node.data)
    if node.right is None:
        return
    if node.right is not None:
        return dfsRightAtas(node.right)


def dfsRightBawah(node):
    if node.right is None:
        print(node.data)
        return
    if node.right is not None:
        dfsRightBawah(node.right)
        print(node.data)


def dfsAtas(node):
    print(node.data)
    if node.left is None and node.right is None:
        return
    if node.left is not None:
        dfsAtas(node.left)
    if node.right is not None:
        dfsAtas(node.right)


def dfsBawah(node):
    if node.left is None and node.right is None:
        print(node.data)
        return
    if node.left is not None:
        dfsBawah(node.left)
    if node.right is not None:
        dfsBawah(node.right)
    print(node.data)


def recrToListDfs(node, node_values):
    node_values.append(node.data)
    if node.left is None and node.right is None:
        return
    if node.left is not None:
        recrToListDfs(node.left, node_values)
    if node.right is not None:
        recrToListDfs(node.right, node_values)


def toListDfs(bt):
    node_values = []
    recrToListDfs(bt.root, node_values)
    return node_values


# Binary tree untuk single left rotation
new_bin_tree = BinaryTree()
nodeone = Node()
nodetwo = Node()
nodethree = Node()
nodeone.data = 50
nodetwo.data = 25
nodethree.data = 20
nodeone.left = nodetwo
nodetwo.left = nodethree
new_bin_tree.root = nodeone

# Binary tree untuk single right rotation
newnewbintree = BinaryTree()
nodeoneone = Node()
nodetwotwo = Node()
nodethreethree = Node()
nodeoneone.data = 50
nodetwotwo.data = 70
nodethreethree.data = 90
nodeoneone.right = nodetwotwo
nodetwotwo.right = nodethreethree
newnewbintree.root = nodeoneone


def singleRotation(bt):
    if bt.root.left is not None:
        if bt.root.left.left is not None:
            pivot = bt.root.left
            bt.root.left = None
            pivot.right = bt.root
            bt.root = pivot
    if bt.root.right is not None:
        if bt.root.right.right is not None:
            pivot = bt.root.right
            bt.root.right = None
            pivot.left = bt.root
            bt.root = pivot


# Binary Tree untuk double rotation left right
double_rotation_bintreeLR = BinaryTree()
node_1_DLR = Node()
node_2_DLR = Node()
node_3_DLR = Node()
node_1_DLR.data = 50
node_2_DLR.data = 25
node_3_DLR.data = 30
node_1_DLR.left = node_2_DLR
node_2_DLR.right = node_3_DLR
double_rotation_bintreeLR.root = node_1_DLR

# Binary Tree untuk double rotation right left
double_rotation_bintreeRL = BinaryTree()
node_1_DRL = Node()
node_2_DRL = Node()
node_3_DRL = Node()
node_1_DRL.data = 100
node_2_DRL.data = 200
node_3_DRL.data = 150
node_1_DRL.right = node_2_DRL
node_2_DRL.left = node_3_DRL
double_rotation_bintreeRL.root = node_1_DRL


def doubleRotation(bt):
    if bt.root.left is not None:
        if bt.root.left.right is not None:
            pivot = bt.root.left.right
            bt.root.left.right = None
            pivot.left = bt.root.left
            bt.root.left = pivot
            singleRotation(bt)
    if bt.root.right is not None:
        if bt.root.right.left is not None:
            pivot = bt.root.right.left
            bt.root.right.left = None
            pivot.right = bt.root.right
            bt.root.right = pivot
            singleRotation(bt)


def samadengan():
    print('==========================================')


def garismin():
    print('------------------------------------------')


def output():
    print('Output:')


def test():
    samadengan()
    print('~~~~~~~~~~~~~BINARY TREE TEST~~~~~~~~~~~~~')
    samadengan()
    print('DEEP FIRST SEARCH')
    print('Tree yang digunakan = {}'.format(toListDfs(bin_tree)))
    garismin()
    print('DFS Left Atas')
    garismin()
    output()
    dfsLeftAtas(bin_tree.root)
    garismin()
    print('DFS Left Bawah')
    garismin()
    output()
    dfsLeftBawah(bin_tree.root)
    garismin()
    print('DFS Right Atas')
    garismin()
    output()
    dfsRightAtas(bin_tree.root)
    garismin()
    print('DFS Right Bawah')
    garismin()
    output()
    dfsRightBawah(bin_tree.root)
    garismin()
    print('DFS Atas')
    garismin()
    output()
    dfsAtas(bin_tree.root)
    garismin()
    print('DFS Bawah')
    garismin()
    output()
    dfsBawah(bin_tree.root)
    garismin()
    print('TO LIST')
    print('Tree yang digunakan = {}'.format(toListDfs(bin_tree)))
    garismin()
    output()
    print(toListDfs(bin_tree))
    garismin()
    print('ROTATION')
    garismin()
    print('Single Rotation (Left)')
    garismin()
    print("Tree yang digunakan (Left) = {}".format(toListDfs(new_bin_tree)))
    singleRotation(new_bin_tree)
    print('After Single Rotation')
    output()
    print(toListDfs(new_bin_tree))
    garismin()
    print("Single Rotation Right")
    garismin()
    print("Tree yang digunakan (Right) = {}".format(toListDfs(newnewbintree)))
    singleRotation(newnewbintree)
    print('After Single Rotation')
    output()
    print(toListDfs(newnewbintree))
    garismin()
    print('Double Rotation Left Right')
    garismin()
    print("Tree yang digunakan (Left Right) = {}".format(
        toListDfs(double_rotation_bintreeLR)))
    doubleRotation(double_rotation_bintreeLR)
    print('After Double Rotation')
    output()
    print(toListDfs(double_rotation_bintreeLR))
    garismin()
    print('Double Rotation Right Left')
    garismin()
    print('Tree yang digunakan = {}'.format(
        toListDfs(double_rotation_bintreeRL)))
    doubleRotation(double_rotation_bintreeRL)
    print('After Double Rotation')
    output()
    print(toListDfs(double_rotation_bintreeRL))
    garismin()
    samadengan()
    print('~~~~~~~~~~~~~~ TEST SELESAI ~~~~~~~~~~~~~~')
    samadengan()


test()
