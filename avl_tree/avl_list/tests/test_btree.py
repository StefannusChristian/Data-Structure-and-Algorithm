from avl_list.btree import *
import pytest

def testCase1():
    my_tree = AVLTree()
    for nodes in [40,50,35,30,39,20]:
        insert(my_tree,nodes)
    expected = [35,30,20,40,39,50]
    current = toListDfs(my_tree)
    assert expected == current

def testCase2():
    my_tree = AVLTree()
    for nodes in [35,20,39,40,50,30]:
        insert(my_tree,nodes)
    expected = [35,20,30,40,39,50]
    current = toListDfs(my_tree)
    assert expected == current
