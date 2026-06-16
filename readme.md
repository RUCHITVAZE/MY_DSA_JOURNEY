# 🚀 My DSA Journey

Welcome to my Data Structures and Algorithms (DSA) repository! This repo is a dedicated space where I document my daily coding progress, problem-solving strategies, and conceptual notes as I prepare for technical interviews.

## 📌 Latest Updates & Progress

### 📅 Day 2 (Today) - Frequency Tracking & Optimization
* **Concepts Learned:** * Optimizing factor loops from $\mathcal{O}(N)$ to $\mathcal{O}(\sqrt{N})$ using the square root property.
    * Hash Map mechanics in Python, specifically mastering the `.get(key, default)` method to avoid `KeyError` exceptions.
    * Utilizing `collections.Counter` for rapid frequency counting.
    * Deep dive into analyzing Time Complexity ($\mathcal{O}$) and Space Complexity ($\mathcal{O}$).
* **Problems Solved:**
    * [x] Print Factors of a Number (Brute Force & Optimized)
    * [x] Find Frequency of Array Elements (Hash Map / Dictionary Approach)

### 📅 Day 1 (Yesterday) - Basic Math & Logic
* **Concepts Learned:**
    * Extracting digits from a number using modulo (`% 10`) and integer division (`// 10`).
    * String manipulation vs. mathematical approaches for logic problems.
* **Problems Solved:**
    * [x] Count Digits in a Number
    * [x] Palindrome Number Checker
    * [x] Armstrong Number Verification

---

## 💡 Key Concept Summary

### ⚡ Complexity Cheat Sheet

| Algorithm / Approach | Time Complexity | Space Complexity | Why? |
| :--- | :--- | :--- | :--- |
| **Factors (Brute Force)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Loops through every single number up to $N$. |
| **Factors (Optimized)** | $\mathcal{O}(\sqrt{N})$ | $\mathcal{O}(1)$ | Factors pair up; we only need to check up to $\sqrt{N}$. |
| **Frequency Count (Loop)** | $\mathcal{O}(N)$ | $\mathcal{O}(U)$ | Traverses the array once; space depends on unique elements ($U$). |

### 🛠️ Python Snippet of the Day
The ultimate safe way to count frequencies in a Python dictionary without crashing:
```python
freq[num] = freq.get(num, 0) + 1