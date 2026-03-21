# LeetCode 题解导航

> 本文件由 generate_index.py 自动生成。

## 子目录 index.md 约定（INDEX_FORMAT_V1）

每个题型目录（如 hash、mono_stack）建议使用如下 Markdown 表格：

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| two_sum | Two Sum | https://leetcode.com/problems/two-sum/ | ./two_sum/README.md | ./two_sum/solution.py | two_sum |

说明：
- slug：题目目录名（必须与文件夹一致）
- title：题目标题（可中文或英文）
- leetcode：LeetCode 题目 URL
- solution：本地题解文档相对路径（相对于当前题型目录）
- code：实现代码相对路径（相对于当前题型目录）
- analysis_anchor：可选，指向当前题型 index.md 中的分析段锚点（如 two_sum）
- 若 analysis_anchor 为空，但存在标题 `### <slug>`，会自动链接到该标题

分析段推荐写法：
- 在题型 index.md 中添加 `## 题目分析`
- 每题一段，使用 `### <slug>` 作为小节标题

## 题目索引

### hash
- 目录说明：[index.md](data_structures_and_algorithms_quest/hash/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [copy_randomlist](data_structures_and_algorithms_quest/hash/copy_randomlist) | [题目](https://leetcode.com/problems/copy-list-with-random-pointer/) | [分析](data_structures_and_algorithms_quest/hash/index.md#copy_randomlist) | [solution.py](data_structures_and_algorithms_quest/hash/copy_randomlist/solution.py) |
| [firstmissingpositive](data_structures_and_algorithms_quest/hash/firstmissingpositive) | [题目](https://leetcode.com/problems/first-missing-positive/) | [分析](data_structures_and_algorithms_quest/hash/index.md#firstmissingpositive) | [solution.py](data_structures_and_algorithms_quest/hash/firstmissingpositive/solution.py) |
| [two_sum](data_structures_and_algorithms_quest/hash/two_sum) | [题目](https://leetcode.com/problems/two-sum/) | [分析](data_structures_and_algorithms_quest/hash/index.md#two_sum) | [solution.py](data_structures_and_algorithms_quest/hash/two_sum/solution.py) |

### heap

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [construct-target-array-with-multiple-sums](data_structures_and_algorithms_quest/heap/construct-target-array-with-multiple-sums) | 待补充 | 待补充 | [solution.py](data_structures_and_algorithms_quest/heap/construct-target-array-with-multiple-sums/solution.py) |
| [latest_stone_weight](data_structures_and_algorithms_quest/heap/latest_stone_weight) | 待补充 | 待补充 | [solution.py](data_structures_and_algorithms_quest/heap/latest_stone_weight/solution.py) |
| [least_two_sum](data_structures_and_algorithms_quest/heap/least_two_sum) | 待补充 | 待补充 | [solution.py](data_structures_and_algorithms_quest/heap/least_two_sum/solution.py) |

### linked_list
- 目录说明：[index.md](data_structures_and_algorithms_quest/linked_list/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [odd_even_list](data_structures_and_algorithms_quest/linked_list/odd_even_list) | [题目](https://leetcode.com/problems/odd-even-linked-list/) | [分析](data_structures_and_algorithms_quest/linked_list/index.md#odd_even_list) | [solution.py](data_structures_and_algorithms_quest/linked_list/odd_even_list/solution.py) |
| [reverse_list](data_structures_and_algorithms_quest/linked_list/reverse_list) | [题目](https://leetcode.com/problems/reverse-linked-list/) | [分析](data_structures_and_algorithms_quest/linked_list/index.md#reverse_list) | [solution.py](data_structures_and_algorithms_quest/linked_list/reverse_list/solution.py) |

### mono_stack
- 目录说明：[index.md](data_structures_and_algorithms_quest/mono_stack/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [largestRectangleArea](data_structures_and_algorithms_quest/mono_stack/largestRectangleArea) | [题目](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [分析](data_structures_and_algorithms_quest/mono_stack/index.md#largestrectanglearea) | [solution.py](data_structures_and_algorithms_quest/mono_stack/largestRectangleArea/solution.py) |
| [next_smaller_number](data_structures_and_algorithms_quest/mono_stack/next_smaller_number) | 待补充 | [分析](data_structures_and_algorithms_quest/mono_stack/index.md#next_smaller_number) | [solution.py](data_structures_and_algorithms_quest/mono_stack/next_smaller_number/solution.py) |

### prefix_sum
- 目录说明：[index.md](data_structures_and_algorithms_quest/prefix_sum/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [minsubarray](data_structures_and_algorithms_quest/prefix_sum/minsubarray) | [题目](https://leetcode.com/problems/make-sum-divisible-by-p/) | [分析](data_structures_and_algorithms_quest/prefix_sum/index.md#minsubarray) | [solution.py](data_structures_and_algorithms_quest/prefix_sum/minsubarray/solution.py) |
| [waystomakefair](data_structures_and_algorithms_quest/prefix_sum/waystomakefair) | [题目](https://leetcode.com/problems/ways-to-make-a-fair-array/) | [分析](data_structures_and_algorithms_quest/prefix_sum/index.md#waystomakefair) | [solution.py](data_structures_and_algorithms_quest/prefix_sum/waystomakefair/solution.py) |

### queue
- 目录说明：[index.md](data_structures_and_algorithms_quest/queue/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [countStudents](data_structures_and_algorithms_quest/queue/countStudents) | [题目](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) | [分析](data_structures_and_algorithms_quest/queue/index.md#countstudents) | [solution.py](data_structures_and_algorithms_quest/queue/countStudents/solution.py) |
| [timeRequiredToBuy](data_structures_and_algorithms_quest/queue/timeRequiredToBuy) | [题目](https://leetcode.com/problems/time-needed-to-buy-tickets/) | [分析](data_structures_and_algorithms_quest/queue/index.md#timerequiredtobuy) | [solution.py](data_structures_and_algorithms_quest/queue/timeRequiredToBuy/solution.py) |

### sort
- 目录说明：[index.md](data_structures_and_algorithms_quest/sort/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [find_k-th_largest](data_structures_and_algorithms_quest/sort/find_k-th_largest) | [题目](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [分析](data_structures_and_algorithms_quest/sort/index.md#find_k-th_largest) | [solution.py](data_structures_and_algorithms_quest/sort/find_k-th_largest/solution.py) |
| [insertion_sort_list](data_structures_and_algorithms_quest/sort/insertion_sort_list) | [题目](https://leetcode.com/problems/insertion-sort-list/) | [分析](data_structures_and_algorithms_quest/sort/index.md#insertion_sort_list) | [solution.py](data_structures_and_algorithms_quest/sort/insertion_sort_list/solution.py) |
| [reductionoperations](data_structures_and_algorithms_quest/sort/reductionoperations) | [题目](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/) | [分析](data_structures_and_algorithms_quest/sort/index.md#reductionoperations) | [solution.py](data_structures_and_algorithms_quest/sort/reductionoperations/solution.py) |
| [sort_array](data_structures_and_algorithms_quest/sort/sort_array) | [题目](https://leetcode.com/problems/sort-an-array/) | [分析](data_structures_and_algorithms_quest/sort/index.md#sort_array) | [solution.py](data_structures_and_algorithms_quest/sort/sort_array/solution.py) |

### stack
- 目录说明：[index.md](data_structures_and_algorithms_quest/stack/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [exclusiveTime](data_structures_and_algorithms_quest/stack/exclusiveTime) | [题目](https://leetcode.com/problems/exclusive-time-of-functions/) | [分析](data_structures_and_algorithms_quest/stack/index.md#exclusivetime) | [solution.py](data_structures_and_algorithms_quest/stack/exclusiveTime/solution.py) |

### string
- 目录说明：[index.md](data_structures_and_algorithms_quest/string/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [repeatedSubstringPattern](data_structures_and_algorithms_quest/string/repeatedSubstringPattern) | [题目](https://leetcode.com/problems/repeated-substring-pattern/) | [分析](data_structures_and_algorithms_quest/string/index.md#repeatedsubstringpattern) | [solution.py](data_structures_and_algorithms_quest/string/repeatedSubstringPattern/solution.py) |

### double_ptr
- 目录说明：[index.md](double_ptr/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [container_with_most_water](double_ptr/container_with_most_water) | [题目](https://leetcode.com/problems/container-with-most-water/) | [分析](double_ptr/index.md#container_with_most_water) | [solution.py](double_ptr/container_with_most_water/solution.py) |
| [twosum_ii](double_ptr/twosum_ii) | [题目](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [分析](double_ptr/index.md#twosum_ii) | [solution.py](double_ptr/twosum_ii/solution.py) |

### dp

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [climbng_stairs_ii](dp/climbng_stairs_ii) | 待补充 | 待补充 | [solution.py](dp/climbng_stairs_ii/solution.py) |

### robs
- 目录说明：[index.md](dp/robs/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [count_house_placements](dp/robs/count_house_placements) | [题目](https://leetcode.cn/problems/count-number-of-ways-to-place-houses/description/) | [分析](dp/robs/index.md#count_house_placements) | [solution.py](dp/robs/count_house_placements/solution.py) |
| [cycle_rob](dp/robs/cycle_rob) | [题目](https://leetcode.cn/problems/house-robber-ii/) | [分析](dp/robs/index.md#cycle_rob) | [solution.py](dp/robs/cycle_rob/solution.py) |

### prefix_sum

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [subarray_sum_equals_k](prefix_sum/subarray_sum_equals_k) | 待补充 | 待补充 | [solution.py](prefix_sum/subarray_sum_equals_k/solution.py) |

### simulation
- 目录说明：[index.md](simulation/index.md)

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [binary_add](simulation/binary_add) | [题目](https://leetcode.com/problems/add-binary/) | [分析](simulation/index.md#binary_add) | [solution.py](simulation/binary_add/solution.py) |

### slide_window

| 题目目录 | LeetCode | 本地题解 | 实现代码 |
| --- | --- | --- | --- |
| [lengthoflongestsubstring](slide_window/lengthoflongestsubstring) | 待补充 | 待补充 | [solution.py](slide_window/lengthoflongestsubstring/solution.py) |
| [maximumsumofalmostuniquesubarray](slide_window/maximumsumofalmostuniquesubarray) | 待补充 | 待补充 | [solution.py](slide_window/maximumsumofalmostuniquesubarray/solution.py) |
| [minarrivalstodiscard](slide_window/minarrivalstodiscard) | 待补充 | 待补充 | [solution.py](slide_window/minarrivalstodiscard/solution.py) |

## 文件树

```text
leetcode/
├── data_structures_and_algorithms_quest/
│   ├── hash/
│   │   ├── copy_randomlist/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   ├── firstmissingpositive/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   └── two_sum/
│   │       ├── solution.py
│   │       └── test_cases.txt
│   ├── heap/
│   │   ├── construct-target-array-with-multiple-sums/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   ├── latest_stone_weight/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   └── least_two_sum/
│   │       ├── solution.py
│   │       └── test_cases.txt
│   ├── linked_list/
│   │   ├── odd_even_list/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   └── reverse_list/
│   │       ├── solution.py
│   │       └── test_cases.txt
│   ├── mono_stack/
│   │   ├── largestRectangleArea/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   └── next_smaller_number/
│   │       ├── solution.py
│   │       └── test_cases.txt
│   ├── prefix_sum/
│   │   ├── minsubarray/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   └── waystomakefair/
│   │       ├── solution.py
│   │       └── test_cases.txt
│   ├── queue/
│   │   ├── countStudents/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   └── timeRequiredToBuy/
│   │       ├── solution.py
│   │       └── test_cases.txt
│   ├── sort/
│   │   ├── find_k-th_largest/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   ├── insertion_sort_list/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   ├── reductionoperations/
│   │   │   ├── solution.py
│   │   │   └── test_cases.txt
│   │   └── sort_array/
│   │       ├── solution.py
│   │       └── test_cases.txt
│   ├── stack/
│   │   └── exclusiveTime/
│   │       ├── solution.py
│   │       └── test_cases.txt
│   └── string/
│       └── repeatedSubstringPattern/
│           ├── solution.py
│           └── test_cases.txt
├── double_ptr/
│   ├── container_with_most_water/
│   │   ├── solution.py
│   │   └── test_cases.txt
│   └── twosum_ii/
│       ├── solution.py
│       └── test_cases.txt
├── dp/
│   └── climbng_stairs_ii/
│       ├── solution.py
│       └── test_cases.txt
│   └── robs/
│       ├── count_house_placements/
│       │   ├── solution.py
│       │   └── test_cases.txt
│       └── cycle_rob/
│           ├── solution.py
│           └── test_cases.txt
├── prefix_sum/
│   └── subarray_sum_equals_k/
│       ├── solution.py
│       └── test_cases.txt
├── simulation/
│   └── binary_add/
│       ├── solution.py
│       └── test_cases.txt
└── slide_window/
    ├── lengthoflongestsubstring/
    │   ├── solution.py
    │   └── test_cases.txt
    ├── maximumsumofalmostuniquesubarray/
    │   ├── solution.py
    │   └── test_cases.txt
    └── minarrivalstodiscard/
        ├── solution.py
        └── test_cases.txt
```
