from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path("text.txt")

# Запис тексту у файл
file_path.write_text("""
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000""")

def total_salary(path):
    with open(path, 'r', encoding="utf-8") as fh:
        total = 0
        lines = [el.strip() for el in fh.readlines() if el.strip()] 
        for el in lines:
            name, salary = el.split(',')
            print(name, salary)
            total = total + int(salary)
        average = total / len(lines)
        return total, average
print(total_salary("text.txt"))