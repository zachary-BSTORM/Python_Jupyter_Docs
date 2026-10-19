# 🚀 CheckDOM - HTML Element - Coderbyte / Odoo Coding Challenge

## 📜 Description
Have the function `CheckDOM(strParam)` read the `strParam` parameter being passed which will be a string of HTML elements and plain text.
The elements that will be used are: `<b>`, `<i>`, `<em>`, `<div>`, `<p>`.

Your program should support **3 cases**:

1.  **Correct**: The string is a correct sequence of nested HTML elements → return `true`.
2.  **Almost correct**: By changing a **single** tag you can make it correct → return the **first tag to change**. 
    *   *Note: Changing a tag does not include adding/removing a tag, or changing an opening tag into a closing tag (and vice versa).*
3.  **Incorrect**: The string requires changing more than one element → return `false`.

---

## 🧩 Examples


| Input | Output | Reason |
| :--- | :--- | :--- |
| `"<div><b><p>hello world</p></b></div>"` | `true` | The HTML is nested correctly. |
| `"<div><i>hello</i>world</b>"` | `"div"` | If the first `<div>` were changed into a `<b>`, it would be properly nested. |
| `"</div><p></p><div>"` | `false` | The order is not respected; changing one tag isn't enough. |
| `"<em></em><em></em><p></b>"` | `p` | Changing `<p>` to `<b>` fixes the sequence. |
| `"<div><p></p><b><p></div>"` | `false` | More than one change required. |
