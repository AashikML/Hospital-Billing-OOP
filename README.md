# Hospital Billing System (OOP in Python)

A mini object-oriented Python project built to practice core Object-Oriented Programming (OOP) concepts through a realistic hospital billing workflow and publish it cleanly on GitHub.

## What Happened & Why?

While learning Python OOP concepts, writing isolated snippets wasn't enough to build lasting intuition. To apply everything in a real-world scenario, this project was created step by step in **VS Code**:

1. **Designed the `HospitalBill` class:** Set up patient details, doctor name, consultation fee, internal charge tracking, and payment status.
2. **Implemented core billing operations:** Added methods to add item charges, calculate totals, validate payments (handling insufficient funds and change), and print a formatted receipt.
3. **Debugged and refined:** Fixed indentation issues in the test block (`if __name__ == "__main__":`) and verified edge cases such as negative amounts, underpayment, overpayment change, and blocking new charges after a bill is paid.
4. **Version-controlled and published:** Configured Git globally, initialized the repository locally, and pushed the project to GitHub.

## Technologies & Concepts Used

- **Language & Tools:** Python, VS Code, Git, GitHub
- **Encapsulation:** Protected internal attributes (`_charges` and `_is_paid`) keep billing data and settlement state controlled rather than exposed to accidental modification.
- **Abstraction:** Public methods (`add_charge`, `calculate_total`, `pay_bill`, `print_receipt`) expose simple actions while hiding validation checks, sum logic, and state rules inside the class.
- **Static Method (`@staticmethod`):** `is_valid_amount` validates positive numeric values without depending on a specific `HospitalBill` instance.

## About the Creator

**Aashik Pandit** is a 15-year-old aspiring AI/Machine Learning Engineer from Nepal. Alongside school academics, he actively builds projects in Python, SQL, Pandas, NumPy, and embedded electronics (Arduino), focusing on writing clean, scalable code and real-world data/software systems.

- **GitHub:** [@AashikML](https://github.com/AashikML)
- **LinkedIn:** [Aashik Pandit](https://www.linkedin.com/in/AashikML)

### Why Build This Project?

Instead of just memorizing OOP definitions, Aashik builds practical mini-projects from scratch to understand how encapsulation, abstraction, and clean state validation work in real software—while developing strong Git/GitHub habits for future AI and Machine Learning engineering projects.

