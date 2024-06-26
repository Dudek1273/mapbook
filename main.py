import sqlite3
from getpass import getpass


def create_tables():
    conn = sqlite3.connect('vet_clinic.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS companies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_id INTEGER,
                    name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    FOREIGN KEY (company_id) REFERENCES companies (id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)''')

    conn.commit()
    conn.close()


def register_user():
    username = input("Podaj nazwę użytkownika: ")
    password = getpass("Podaj hasło: ")

    conn = sqlite3.connect('vet_clinic.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

    print("Rejestracja zakończona sukcesem.")
    main_menu()


def login():
    username = input("Podaj nazwę użytkownika: ")
    password = getpass("Podaj hasło: ")

    conn = sqlite3.connect('vet_clinic.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        print("Logowanie zakończone sukcesem.")
        user_menu()
    else:
        print("Nieprawidłowa nazwa użytkownika lub hasło.")
        main_menu()


def manage_companies():
    while True:
        print("\nZarządzanie firmami:")
        print("1. Dodaj firmę")
        print("2. Wyświetl firmy")
        print("3. Aktualizuj firmę")
        print("4. Usuń firmę")
        print("0. Powrót")

        choice = int(input("Wybierz opcję: "))

        conn = sqlite3.connect('vet_clinic.db')
        c = conn.cursor()

        if choice == 1:
            name = input("Podaj nazwę firmy: ")
            address = input("Podaj adres firmy: ")
            c.execute('INSERT INTO companies (name, address) VALUES (?, ?)', (name, address))
            conn.commit()
            print("Firma została dodana.")

        elif choice == 2:
            c.execute('SELECT * FROM companies')
            companies = c.fetchall()
            for company in companies:
                print(company)

        elif choice == 3:
            company_id = int(input("Podaj ID firmy do aktualizacji: "))
            name = input("Podaj nową nazwę firmy: ")
            address = input("Podaj nowy adres firmy: ")
            c.execute('UPDATE companies SET name = ?, address = ? WHERE id = ?', (name, address, company_id))
            conn.commit()
            print("Firma została zaktualizowana.")

        elif choice == 4:
            company_id = int(input("Podaj ID firmy do usunięcia: "))
            c.execute('DELETE FROM companies WHERE id = ?', (company_id,))
            conn.commit()
            print("Firma została usunięta.")

        elif choice == 0:
            conn.close()
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def manage_employees():
    while True:
        print("\nZarządzanie pracownikami:")
        print("1. Dodaj pracownika")
        print("2. Wyświetl pracowników")
        print("3. Aktualizuj pracownika")
        print("4. Usuń pracownika")
        print("0. Powrót")

        choice = int(input("Wybierz opcję: "))

        conn = sqlite3.connect('vet_clinic.db')
        c = conn.cursor()

        if choice == 1:
            company_id = int(input("Podaj ID firmy: "))
            name = input("Podaj imię i nazwisko pracownika: ")
            position = input("Podaj stanowisko pracownika: ")
            c.execute('INSERT INTO employees (company_id, name, position) VALUES (?, ?, ?)',
                      (company_id, name, position))
            conn.commit()
            print("Pracownik został dodany.")

        elif choice == 2:
            c.execute('SELECT * FROM employees')
            employees = c.fetchall()
            for employee in employees:
                print(employee)

        elif choice == 3:
            employee_id = int(input("Podaj ID pracownika do aktualizacji: "))
            name = input("Podaj nowe imię i nazwisko pracownika: ")
            position = input("Podaj nowe stanowisko pracownika: ")
            c.execute('UPDATE employees SET name = ?, position = ? WHERE id = ?', (name, position, employee_id))
            conn.commit()
            print("Pracownik został zaktualizowany.")

        elif choice == 4:
            employee_id = int(input("Podaj ID pracownika do usunięcia: "))
            c.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
            conn.commit()
            print("Pracownik został usunięty.")

        elif choice == 0:
            conn.close()
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def manage_clients():
    while True:
        print("\nZarządzanie klientami:")
        print("1. Dodaj klienta")
        print("2. Wyświetl klientów")
        print("3. Aktualizuj klienta")
        print("4. Usuń klienta")
        print("0. Powrót")

        choice = int(input("Wybierz opcję: "))

        conn = sqlite3.connect('vet_clinic.db')
        c = conn.cursor()

        if choice == 1:
            name = input("Podaj imię i nazwisko klienta: ")
            address = input("Podaj adres klienta: ")
            c.execute('INSERT INTO clients (name, address) VALUES (?, ?)', (name, address))
            conn.commit()
            print("Klient został dodany.")

        elif choice == 2:
            c.execute('SELECT * FROM clients')
            clients = c.fetchall()
            for client in clients:
                print(client)

        elif choice == 3:
            client_id = int(input("Podaj ID klienta do aktualizacji: "))
            name = input("Podaj nowe imię i nazwisko klienta: ")
            address = input("Podaj nowy adres klienta: ")
            c.execute('UPDATE clients SET name = ?, address = ? WHERE id = ?', (name, address, client_id))
            conn.commit()
            print("Klient został zaktualizowany.")

        elif choice == 4:
            client_id = int(input("Podaj ID klienta do usunięcia: "))
            c.execute('DELETE FROM clients WHERE id = ?', (client_id,))
            conn.commit()
            print("Klient został usunięty.")

        elif choice == 0:
            conn.close()
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Zarejestruj użytkownika")
        print("2. Zaloguj się")
        print("0. Wyjdź")

        choice = int(input("Wybierz opcję: "))

        if choice == 1:
            register_user()
        elif choice == 2:
            login()
        elif choice == 0:
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def user_menu():
    while True:
        print("\nMenu użytkownika:")
        print("1. Zarządzaj firmami")
        print("2. Zarządzaj pracownikami")
        print("3. Zarządzaj klientami")
        print("0. Wyloguj się")

        choice = int(input("Wybierz opcję: "))

        if choice == 1:
            manage_companies()
        elif choice == 2:
            manage_employees()
        elif choice == 3:
            manage_clients()
        elif choice == 0:
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    create_tables()
    main_menu()1