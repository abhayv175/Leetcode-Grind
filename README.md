# Leetcode-Problems
My LeetCode solutions in Python with time/space complexity analysis and notes.

<div align="center">

# ⚡ LeetCode Solutions in Python

> *My LeetCode solutions in Python with time/space complexity analysis and notes.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-abhayv175-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/abhayv175/)

---

### 📊 Practice Metrics

<img src="https://leetcard.jacoblin.cool/abhayv175?theme=dark&font=Karma&ext=heatmap" alt="LeetCode Stats for abhayv175" />

</div>

---

## 🎯 Repository Objectives

- **Pattern-First Problem Solving:** Master core algorithmic patterns (Two Pointers, Sliding Window, Trees, Graphs, DP) instead of memorizing solutions.
- **Idiomatic Python:** Implement clean, maintainable Python solutions leveraging built-in standard libraries (`collections`, `heapq`, `math`).
- **Complexity Analysis:** Document strict Time ($O$) and Space ($O$) trade-offs for every solution.

---

## 📂 Directory Layout

Solutions are organized into focused topic folders to streamline revision:







```markdown
<div align="center">

# ⚡ LeetCode Solutions & DSA Handbook

> *My LeetCode solutions in Python with time/space complexity analysis and comprehensive Data Structures & Algorithms notes.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-abhayv175-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/abhayv175/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](./LICENSE)

---

### 📊 Practice Metrics

<img src="https://leetcard.jacoblin.cool/abhayv175?theme=dark&font=Karma&ext=heatmap" alt="LeetCode Stats for abhayv175" />

</div>

---

## 🎯 Repository Objectives

- **Pattern-First Problem Solving:** Master core algorithmic patterns (Two Pointers, Sliding Window, Trees, Graphs, DP) instead of memorizing solutions.
- **Idiomatic Python:** Implement clean, maintainable Python solutions leveraging built-in standard libraries (`collections`, `heapq`, `math`).
- **Complexity Analysis:** Document strict Time ($O$) and Space ($O$) trade-offs for every solution.

---

## 📂 Directory Layout

Solutions are organized into focused topic folders to streamline revision:

```text
leetcode-solutions/
├── arrays-hashing/           # Hash maps, frequency counts, prefix sums
├── two-pointers/             # Converging pointers, fast & slow pointers
├── sliding-window/           # Fixed and dynamic subarray windows
├── stack/                    # Monotonic stack, parenthesis matching
├── binary-search/            # Sorted search, search spaces, boundary finding
├── linked-list/              # In-place manipulation, cycle detection
├── trees/                    # Binary trees, BSTs, DFS/BFS traversals
├── heap-priority-queue/      # Top-K elements, min/max heaps
├── backtracking/             # Subsets, permutations, search pruning
├── graphs/                   # Grid traversal, BFS/DFS, topological sort
├── dynamic-programming/      # Memoization and iterative tabulation
├── intervals/                # Overlapping intervals, merge patterns
├── bit-manipulation/         # Bitwise operations, XOR properties
├── templates/                # Standard boilerplate and solution template
├── LICENSE
└── README.md

