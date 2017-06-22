# Amazon OA question

## 1.Search a 2D Matrix
Problem:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

## 2.Valid Parentheses
Problem:
Given a string containing just the characters ‘(‘, ‘)’, ‘{‘, ‘}’, ‘[‘ and ‘]’, determine if the input string is valid.

The brackets must close in the correct order, “()” and “()[]{}” are all valid but “(]” and “([)]” are not.

## 3.Merge Two Sorted Lists
Problem:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

## 4. Overlap Rectangle
Problem:
Check whether two rectangles overlaps. The bottem-left and top-right Node has been given.

## 5. Sliding Window Maximum
Problem:
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].


## 6. Search a 2D Matrix II
Problem:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

7.Gray Code
Problem:
Given two hexadecimal numbers find if they can be consecutive in gray code
For example: 10001000, 10001001
return 1
since they are successive in gray code

Example2: 10001000, 10011001
return -1
since they are not successive in gray code.


8.Rotate String
Problem:
Given two words, find if second word is the round rotation of first word.
For example: abc, cab
return 1
since cab is round rotation of abc

Example2: ab, aa
return -1
since ab is not round rotation for aa

9. remove vowel


10. Find Optimal Weights (Close Two Sum)
题目
有一个容器double capacity, 還有一個array(double[] weights), 和int numOfContainers。

要求在array中选出两个weights總总和小于等于capacity但最接近capacity 然後指定到一個Container object並且return。

11. Reverse Second Half of Linked List
题目
2->1->3->4->5->6->7->8 变成 2->1->3->4->8->7->6->5 ； 如果总是为奇数，中间的也要变 5->7->8->6->3->4->2 变成 5->7->8->2->4->3->6 。



12. GCD
题目
找一个数组中所有数的最大公约数。

13.Same Tree
Problem:
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

14. Subtree Check
Please read http://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/

15.K Closest Points
Problem:
Find the K closest points to the origin in 2D plane, given an array containing N points. You can assume K is much smaller than N and N is very large. You need only use standard math operators (addition, subtraction, multiplication, and division).