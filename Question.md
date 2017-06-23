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


16. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

17. Window Sum
注意(arraylist == null || arraylist.size() == 0)要return一个已经初始化的arrayList而不是null。
注意 corner cases。

18. Tree Amplitude
In a binary tree T, a path P is a non-empty sequence of nodes of tree such that, each consecutive node in the sequence is a subtree of its preceding node. In the example tree, the sequences [9, 8, 2] and [5, 8, 12] are two paths, while [12, 8, 2] is not. The amplitude of path P is the maximum difference among values of nodes on path P. The amplitude of tree T is the maximum amplitude of all paths in T. When the tree is empty, it contains no path, and its amplitude is treated as 0.
For exmaple.

Input:

         5
       /   \
     8       9
   /  \     /  \ 
  12   2   8   4
          /    /
        2    5
Output:
7
Explanation:
The paths [5, 8, 12] and [9, 8, 2] have the maximum amplitude 7.



19.Arithmetic Sequence
find out number of arithmetic sequence in array, if result > 1 billion return -1.
[0,1,2,3,2,1] -> 4 ({0 ,1, 2},{1, 2, 3},{0, 1, 2, 3},{3, 2, 1})


20 BST Minimum Path Sum
Return the minimum sum of a path in a BST from node to leaf.

21 Day change
Given an array and number of days. Rules: if arr[i-1] == arr[i+1], arr = 0 else arr = 1, do that for n days.


22. Insert Into Cycle Linked List
please refer to http://www.jianshu.com/p/fc64ced753ad


23. Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.

24. LRU Cache Count Miss

26. Round Robin
一个处理器要处理一堆request，一次只能处理一条，每次执行一个任务最多执行时间q，接着执行等待着的下一个任务。若前一个任务没执行完则放到队尾，等待下一次执行。
假设只要有任务开始以后cpu是不会空闲的，也就是说cpu开始后如果空闲了就说明没有任务了，另外Robin Round最后返回值是float。

26. Rotate Matrix
把一个m*n的矩阵旋转90度，给一个flag规定是向左转还是向右转。


27. Shortest Job First
一个处理器要处理一堆request，一次只能处理一条，如果它有几个积压着的requests，它会先执行持续时间短的那个；对于持续时间相等的requests，先执行最早到达处理器的request。问平均每个request要等多久才能被处理。input：requestTimes[]，每个request到达处理器的时间; durations[] 每个request要处理的持续时间。 两个数组是一一对应的，并已按requestTimes[] 从小到大排序过。


28. maze
给个array,其中只有一格是9，其他格子是0或1，0表示此路不通，1表示可以走，判断从（0,0) 点开始上下左右移动能否找到这个是9的格子。


29. Four Integer
Given four integers, make F(S) = abs(S[0]-S[1])+abs(S[1]-S[2])+abs(S[2]-S[3]) to be largest.


30. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
Code 1: O(1) space


31. Order Dependency
Use topological sort.

32. Maximum Minimum Path
给一个int[][]的matirx，对于一条从左上到右下的path pi，pi中的最小值是mi，求所有mi中的最大值。只能往下或右.


33. Minimum Spanning Tree
题目内容是这样的，给十几个城市供电，连接不同城市的花费不同，让花费最小同时连到所有的边。给出一系列connection类，里面是edge两端的城市名和它们之间的一个cost，找出要你挑一些边，把所有城市连接起来并且总花费最小。不能有环，最后所以城市要连成一个连通块。
不能的话输出空表，最后还要按城市名字排序输出，按照node1来排序,如果一样的话再排node2。
输入:
{“Acity”,”Bcity”,1}
(“Acity”,”Ccity”,2}
(“Bcity”,”Ccity”,3}
输出：
(“Acity”,”Bcity”,1}
(“Acity”,”Ccity”,2}
补充一句，test case一共有6个。


34 Maximum Subtree of Average
就是给一棵多叉树，表示公司内部的上下级关系。每个节点表示一个员工，节点包含的成员是他工作了几个月(int)，以及一个下属数组(ArrayList)。目标就是找到一棵子树，满足：这棵子树所有节点的工作月数的平均数是所有子树中最大的。最后返回这棵子树的根节点。这题补充一点，返回的不能是叶子节点(因为叶子节点没有下属)，一定要是一个有子节点的节点。

35. Five Scores
写好了一个叫Result的类，中文翻译成节点，题目是输入是一堆节点，节点里面有两个属性学生id和分数，保证每个学生至少会有5个分数，求每个人最高的5个分数的平均分。返回的是Map, key是id，value是每个人最高5个分数的平均分double是平均分。


36.Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.


题目：
给一长一短两个 string，返回长 string (N) 里面有没有 substring 是短 string (M) 的 anagram，最好给出O(N)的解法。
思路：
与leetcode 76 相似。