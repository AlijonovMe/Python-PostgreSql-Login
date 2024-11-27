from colorama import Fore, Back, Style
from database import connect

def run():
    while True:
        command = input(
            Fore.BLUE + "Buyruqlar ro'yxati:\n\n" +
            Fore.GREEN + "stop - Dasturni to'xtatish\n" +
            Fore.GREEN + "login - Ro'yxatdan o'tish\n" +
            Fore.GREEN + "statistic - Statistikani ko'rish\n\n" +
            Fore.BLUE + "Kerakli buyruqni kiriting: " + Style.RESET_ALL
        )

        if command == "login":
            while True:
                first_name = input(Fore.BLUE + "Ismingizni kiriting: ").title()

                if not first_name.isalpha():
                    print(Fore.RED + "Ismingizda faqat harflar bo'lishi kerak!")
                    continue
                break

            while True:
                last_name = input(Fore.BLUE + "Familiyangizni kiriting: ").title()

                if not last_name.isalpha():
                    print(Fore.RED + "Familiyangizda faqat harflar bo'lishi kerak!")
                    continue
                break

            while True:
                login = input(Fore.BLUE + "Yangi loginingizni kiriting: ").lower()

                if not login.isalpha():
                    print(Fore.RED + "Loginingizda faqat harflar bo'lishi kerak!")
                    continue

                elif connect.find('users', 'login', login):
                    print(Fore.RED + "Ushbu login band. Qaytadan urunib ko'ring: ")
                    continue
                break

            while True:
                password = input(Fore.BLUE + "Yangi parolingizni kiriting: ")

                if len(password) < 8:
                    print(Fore.RED + "Parol uzunligi kamida 8 ta belgidan iborat bo'lishi kerak.")
                    continue

                elif not password.isalnum():
                    print(Fore.RED + "Parol faqat harflar va raqamlardan iborat bo'lishi kerak.")
                    continue
                break

            connect.insert_users(first_name, last_name, login, password)
            print(Fore.GREEN + "\nMuvaffaqiyatli ro'yxatdan o'tdingiz!\n")

        elif command == "statistic":
            if connect.counts('users')[0] == 0:
                print(Fore.RED + Style.BRIGHT + "\nHozirda ro'yxatdan o'tgan foydalanuvchilar mavjud emas.\n")
            else:
                print(Fore.BLUE + Style.BRIGHT + "\nRo'yxatdan o'tganlar soni: " + Fore.RED + f"{connect.counts('users')[0]} ta\n")

        elif command == "stop":
            print(Fore.RED + "\nDastur to'xtatildi!")
            break

if __name__ == '__main__':
    connect.create_users()
    run()