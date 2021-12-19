import os


def read_cookbook():
    cook_book = {}

    with open('recipes.txt', encoding='UTF-8') as file:
        for line in file:
            ingredients_list = []
            dish_name = line.strip()

            get_num_of_ingredients = int(file.readline())
            quantity_of_ingredients = int(get_num_of_ingredients)

            for ingredient in range(quantity_of_ingredients):
                ingredients = {}

                ingredient = file.readline().strip()
                ingredient = ingredient.strip()
                ingredients['ingredient_name'], (ingredients['quantity']), ingredients['measure'] = ingredient.split('|')
                ingredients_list.append(ingredients)
            file.readline()
            cook_book[dish_name] = ingredients_list

    return cook_book


result = read_cookbook()
print(result)