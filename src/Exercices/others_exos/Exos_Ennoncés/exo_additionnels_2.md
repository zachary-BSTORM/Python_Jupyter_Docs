# Bracket Matcher

Create a function `BracketMatcher(str)` that takes a string `str` as input and returns `1` if the parentheses in the string are correctly matched and properly nested. Otherwise, return `0`.

## Rules

A string is considered valid if:
- Every opening parenthesis `(` has a corresponding closing parenthesis `)`
- Parentheses are closed in the correct order

If the string contains no parentheses, return `1`.

## Examples

**Input:**  
`"(hello (world))"`  
**Output:**  
`1`

---

**Input:**  
`"((hello (world))"`  
**Output:**  
`0`

---

**Input:**  
`"(coder)(byte))"`  
**Output:**  
`0`

---

**Input:**  
`"(c(oder)) b(yte)"`  
**Output:**  
`1`




# Pick Peaks

Write a function that returns the positions and the values of the **peaks** (or local maxima) of a numeric array.

## Description

A peak is an element that is greater than its immediate neighbors.

For example:  
`arr = [0, 1, 2, 5, 1, 0]`  
→ The peak is at position `3` with value `5`

## Output Format

The function should return an object with two properties:
- `pos`: an array of peak positions
- `peaks`: an array of peak values

If there are no peaks, return:

{ pos: [], peaks: [] }


## Rules

- The first and last elements of the array **cannot be peaks**
- Input arrays will always contain integers (possibly empty)
- No need to validate input

## Plateau Rule

A plateau occurs when consecutive elements have the same value.

- `[1, 2, 2, 2, 1]` → **has a peak**
- `[1, 2, 2, 2, 3]` → **no peak**
- `[1, 2, 2, 2, 2]` → **no peak**

In the case of a plateau peak, return the **position and value of the start of the plateau**

## Examples

**Input:**  
`pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])`  
**Output:**  

{ pos: [3, 7], peaks: [6, 3] }


---

**Input:**  
`pickPeaks([1, 2, 2, 2, 1])`  
**Output:**  

{ pos: [1], peaks: [2] }


# Range Extraction

## Description

A format for expressing an ordered list of integers is to use a comma-separated list of either:

- individual integers  
- or a range of integers denoted by the starting integer separated from the ending integer by a dash (`-`)

A range includes all integers between the start and end values (inclusive).

A sequence is only considered a range if it contains **at least 3 consecutive numbers**.

## Task

Write a function `solution(arr)` that:

- takes a list of integers sorted in increasing order
- returns a string formatted using the range rules described above

## Rules

- Use a single number for isolated values  
- Use the format `start-end` for ranges of **3 or more consecutive numbers**  
- Separate all elements with commas  
- The input list will always be sorted  

## Example

**Input:**


[-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]


**Output:**


"-10--8,-6,-3-1,3-5,7-11,14,15,17-20"


## Explanation

- `-10, -9, -8` → `-10--8` (range of 3 numbers)  
- `-6` → `-6` (single number)  
- `-3, -2, -1, 0, 1` → `-3-1`  
- `3, 4, 5` → `3-5`  
- `7, 8, 9, 10, 11` → `7-11`  
- `14, 15` → `14,15` (only 2 numbers → not a range)  
- `17, 18, 19, 20` → `17-20`