import os

files_data = []
files_list = os.listdir("n3_files")
for file in files_list:
    with open(f'n3_files/{file}', 'r') as f:
        file_data = f.read()
        files_data.append([file, len(file_data.split('\n')), file_data.split('\n')])

for i, file_data in enumerate(files_data):
    for file_line in file_data:
        if type(file_line) == str:
            print(file_line, i + 1)
        elif type(file_line) == list:
            for j in file_line:
                print(f"Строка номер {j} файла номер {i + 1}")
        else:
            print(file_line)
