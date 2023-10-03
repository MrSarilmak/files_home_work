import json

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    res_dict = {}
    for dish in dishes:
        for i, _ in enumerate(cook_book[dish]):
            res_dict[cook_book[dish][i]['ingredient_name']] = {'measure': cook_book[dish][i]['measure'],
                                                               'quantity': cook_book[dish][i][
                                                                               'quantity'] * person_count}
    return res_dict


# print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2), file=open('files2.json', 'w'))


with open('files2.json', 'w') as f:
    json.dump(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2), f, indent=2, ensure_ascii=False)
