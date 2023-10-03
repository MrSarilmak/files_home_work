# Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения


with open('files1.txt', 'r') as f:
    file_list = f.readlines()

last_dish = ["", 0, []]
cook_book = dict()

for line in file_list:
    line = line.replace('\n', '')
    if line.isdigit():
        last_dish[1] = int(line)
    elif len(line.split(" | ")) > 1:
        last_dish[2].append(line.split("|"))
    elif line == '':
        cook_book[last_dish[0]] = {
            'ingredient_name': last_dish[2],
            'quantity': last_dish[2],
            'measure': last_dish[2]
        }
        last_dish[1] = 0
        last_dish[2] = []
        # continue
    else:
        last_dish[0] = line
    # if last_dish[0] and last_dish[1] > 0 and last_dish[2]:
    #     cook_book[last_dish[0]] = {
    #         'ingredient_name': last_dish[2],
    #         'quantity': last_dish[2],
    #         'measure': last_dish[2]
    #     }

print(cook_book)
