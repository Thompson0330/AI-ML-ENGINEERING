# 💰 Overtime Pay Calculator

A Python utility designed to automate payroll calculations. This project demonstrates foundational programming logic, precise data handling, and user-centric error validation.

## 📝 Project Overview
This script calculates an employee's gross monthly pay based on hours worked and a flat hourly rate. It features an automated logic gate to handle **overtime compensation** at a rate of **1.5x** for any time worked beyond the standard 40-hour work week.

## ✨ Key Technical Features
*   **Dynamic Overtime Logic**: Uses conditional branching (`if/else`) to differentiate between regular and overtime pay.
*   **Input Validation**: Implemented `try/except` blocks (in the refactored version) to handle non-numeric inputs without crashing.
*   **Currency Formatting**: Leverages Python **f-strings** with precision specifiers (`:.2f`) to ensure financial data is displayed in a standard currency format.
*   **Clean Code Standards**: Uses descriptive variable naming and modular structure for high readability.

## 🚀 Usage

### 1. File Location
```text
AI-ML-ENGINEERING/pay_calculator/overtimepay_calculator.py
```

### 2. Running the Script
Navigate to your project directory and run:
```bash
python overtimepay_calculator.py
```

### 3. Example Input/Output
**Input:**
- Name: `[Your Name]`
- Hours: `45`
- Rate: `20`

**Output:**
```text
[Your Name]'s pay for the month is 950.00 $
```

## 🧠 Logic Formula
The script calculates the total using the following engineering logic:
- **Base Pay:** $Hours (\leq 40) \times Rate$
- **Overtime:** $(Total Hours - 40) \times (Rate \times 1.5)$
- **Total:** $Base Pay + Overtime$

