from pprint import pprint



def read_cookbook(file_path):
    cook_book = {}
    with open(file_path, encoding='UTF-8') as file:
        for line in file:
            ingredients_list = []
            dish_name = line.strip()

            get_num_of_ingredients = int(file.readline())
            quantity_of_ingredients = int(get_num_of_ingredients)
            for ingredient in range(quantity_of_ingredients):
                ingredients = {}

                ingredient = file.readline().strip()
                ingredient = ingredient.strip()
                ingredients['ingredient_name'], ingredients['quantity'], ingredients['measure'] = ingredient.split('|')
                ingredients['ingredient_name'] = ingredients['ingredient_name'].strip()
                ingredients['quantity'] = ingredients['quantity'].strip()
                ingredients['measure'] = ingredients['measure'].strip()
                ingredients_list.append(ingredients)
            file.readline()
            cook_book[dish_name] = ingredients_list
    return cook_book


result = read_cookbook('recipes.txt')

pprint(result)


def get_shop_list_by_dishes(dishes, persons):
    menu = read_cookbook('recipes.txt')
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'],
                                                              'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    shopping_list.update(items_list)
        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)