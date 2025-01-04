# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 08:07:25 2025

@author: purna
"""

import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def read_file(file_name):
    if not os.path.exists(file_name):
        open(file_name, 'w').close()
    with open(file_name, 'r') as file:
        return file.readlines()

def write_to_file(file_name, data, mode='a'):
    with open(file_name, mode) as file:
        file.write(data + "\n")

def check_account(account_number):
    accounts = read_file('accounts.txt')
    for account in accounts:
        details = account.strip().split(', ')
        if details[0] == account_number:
            return details
    return None

def create_account():
    flage = True
    name = input("Enter your name: ")

    while flage:
        if len(name)<4 :
            name = input("enter valid input: ")
        else:
            flage = False
    flage = True
    while flage:
        try:
            initial_deposit = float(input("Enter your initial deposit not less than $500: "))
            if initial_deposit < 499.99  :
                pass
            else:
                flage = False
        except ValueError:
            initial_deposit = float(input("please enter a valid amount: "))
    flage = True
    while flage:
        password = input("enter a eight digit password : ")
        if len(password)<8:
            pass
        else:
            flage = False
    account_number = str(hash(name + password) % 100000000000).zfill(11)
    hashed_password = hash_password(password)

    account_data = f"{account_number}, {name}, {hashed_password}, {initial_deposit}"
    write_to_file('accounts.txt', account_data)

    print(f"Account created successfully! Your account number: {account_number}")

def login():
    account_number = input("Enter your 11 digit account number: ")
    password = input("Enter your password: ")

    account = check_account(account_number)
    if account and account[2] == hash_password(password):
        print("Login successful!")
        return account
        
    print("Invalid account number or password.")
    return None

def transaction(account):
    print(f"your balance is {account[3]}")
    print("1. Deposit")
    print("2. Withdraw")
    user_choice = input("Enter your choice: ")
    
    flage = True
    while flage:
        try:
            amount= float(input("Enter your amount: "))
            if amount < float(100):
                pass
            else:
                flage = False
        except ValueError:
             amount = float(input("please enter a valid amount: "))

    if user_choice == '1':
        account[3] = str(float(account[3]) + amount)
        transaction = f"{account[0]}, Deposit, {amount}"
    elif user_choice == '2' and float(account[3]) >= amount:
        account[3] = str(float(account[3]) - amount)
        transaction = f"{account[0]}, Withdrawal, {amount}"

    else:
        print("Insufficient balance.")
        return

    write_to_file('transactions.txt', transaction)
    update_account(account)
    print(f"Transaction successful! New balance: {account[3]}")


def update_account(account):
    accounts = read_file('accounts.txt')
    updated_data = "\n".join(
        [f"{','.join(account)}" if acc.startswith(account[0]) else acc.strip() for acc in accounts]
    )
    write_to_file('accounts.txt', updated_data, mode='w')

def main():
    while True:
        print("Welcome to banking system")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            create_account()
        elif user_choice =="2":
            account = login()
            if account:
                transaction(account)
        elif user_choice == "3":
            print("Thank you for choosing us!")
            break
        else:
            print("Please enter a valid input")
main()