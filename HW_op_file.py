cook_book = {}

#
# def cook_meal(file_name):
#     cook_recipe = []
#     x = []
#     with open(file_name, encoding='UTF-8') as file:
#         for line in file:
#             print(line)
#             #cook_recipe.append(line.strip())
#             omlet = int(file.readline().strip())
#             for ing_type in range(omlet):
#                 file.readline()
#                 x_file = file.readlines()
#                 for x in x_file:
#                     file.readline()
#                     #print(x)
#             file.readline()
#     #print(cook_recipe)




def cook_omlet(file_name):
    omlet = {}
    ingredient = []
    ingredient_2 = {}
    with open(file_name, encoding='UTF-8') as file:
        row = file.readlines(1)
        for line in row:
            cook_book[line.strip()] = ingredient
            rows = file.readlines(2)
            x = []
            for i in rows:
                x.append(i)
            x.remove('3\n')
            for p in x:
                egg = p[:4]
                quantity = int(p[7:8])
                measure = p[11:13]
                omlet['ingredient_name'] = egg
                omlet['quantity'] = quantity
                omlet['measure'] = measure
                ingredient.append(omlet)
                rows = file.readlines(1)
                for milk in rows:
                    ingredient_milk = milk[:6].strip()
                    quantity_milk = int(milk[8:12].strip())
                    measure_milk = milk[15:18].strip()
                    ingredient_2['ingredient_name'] = ingredient_milk
                    ingredient_2['quantity'] = quantity_milk
                    ingredient_2['measure'] = measure_milk
                    all_ingredients = [ingredient_2]
                    print(all_ingredients)



cook_omlet('recipes.txt')
print(cook_book)

