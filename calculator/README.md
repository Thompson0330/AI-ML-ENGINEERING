# 🧮 Python Logic Calculator

A practical arithmetic tool that focuses on **input validation** and **loop control**. This project was built to practice handling user data safely and preventing common program crashes.

## 🚀 Key Features
- **Continuous Operation**: Uses a `while True` loop so you can perform multiple calculations in one session.
- **Input Protection**: If a user enters a letter instead of a number, the `try/except` block catches the error and resets the loop.
- **Smart Logic Gates**: 
    - Uses `continue` to jump back to the start if an error occurs.
    - Prevents **Division by Zero** errors with a dedicated check.
    - Validates operators to ensure only `+`, `-`, `x`, or `/` are used.

## 🛠️ Built With
- **Language**: Python 3.14.3
- **Concepts**: Error Handling (`ValueError`), Conditional Logic, and Flow Control.

## 📂 Project Path
`AI-ML-ENGINEERING/calculator/calculator.py`

## 📖 How to Run
1. Navigate to the folder:
   ```bash
   cd calculator
   ```
2. Run the script:
   ```bash
   python calculator.py
   ```

## 🧪 Logic Example
**Handling a Mistake:**
```text
num1: hello
input a number  <-- (Program resets instead of crashing)
num1: 10
num2: 2
operator: /
5.0
```

---
*Part of my AI-ML Engineering foundations repository.*
