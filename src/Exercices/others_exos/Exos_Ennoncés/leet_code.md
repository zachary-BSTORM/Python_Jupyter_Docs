# Exercise 1 — PIN Variations

Alright, detective.

One of our colleagues successfully observed our target, Robby the robber. We followed him to a secret warehouse where we assume all the stolen goods are stored. The warehouse door is secured by an electronic combination lock. Unfortunately, our spy is not completely sure about the PIN he saw when Robby entered it.

The keypad has the following layout:

1 2 3  
4 5 6  
7 8 9  
--0--

He noted the PIN `1357`, but each observed digit could actually be any adjacent digit (horizontally or vertically, not diagonally).

Examples:
- Instead of `1`, it could also be `2` or `4`
- Instead of `5`, it could also be `2`, `4`, `6`, or `8`

The lock allows unlimited attempts, so all possible variations can be tested.

Task:
Write a function that returns all possible PIN variations based on the observed PIN (length between 1 and 8 digits).

Function names:
- `getPINs` (JavaScript / Java / Kotlin)
- `get_pins` (Python)
- `GetPINs` (C#)

Important:
- All PINs must be returned as strings (to preserve leading zeros)


---

# Exercise 2 — Strip Comments

Complete the solution so that it removes all text following any of a set of comment markers.

Also remove any trailing whitespace at the end of each line.

## Example

Input:

apples, pears # and bananas
grapes
bananas !apples


Output:

apples, pears
grapes
bananas



---

# Exercise 3 — Snail Sort

Given an `n x n` array, return its elements arranged in a clockwise spiral from the outermost layer to the center.

## Example 1

Input:

[[1,2,3],
[4,5,6],
[7,8,9]]


Output:

[1,2,3,6,9,8,7,4,5]


## Example 2

Input:<br>
[[1,2,3],<br>
[8,9,4],<br>
[7,6,5]]<br>
<br>

Output:

[1,2,3,4,5,6,7,8,9]



---

# Exercise 4 — Roman Numerals

Write two functions:
- One to convert an integer to a Roman numeral
- One to convert a Roman numeral to an integer

## Rules

- Process digits from left to right
- Skip digits with value 0
- Use standard modern Roman numeral notation

Examples:
- `1990` → `MCMXC`
- `2008` → `MMVIII`
- `1666` → `MDCLXVI`

Note:
- `4` must be written as `IV`, not `IIII`

## Examples

### To Roman

- 2000 -> "MM"
- 1666 -> "MDCLXVI"
- 86   -> "LXXXVI"
- 1    -> "I"

### From Roman

- "MM"      -> 2000
- "MDCLXVI" -> 1666
- "LXXXVI"  -> 86
- "I"       -> 1


## Reference Table

| Symbol | Value |
|--------|-------|
| M      | 1000  |
| CM     | 900   |
| D      | 500   |
| CD     | 400   |
| C      | 100   |
| XC     | 90    |
| L      | 50    |
| XL     | 40    |
| X      | 10    |
| IX     | 9     |
| V      | 5     |
| IV     | 4     |
| I      | 1     |


Constraints:

1 <= n < 4000



---

# Exercise 5 — Daily Temperatures

Given an array `temperatures`, return an array `answer` such that:

- `answer[i]` is the number of days you must wait after day `i` to get a warmer temperature
- If no warmer day exists, `answer[i] = 0`

## Examples

### Example 1

Input: [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]


### Example 2

Input: [30,40,50,60]
Output: [1,1,1,0]


### Example 3

Input: [30,60,90]
Output: [1,1,0]


## Constraints


1 <= temperatures.length <= 100000
30 <= temperatures[i] <= 100