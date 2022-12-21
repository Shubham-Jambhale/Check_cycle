# Check_cycle

# Question

You are given an 1D array, Find if there is a cycle in the given array.Assume that moving forward
from the last element puts you on the first element and moving backwards from the first element
puts you on the last element. So, assumption is it is circular array.

if arr[i] > 0, move arr[i] steps forward

if arr[i] < 0, move arr[i] steps backward

if arr[i] = 0, stay idle

# Example 1:

Input array - [2, -1, 1, 2, 2]

Output- True (Cycle Exists)

Explanation:
We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all
its nodes are white (jumping in the same direction)
