

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
print(result)