```

---

## 📚 Complete Data Structures & Algorithms (DSA) Handbook

### 1. What is a Data Structure (DS)?

A **Data Structure** is a specialized format for organizing, managing, and storing data in computer memory so that operations (such as searching, inserting, updating, and deleting) can be performed efficiently.

Memory in a computer consists of sequential memory addresses. Different data structures handle this layout differently:

* **Contiguous Allocation (Arrays / Python Lists):** Elements sit sequentially next to each other in memory. This allows constant-time access by calculating `memory_address = base_address + (index * element_size)`. However, resizing or inserting elements into the middle requires shifting subsequent elements, incurring a linear cost.
* **Node-Based Pointer Networks (Linked Lists, Trees, Graphs):** Elements ("nodes") are scattered arbitrarily in memory and connected via reference pointers. This allows dynamic growth and cheap updates, but accessing an arbitrary node requires traversing the pointers sequentially.

---

### 2. What is an Algorithm (A)?

An **Algorithm** is an unambiguous, step-by-step computational procedure that takes an input, processes it through a finite set of instructions, and terminates with an output.

Evaluating an algorithm involves two primary dimensions:

1. **Correctness:** Does it yield the exact intended output across every edge case (empty arrays, negative values, duplicates, large inputs)?
2. **Efficiency:** How many computational operations and memory allocations does it perform relative to the input size $n$?

---

### 3. What is Time & Space Complexity, and Why Does It Matter?

Running a timer (like `time.time()`) to measure how fast code runs is unreliable because runtime depends on hardware specifications, CPU throttling, background operating system processes, and programming language runtimes.

**Asymptotic Complexity** solves this by evaluating how an algorithm's resource requirements scale as the input size $n$ approaches infinity ($n \to \infty$).

#### The Three Asymptotic Bounds:

* **Big-O Notation ($O$):** The **upper bound** (worst-case scenario). Guarantees that execution time or memory will never exceed this growth rate.
* **Big-$\Omega$ (Omega) Notation ($\Omega$):** The **lower bound** (best-case scenario).
* **Big-$\Theta$ (Theta) Notation ($\Theta$):** The **tight bound** (when worst-case and best-case scale at the exact same rate).

#### Why Complexity Is Critical in Interviews & Production:

* **Preventing Server Timeouts:** Online coding platforms and production web services have strict execution limits (typically ~1–2 seconds on LeetCode, translating to roughly $10^7$ to $10^8$ operations). An $O(n^2)$ algorithm applied to $n = 100,000$ requires $10^{10}$ operations—causing a **Time Limit Exceeded (TLE)** error or hanging a production API endpoint.
* **Preventing Out-of-Memory (OOM) Crashes:** An algorithm that allocates dynamic tables or recursion trees without bounding its depth can exhaust available RAM or trigger a call stack overflow.
* **Space-Time Trade-off:** Optimizing algorithmic systems often means sacrificing auxiliary RAM (e.g., hash tables, precomputed prefix arrays) to drastically reduce runtime CPU operations.

---

### 4. Complexity Orders & Scale of Growth

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$$

| Complexity | Name | Operations for $n = 1000$ | Practical Example | Feasible Constraints ($n$) |
| --- | --- | --- | --- | --- |
| **$O(1)$** | Constant | 1 | Index lookup in array, hash map retrieval | Any $n$ |
| **$O(\log n)$** | Logarithmic | $\approx 10$ | Binary Search, balanced tree operations | $n \le 10^9$ |
| **$O(n)$** | Linear | $1,000$ | Single pass, Two Pointers, Sliding Window | $n \le 10^7$ |
| **$O(n \log n)$** | Linearithmic | $\approx 10,000$ | Merge Sort, Quick Sort (average), Heap Sort | $n \le 10^6$ |
| **$O(n^2)$** | Quadratic | $1,000,000$ | Nested loops, brute-force comparisons | $n \le 10^4$ |
| **$O(2^n)$** | Exponential | $1.07 \times 10^{301}$ | Recursive power set, exhaustive branch search | $n \le 20$ |
| **$O(n!)$** | Factorial | Incalculable | Permutations generation (Traveling Salesperson) | $n \le 11$ |

---

### 5. Master Data Structures Breakdown

| Data Structure | Access | Search | Insertion | Deletion | Space | Key Python Implementation & Notes |
| --- | --- | --- | --- | --- | --- | --- |
| **Array / Dynamic Array** | $O(1)$ | $O(n)$ | $O(1)$ amortized (end)<br>

<br>$O(n)$ (start/mid) | $O(n)$ | $O(n)$ | Python `list`. Appending to the end is fast; inserting at index 0 shifts all elements. |
| **Hash Table** | N/A | $O(1)$ avg<br>

<br>$O(n)$ worst | $O(1)$ avg<br>

<br>$O(n)$ worst | $O(1)$ avg | $O(n)$ | Python `dict` and `set`. Keys must be immutable (hashable). Worst-case occurs during hash collisions. |
| **Singly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ (with reference) | $O(1)$ (with reference) | $O(n)$ | Use a `dummy` head node to eliminate special edge-case handling for modifying the head. |
| **Stack** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ | LIFO (Last-In, First-Out). Implemented using Python's `list` (`append` and `pop`). |
| **Queue** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ | FIFO (First-In, First-Out). Always use `collections.deque` (`append` and `popleft`). Avoid `list.pop(0)` as it is $O(n)$. |
| **Binary Search Tree (BST)** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ | Left child $<$ Root $\le$ Right child. Degenerates to $O(n)$ if values are inserted in sorted order without balancing. |
| **Heap / Priority Queue** | $O(1)$ (min) | $O(n)$ | $O(\log n)$ | $O(\log n)$ (`heappop`) | $O(n)$ | Python's `heapq` module is a **min-heap** by default. To simulate a max-heap, multiply values by `-1`. |
| **Graph (Adjacency List)** | N/A | $O(V + E)$ | $O(1)$ | $O(E)$ | $O(V + E)$ | Represented via `collections.defaultdict(list)`. Requires a `visited` set to prevent infinite cycles. |

---

### 6. Algorithmic Pattern Decision Matrix

Identify the correct algorithmic pattern based on problem characteristics:

| Algorithmic Pattern | Problem Trigger Keywords | Mechanism / Strategy | Common Time | Auxiliary Space |
| --- | --- | --- | --- | --- |
| **Two Pointers** | Sorted array, finding pairs, checking palindromes, in-place reversal | Converge `left` and `right` indices, or use fast/slow pointers for cycle detection | $O(n)$ | $O(1)$ |
| **Sliding Window** | Contiguous subarrays/substrings, target sums, distinct characters | Grow `right` to meet a constraint; contract `left` to optimize window size | $O(n)$ | $O(k)$ |
| **Monotonic Stack** | "Next Greater Element", "Previous Smaller Element", largest rectangle | Maintain elements in strictly increasing or decreasing order inside stack | $O(n)$ | $O(n)$ |
| **Binary Search** | Sorted sequences, searching monotonic condition space ("minimize maximum") | Repeatedly halve the search boundary $[low, high]$ by testing midpoint condition | $O(\log n)$ | $O(1)$ |
| **BFS (Breadth-First)** | Shortest path in unweighted graphs/matrices, level-order traversal | FIFO queue processing nodes layer-by-layer; guarantees shortest path | $O(V + E)$ | $O(V)$ |
| **DFS (Depth-First)** | Path verification, finding connected components, recursive trees | Call stack or explicit LIFO stack exploring completely to branch leaves | $O(V + E)$ | $O(V)$ |
| **Topological Sort** | Prerequisite ordering, task scheduling, cycle checks in DAGs | Track in-degrees (Kahn's Algorithm via Queue) or post-order DFS | $O(V + E)$ | $O(V)$ |
| **Dynamic Programming** | Overlapping subproblems, optimal substructure, calculating combinations | Store subproblem results via memoization (top-down) or table array (bottom-up) | $O(\text{states})$ | $O(\text{states})$ |
| **Backtracking** | Generate all subsets, permutations, combinations, N-Queens | Build state recursively, validate validity, explore branch, and backtrack (undo) | $O(2^n) \text{ or } O(n!)$ | $O(n)$ |

---

## 📝 Solution Template

Every committed `.py` solution adheres to this standard template:

```python
"""
Problem:     0001. Two Sum
Difficulty:  Easy
Link:        [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)
Topic:       Arrays & Hashing

Approach:
    Use a hash map to record visited values and their indices.
    For each element, calculate complement = target - num.
    If complement exists in the map, return the pair.

Complexity:
    - Time:  O(n) - Single linear scan through the array.
    - Space: O(n) - Hash map holds at most n elements.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], idx]
            lookup[num] = idx
        return []

# Local Verification
if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1], "Test Case 1 Failed"
    assert sol.twoSum([3, 2, 4], 6) == [1, 2], "Test Case 2 Failed"
    assert sol.twoSum([3, 3], 6) == [0, 1], "Test Case 3 Failed"
    print("✓ All test assertions passed successfully.")

```

---

## 📈 Solutions Index

| # | Problem | Difficulty | Solution | Time | Space | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 0001 | [Two Sum](https://leetcode.com/problems/two-sum/) | `Easy` | [0001-two-sum.py](https://www.google.com/search?q=./arrays-hashing/0001-two-sum.py) | $O(n)$ | $O(n)$ | Hash map complement lookup |
| 0217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | `Easy` | [0217-contains-duplicate.py](https://www.google.com/search?q=./arrays-hashing/0217-contains-duplicate.py) | $O(n)$ | $O(n)$ | Hash set tracking |

| # | Problem | Difficulty | Solution | Time | Space | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 0125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | `Easy` | [0125-valid-palindrome.py](https://www.google.com/search?q=./two-pointers/0125-valid-palindrome.py) | $O(n)$ | $O(1)$ | Two converging pointers |

| # | Problem | Difficulty | Solution | Time | Space | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 0121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | `Easy` | [0121-best-time-to-buy-and-sell-stock.py](https://www.google.com/search?q=./sliding-window/0121-best-time-to-buy-and-sell-stock.py) | $O(n)$ | $O(1)$ | Rolling min tracker |

---

## 🛠️ Environment & Tooling

* **Language:** Python `3.10+`
* **Editor:** Visual Studio Code
* **Linter & Formatter:** `ruff` / `black`
* **Testing:** Local assertion blocks (`assert`) in each file
* **Platform Profile:** [LeetCode - abhayv175](https://leetcode.com/u/abhayv175/)

```

```
