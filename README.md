# CSC 301 - Third Assignment

**Examples of Recursion, Dynamic Arrays, Linked Lists + Amortized Analysis**

### Student Details
- **Name:** Akerele Paul Bayo  
- **Matric Number:** 240502023  
- **Course Code:** CSC 301  

---

## 1. Amortized Analysis

**What is Amortized Analysis?**

Amortized analysis is a technique used to analyze the time complexity of a sequence of operations on a data structure.  
Instead of looking at the worst-case cost of a single operation, it calculates the average cost of each operation over a long sequence of operations (in the worst case).

It is especially useful when some operations are occasionally expensive, but those expensive operations happen rarely. The high cost is "spread out" (amortized) across many cheaper operations.

**Simple Example:**  
In a dynamic array, most insertions take O(1) time. Sometimes the array must resize (which takes O(n) time). Using amortized analysis, we can prove that the average cost of each insertion is still **O(1)**.

---

## 2. Examples

### A. Recursion Example (Factorial)
See file: `recursion_example.py`

### B. Dynamic Array Example
See file: `dynamic_array_example.py`

### C. Linked List Example
See file: `linked_list_example.py`

---

## How to Run

```bash
python recursion_example.py
python dynamic_array_example.py
python linked_list_example.py
```
