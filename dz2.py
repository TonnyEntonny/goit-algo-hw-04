from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open( path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                cat_id, name, age = parts
                cat_dict = {"id": cat_id,
                "name": name,
                "age": int(age) }
                cats_info.append(cat_dict)

    except FileNotFoundError: 
        print(f"файл не знадено {path}")
    except ValueError: 
        print(f"не вірний формат віку")
    return cats_info
    