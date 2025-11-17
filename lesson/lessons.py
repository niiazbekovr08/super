import re 
file_path = r"C:\Users\user\Desktop\lesson\mockdata.txt"

with open(file_path, "r", encoding='utf-8') as f:
    text = f.read()

names = re.findall(r'^[A-Za-z]+', text, flags=re.MULTILINE)
print("Names:", names)

surnames = re.findall(r'(?<=\s)[A-Za-z]+(?=\s)', text)
print("Surnames:", surnames)

file_types = re.findall(r'\.\w{2,4}\b', text)
print("File types:", file_types)

with open("name.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(names))

with open("surname.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(surnames))

with open("typeFile.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(file_types))

print("Файлы созданы!")