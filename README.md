# banking-system-console-base
# Simple Banking System

A Python-based banking application that allows users to create accounts, log in, and perform basic transactions like deposits and withdrawals. This project demonstrates file handling, hashing for secure password storage, and basic input validation.

---

## Features

- **Account Creation**:
  - Create a new account with a unique account number.
  - Enforce minimum password length and an initial deposit of at least $500.
  
- **Login**:
  - Secure login using account number and hashed password verification.
  
- **Transactions**:
  - Deposit or withdraw money (minimum $100 per transaction).
  - Prevents overdrafts during withdrawals.
  - Logs all transactions for reference.

- **Data Persistence**:
  - Account details and transaction logs are stored in plain text files (`accounts.txt` and `transactions.txt`).

---

## Requirements

- Python 3.6 or higher.
