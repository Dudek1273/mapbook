from FunkcjeFirmy import show_companies, add_company, remove_company, update_company, companies_map
from FunkcjeKlienci import show_clients, add_client, remove_client, update_client, clients_map
from FunkcjePracownicy import show_workers, add_worker, remove_worker, update_worker, workers_map, \
    show_animals_under_care
from Lista import companies, clients, workers, animals


def logowanie():
    correct_login = "klinika"
    correct_password = "1234"
    logowanie = False

    while not logowanie:
        login = input("Wprowadź login: ")
        password = input("Wprowadź hasło: ")

        if login == correct_login and password == correct_password:
            print("Pomyślnie zalogowano.")
            logowanie = True
        else:
            print("Niepoprawny login lub hasło.")
    return logowanie


if logowanie():
    if __name__ == '__main__':
        print("Witaj w systemie zarządzania klinikami weterynaryjnymi.")
        while True:
            print("Menu:")
            print("0. Zakończ pracę")
            print("1. Kliniki weterynaryjne")
            print("2. Klienci")
            print("3. Pracownicy")
            menu_option = input("Wybierz opcję: ")
            if menu_option == '0':
                break
            elif menu_option == '1':
                while True:
                    print("0. Powrót do menu głównego")
                    print("1. Wyświetl listę klinik weterynaryjnych")
                    print("2. Dodaj klinike do listy")
                    print("3. Usuń klinike z listy")
                    print("4. Aktualizuj dane kliniki")
                    print("5. Wyświetl lokalizację wszystkich klinik na mapie")
                    opcja = input("Wybierz opcję: ")
                    if opcja == '0':
                        break
                    elif opcja == '1':
                        show_companies(companies)
                    elif opcja == '2':
                        add_company(companies)
                        show_companies(companies)
                    elif opcja == '3':
                        remove_company(companies)
                        show_companies(companies)
                    elif opcja == '4':
                        update_company(companies)
                        show_companies(companies)
                    elif opcja == '5':
                        companies_map(companies)
                    else:
                        print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
            elif menu_option == '2':
                while True:
                    print("0. Powrót do menu głównego")
                    print("1. Wyświetl listę klientów danej kliniki")
                    print("2. Dodaj klienta do kliniki")
                    print("3. Usuń klienta z kliniki")
                    print("4. Aktualizuj dane klienta")
                    print("5. Wyświetl lokalizację wszystkich klientów na mapie")
                    opcja = input("Wybierz opcję: ")
                    if opcja == '0':
                        break
                    elif opcja == '1':
                        show_clients(clients)
                    elif opcja == '2':
                        add_client(clients, companies)
                    elif opcja == '3':
                        remove_client(clients, companies)
                    elif opcja == '4':
                        update_client(clients, companies)
                    elif opcja == '5':
                        clients_map(clients)
                    else:
                        print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
            elif menu_option == '3':
                while True:
                    print("0. Powrót do menu głównego")
                    print("1. Wyświetl listę pracowników danej kliniki")
                    print("2. Dodaj pracownika do kliniki")
                    print("3. Usuń pracownika z kliniki")
                    print("4. Aktualizuj dane pracownika")
                    print("5. Wyświetl lokalizację wszystkich pracowników na mapie")
                    print("6. Wyświetl liste zwierząt pod opieką pracownika")
                    opcja = input("Wybierz opcję: ")
                    if opcja == '0':
                        break
                    elif opcja == '1':
                        show_workers(workers)
                    elif opcja == '2':
                        add_worker(workers, companies)
                    elif opcja == '3':
                        remove_worker(workers, companies)
                    elif opcja == '4':
                        update_worker(workers, companies, )
                    elif opcja == '5':
                        workers_map(workers)
                    elif opcja == '6':
                        show_animals_under_care(workers, animals)
                    else:
                        print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
            print("Dziękujemy za skorzystanie z systemu. Do widzenia!")
