# Practice Problems

---

## 1. Backspace String Compare

### Description
Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `#` means a backspace character.

Note: After backspacing an empty text, the text remains empty.

### Examples

**Example 1**
- Input: `s = "ab#c"`, `t = "ad#c"`
- Output: `true`
- Explanation: Both `s` and `t` become `"ac"`

**Example 2**
- Input: `s = "ab##"`, `t = "c#d#"`
- Output: `true`
- Explanation: Both `s` and `t` become `""`

**Example 3**
- Input: `s = "a#c"`, `t = "b"`
- Output: `false`
- Explanation: `s` becomes `"c"` while `t` becomes `"b"`

### Constraints
- `1 <= s.length, t.length <= 200`
- `s` and `t` only contain lowercase letters and `#`

### Follow-up
Can you solve it in **O(n)** time and **O(1)** space?

---

## 2. Simplify Path

### Description
You are given an absolute path for a Unix-style file system, which always begins with a slash `/`.

Your task is to transform this path into its simplified canonical path.

### Rules
- `.` represents the current directory → ignore it  
- `..` represents the parent directory → go back one level  
- Multiple slashes (`//`, `///`) are treated as a single `/`  
- Any other sequence (e.g., `...`) is a valid directory name  

### Requirements
The final path must:
1. Start with `/`
2. Use a single `/` between directories
3. Not end with `/` (except root `/`)
4. Not contain `.` or `..`

### Example

Input:  
`/a/./b/../../c/`

Output:  
`/c`

### Goal
Return the simplified canonical path as a string.

---

## 3. Longest Substring Without Repeating Characters

### Description
Given a string `s`, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within a string.

### Requirements
- The substring must contain only unique characters
- Return the length of the longest valid substring
- Aim for a linear time solution

### Examples

**Example 1**
- Input: `"abcabcbb"`
- Output: `3`
- Explanation: `"abc"`

**Example 2**
- Input: `"bbbbb"`
- Output: `1`
- Explanation: `"b"`

**Example 3**
- Input: `"pwwkew"`
- Output: `3`
- Explanation: `"wke"`

---

## 4. CheckDOM - HTML Element

### Description
Have the function `CheckDOM(strParam)` read a string of HTML elements and text.

Supported tags: `<b>`, `<i>`, `<em>`, `<div>`, `<p>`

### Cases

1. **Correct**  
   The HTML is properly nested → return `true`

2. **Almost correct**  
   One tag change fixes it → return the first tag to change  
   (No adding/removing tags, no switching opening/closing)

3. **Incorrect**  
   Requires more than one change → return `false`

### Examples

| Input | Output | Reason |
|------|--------|--------|
| `"<div><b><p>hello</p></b></div>"` | `true` | Proper nesting |
| `"<div><i>hello</i>world</b>"` | `"div"` | Changing `<div>` fixes it |
| `"</div><p></p><div>"` | `false` | Order incorrect |
| `"<em></em><em></em><p></b>"` | `"p"` | Change `<p>` to `<b>` |
| `"<div><p></p><b><p></div>"` | `false` | Multiple fixes needed |