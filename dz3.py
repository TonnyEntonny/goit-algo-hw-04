import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)
target_path = Path(sys.argv[1])
if target_path.exists():
    print("папка існує")
    if target_path.is_dir():
        print("цей обьект є папкою")
        
        for item in target_path.iterdir():
            if item.is_dir():
                print(f"{Fore.BLUE}📁 Папка: {item.name}")
            else:
                print(f"{Fore.GREEN}📄 Файл: {item.name}")
            
    else:
        print("Це файл, а не папка!")
else:
    print("Такого шляху взагалі не існує!")