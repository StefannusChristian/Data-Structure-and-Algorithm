from avl_list.btree import*
import random
import time

if __name__ == '__main__':
    insert_time_start = time.time()
    print("-"*len("PROGRAM IS GENERATING RANDOM NUMBER AND INSERTING TO TREES"))
    print("PROGRAM IS GENERATING RANDOM NUMBER AND INSERTING TO TREES")
    print("-"*len("PROGRAM IS GENERATING RANDOM NUMBER AND INSERTING TO TREES"))
    random_number = random.sample(range(1, 2000), 1999)
    my_tree = AVLTree()
    for num in random_number:
        insert(my_tree, num)
    insert_time_stop = time.time()
    insert_time = insert_time_stop - insert_time_start
    print(f'Waktu yang dibutuhkan untuk insert ke AVL TREE: {insert_time} s')
    print()

    start_1 = time.time()
    num_1 = 142
    print(find(my_tree, num_1))
    stop_1 = time.time()
    time_ned_1 = stop_1-start_1
    print(f'Waktu yang dibutuhkan search (AVL_TREE): {time_ned_1} s')

    start_2 = time.time()
    print(num_1 in random_number)
    stop_2 = time.time()
    time_ned_2 = stop_2-start_2
    print(f'Waktu yang dibutuhkan search (LIST) = {time_ned_2} s')

    start_1 = time.time()
    num_2 = 13493
    print(find(my_tree, num_2))
    stop_1 = time.time()
    time_ned_1 = stop_1-start_1
    print(f'Waktu yang dibutuhkan search (AVL_TREE): {time_ned_1} s')

    start_2 = time.time()
    print(num_2 in random_number)
    stop_2 = time.time()
    time_ned_2 = stop_2-start_2
    print(f'Waktu yang dibutuhkan search (LIST) = {time_ned_2} s')

    start_1 = time.time()
    num_3 = -24
    print(find(my_tree, num_3))
    stop_1 = time.time()
    time_ned_1 = stop_1-start_1
    print(f'Waktu yang dibutuhkan search (AVL_TREE): {time_ned_1} s')

    start_2 = time.time()
    print(num_3 in random_number)
    stop_2 = time.time()
    time_ned_2 = stop_2-start_2
    print(f'Waktu yang dibutuhkan search (LIST) = {time_ned_2} s')

    start_1 = time.time()
    num_4 = 5533
    print(find(my_tree, num_4))
    stop_1 = time.time()
    time_ned_1 = stop_1-start_1
    print(f'Waktu yang dibutuhkan search (AVL_TREE): {time_ned_1} s')

    start_2 = time.time()
    print(num_4 in random_number)
    stop_2 = time.time()
    time_ned_2 = stop_2-start_2
    print(f'Waktu yang dibutuhkan search (LIST) = {time_ned_2} s')

    start_1 = time.time()
    num_5 = 9999
    print(find(my_tree, num_5))
    stop_1 = time.time()
    time_ned_1 = stop_1-start_1
    print(f'Waktu yang dibutuhkan search (AVL_TREE): {time_ned_1} s')

    start_2 = time.time()
    print(num_5 in random_number)
    stop_2 = time.time()
    time_ned_2 = stop_2-start_2
    print(f'Waktu yang dibutuhkan search (LIST) = {time_ned_2} s')

    start_1 = time.time()
    num_6 = -113
    print(find(my_tree, num_6))
    stop_1 = time.time()
    time_ned_1 = stop_1-start_1
    print(f'Waktu yang dibutuhkan search (AVL_TREE): {time_ned_1} s')

    start_2 = time.time()
    print(num_6 in random_number)
    stop_2 = time.time()
    time_ned_2 = stop_2-start_2
    print(f'Waktu yang dibutuhkan search (LIST) = {time_ned_2} s')

    start_1 = time.time()
    num_7 = 92834
    print(find(my_tree, num_7))
    stop_1 = time.time()
    time_ned_1 = stop_1-start_1
    print(f'Waktu yang dibutuhkan search (AVL_TREE): {time_ned_1} s')

    start_2 = time.time()
    print(num_7 in random_number)
    stop_2 = time.time()
    time_ned_2 = stop_2-start_2
    print(f'Waktu yang dibutuhkan search (LIST) = {time_ned_2} s')
