import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def explore_directory(path, indent=0):
    space = " " * indent
    for item in path.iterdir():
        if item.is_dir():
            print(f"{space}{Fore.BLUE}📁 Папка: {item.name}")
            explore_directory(item, indent + 4)
        else:
            print(f"{space}{Fore.GREEN}📄 Файл: {item.name}")


target_path = Path(sys.argv[1])

if target_path.exists():
    print("папка існує")
    if target_path.is_dir():
        print("цей обєкт є папкою\n")
        explore_directory(target_path)
    else:
        print("Це файл, а не папка!")
else:
    print("Такого шляху взагалі не існує!")
