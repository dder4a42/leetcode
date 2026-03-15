# mono_stack

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| largestRectangleArea | Largest Rectangle in Histogram | https://leetcode.com/problems/largest-rectangle-in-histogram/ | - | ./largestRectangleArea/solution.py | largestrectanglearea |
| next_smaller_number | Next Smaller Number | - | - | ./next_smaller_number/solution.py | next_smaller_number |

## 题目分析

### largestrectanglearea
单调递增栈维护候选柱子。每次遇到更矮柱子时持续出栈，
被弹出元素即可确定右边界；新栈顶即其左边界，进而计算最大矩形面积。

### next_smaller_number
维护单调栈；当新元素小于栈顶时，栈顶元素的 next smaller 被确定为当前元素。
1. 商品折扣后的最终价格：将下一个小于自己的数字作为折扣，则需要为每一元素寻找下一个小于自己的数字，用单调栈实现。
    - 单调栈即尝试令遇到的每一元素入栈，并维护单调增序列。若新元素破坏了单调性，则至少栈顶元素遇到了下一个小于自己的数字，于是不断出栈直至重新满足单调性。
    - 可以认为，单调栈存储了一些尚在观望的投机元素，只要有折扣就下车。每个元素入栈一次、出栈一次。
2. 柱状图中的最大矩形：枚举极大值，接着选出最大值。对每一柱子，尽量向两侧扩张，直至遇到下一个小于自己的柱子，从而得到一个极大矩形。
    - 单调栈可以帮助找到右侧第一个小于自己的柱子，即被出栈时，待入栈元素为扩张的右边界。
    - 大小是相对的，停止出栈时，待入栈元素也遇到了左侧第一个小于自己的柱子。
    - 在左右两侧添加哨兵柱子，简化边界情况处理。