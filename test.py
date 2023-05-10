import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("Sau khi hien dong nay man hinh se bi xoa: ")
    a = str(input('Nhap yes: '))
    if a == 'yes':
        os.system('cls')

if __name__ == "__main__":
    main()