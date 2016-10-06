# Dynamic programming workshop
This repository contains materials for a workshop on dynamic programming given at the Recurse Center on October 6, 2016. It includes source code for all examples discussed, the presentation document, and most importantly, a list of resources / tips in this readme.

## How to get good at dynamic programming
More so than with other types of algorithmic problems, the best way to get good at dynamic
programming is practice. The reason for this is two-fold:

1. It takes some built-up pattern recognition to get used to identifying problem sub-structure
2. Dynamic programming solutions tend to be more customized than solutions to other types of problems

To elaborate on the second point, I'd like to draw a contrast between graph algorithms and dynamic programming.
When it comes to solving graph related programming problems, almost everything can be solved
with some variation of search (breadth-first or depth-first), or rarely topological sort.
There's no such "core" algorithm for dynamic programming problems; you generally have to tailor
your algorithm very specifically to the problem you're solving.

## Resources for learning and practicing
In terms of learning the ideas and theory behind dynamic programming, I'd like to recommend
the lectures in part 2 of the [Stanford Algorithms course on Coursera](https://www.coursera.org/learn/algorithm-design-analysis-2).
You can skip right to the dynamic programming lectures, they're in week 3. A lot of the materials for
this workshop were drawn from these lectures so some things will be familiar.

Besides that, I'd recommend 2 things:

1. Practicing lots of problems in the dynamic programming category on [Leetcode](https://leetcode.com/tag/dynamic-programming/)
2. Searching for other videos / explanations of some of the more "classic" DP algorithms. A couple I'd recommend learning about are:
  * The Coin Change problem
  * String edit distance (helps you solve a whole class of string matching problems, like RegEx matching, etc. I found [this](https://www.youtube.com/watch?v=8Q2IEIY2pDU) video and [this](https://www.youtube.com/watch?v=eAVGRWSryGo) video to be really helpful, both from a Coursera course on gene sequencing)
  * The Knapsack problem (covered in the workshop)
  * The Longest Common Subsequence algorithm

## Curated practice problems
Here I've listed some of my favorite dynamic programming problems on leetcode (and a couple from Project Euler), ordered by difficulty.

#### Easier problems
These are pretty similar to the ones we did in workshop (with 1 dimension)  
1. [Climbing stairs](https://leetcode.com/problems/climbing-stairs/) (similar to a problem covered in workshop)  
2. [House robber](https://leetcode.com/problems/house-robber/) (covered in workshop)  
3. [Stock selling](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (a variant on classic DP principles)  
4. [Max sum subarray](https://leetcode.com/problems/maximum-subarray/) (a little more difficult)  

#### Medium-ish problems
I tried to include some 2 dimensional problems here, as well as more complex string / sequence problems.  
1. [Subsequence check](https://leetcode.com/problems/is-subsequence/) (First introduction to string comparison dynamic programming)  
2. [Longest wiggle subsequence](https://leetcode.com/problems/wiggle-subsequence/) (More sequence/subsequence practice)  
3. [Min path sum](https://leetcode.com/problems/minimum-path-sum/) (An introduction to (usually contrived) pathfinding DP problems)  
4. [More pathfinding](https://projecteuler.net/problem=82) (Slightly harder pathfinding)  
5. [Coin change](https://leetcode.com/problems/coin-change/) (Another classic)  
6. [Min perfect square sum](https://leetcode.com/problems/perfect-squares/) (Good 2d problem)  

#### Hard problems
An assortment of problems of the more difficult variety.
1. [More stock buying](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (A tough variation to the max profit problem)
2. [Count unique BSTs](https://leetcode.com/problems/unique-binary-search-trees/) (No comment)
3. [Edit distance](https://leetcode.com/problems/edit-distance/) (Would recommend watching the videos listed above for this one. Maybe give it a shot though?)
4. [Wildcard / regex matching](https://leetcode.com/problems/wildcard-matching/) (Can be solved with dynamic programming, but I think there are more efficient non-DP solutions)

For any of these problems, I would highly recommend looking at the discussion forum on Leetcode once you've finished your solution. I've learned more from people on there than most other sources combined.
