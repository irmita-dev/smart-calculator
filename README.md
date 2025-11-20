# 🧮 Smart Calculator (Python)

A clean, modular, fully tested command-line calculator built with Python.  
Designed using best practices: separation of concerns, readable architecture, and unit testing with `pytest`.

---

## 🚀 Features
- Modular architecture (`src/operations.py`, `src/utils.py`, `src/calculator.py`)
- Supports core math operations:
  - Addition (+), Subtraction (-), Multiplication (*), Division (/)
  - Power (**)
  - Percentage (x % y)
- Full input validation & error handling
- Interactive CLI interface
- 100% tested math operations using **pytest**
- Easy to extend with new operations

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

Expected result: all tests pass ✔️


---

▶️ Run the Calculator

python3 main.py

Example:

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

Clean Code practices



---

📌 Future Improvements

Add scientific functions (sin, cos, sqrt…)

Add calculation history

Add GUI version (Tkinter or React front-end)



---

👩‍💻 Author

Irmita Dev
Python Developer | Clean Code | Always learning & building