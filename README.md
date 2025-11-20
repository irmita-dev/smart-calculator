<!-- Banner -->
<p align="center">
  <img src="https://raw.githubusercontent.com/irmita-dev/smart-calculator/refs/heads/main/smart-calculator-irmita-dev.png" width="100%">
</p>

<h1 align="center">🧮 Smart Calculator (Python)</h1>

<p align="center">
A clean, modular and fully tested command-line calculator built with Python.<br>
Follows clean code principles, separation of concerns and uses <strong>pytest</strong> for unit testing.
</p>

---

## 🚀 Features

- Clean, modular architecture:
  - `src/operations.py`
  - `src/utils.py`
  - `src/calculator.py`
- Supports the following operations:
  - ➕ Addition (`a + b`)
  - ➖ Subtraction (`a - b`)
  - ✖️ Multiplication (`a * b`)
  - ➗ Division (`a / b`)
  - 🔼 Power (`a ** b`)
  - 📊 Percentage (`a % b`)
- Full input validation + helpful error messages
- Interactive user-friendly CLI
- 100% tested mathematical operations using **pytest**
- Easy to extend with new functionality

---

## 📁 Project Structure

smart_calculator/ │ ├── src/ │ ├── calculator.py │ ├── operations.py │ ├── utils.py │ ├── tests/ │ ├── test_operations.py │ ├── main.py ├── requirements.txt └── README.md

---

## 🧪 Running Tests

Install dependencies:

```bash
pip install -r requirements.txt

Run all tests:

pytest

Expected result:

=== 7 passed in X.XXs ===

✔ All tests should pass.


---

▶️ Running the Calculator

Run the CLI application:

python3 main.py

Example session:

Smart Calculator
Type expressions like '10 + 5' or '200 % 10'
Type 'quit' or 'exit' to leave.

> 10 + 5
= 15

> 8 * 3
= 24


---

🔧 Technologies Used

Python 3

Pytest

Modular Architecture

Clean Code Principles



---

📌 Future Improvements

Add scientific functions (sin, cos, sqrt…)

Add command history

Implement optional GUI version (Tkinter or React frontend)

Add logging and configuration file



---

👩‍💻 Author

Irmita Dev
Python Developer · Clean Code · Always Learning & Building

---
