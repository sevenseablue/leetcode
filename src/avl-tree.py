# coding: utf8
"""
---------------------------------------------
    File Name: avl-tree
    Description: 
    Author: wangdawei
    date:   2018/4/23
---------------------------------------------
    Change Activity: 
                    2018/4/23
---------------------------------------------    
"""
import random
import time
import sys
import argparse


class AVLTree(object):
    def __init__(self):
        self.root = None

    class __Node(object):
        def __init__(self, key):
            self.key = key
            self.right = None
            self.left = None
            self.height = 1

    def __bfactor(self, node):
        return self.__height(node.right) - self.__height(node.left)

    def insertKey(self, key):
        self.root = self.__insert(self.root, key)

    def __insert(self, node, key):
        if node == None:
            node = self.__Node(key)
            return node
        if key == node.key:
            raise Exception("Key already in tree")

        if (key < node.key):
            #			print key, node.key
            node.left = self.__insert(node.left, key)
        else:
            node.right = self.__insert(node.right, key)
        return self.__balance(node)

    def __fixheight(self, node):
        node.height = max(self.__height(node.right), self.__height(node.left)) + 1

    def __height(self, node):
        if node != None:
            return node.height
        else:
            return 0

    def __rotateLeft(self, node):
        p = node.right
        node.right = p.left
        p.left = node
        self.__fixheight(node)
        self.__fixheight(p)
        return p

    def __rotateRight(self, node):
        q = node.left
        node.left = q.right
        q.right = node
        self.__fixheight(node)
        self.__fixheight(q)
        return q

    def __balance(self, node):
        self.__fixheight(node)
        if self.__bfactor(node) == 2:
            if self.__bfactor(node.right) < 0:
                node.right = self.__rotateRight(node.right)
            return self.__rotateLeft(node)

            if self.__bfactor(node) == -2:
                node.left = self.__rotateLeft(node.left)
            return self.__rotateRight(node)
        return node

    def __bfs_sort(self, node, keys_sorted):
        if node == None:
            return
        self.__bfs_sort(node.left, keys_sorted)
        keys_sorted.append(node.key)
        self.__bfs_sort(node.right, keys_sorted)

    def sorted(self):
        keys_sorted = list()
        self.__bfs_sort(self.root, keys_sorted)
        return keys_sorted


def merge_sort(data):
    def __merge(list1, list2):
        res = list()
        # print list1, list2
        i1 = i2 = 0
        while i1 < len(list1) and i2 < len(list2):
            if list1[i1] < list2[i2]:
                elem = list1[i1]
                i1 += 1
            else:
                elem = list2[i2]
                i2 += 1
            res.append(elem)

        res.extend(list1[i1:])
        res.extend(list2[i2:])
        # print "Result is", res
        return res

    if len(data) == 1:
        return data
    middle = len(data) / 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return __merge(left, right)


def main(argv):
    fill = 'random'
    nElem = 1000
    w = 0
    q = nElem
    parser = argparse.ArgumentParser(description='Sorting algorithms comparison')
    parser.add_argument('--fill', metavar='FILL', type=str,
                        help='fill for integer list')
    parser.add_argument('-n', type=int, metavar='n',
                        help='Number of elements in list')
    parser.add_argument('-q', type=int, metavar='q',
                        help='Lower bound of element')
    parser.add_argument('-w', type=int, metavar='w',
                        help='Upper bound of element')

    args = parser.parse_args(argv)
    print(args)

    numbers = random.sample(range(q, w), n)

    random.shuffle(numbers)

    start_time = time.clock()
    sorted_numbers = merge_sort(numbers)
    print(time.clock() - start_time)
    print(sorted_numbers[0], sorted_numbers[-1])

    tree = AVLTree()
    random.shuffle(numbers)

    for i in numbers:
        tree.insertKey(i)

    start_time = time.clock()
    nsorted = tree.sorted()
    print
    time.clock() - start_time
    print
    nsorted[0], nsorted[-1]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
