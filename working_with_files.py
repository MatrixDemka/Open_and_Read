import pprint as pprint


#Task1
def read_recipes(recipe):
    """
    Функция считывает рецепты из внешнего текстового файла
    и формирует словарь с рецептами.
    :param recipe:
    :return:
    """
    with open(recipe, encoding="utf-8") as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_all = file.readline().split(" | ")
                ingredients.append({
                    "ingredient_name": ingredient_all[0],
                    "quantity": ingredient_all[1],
                    "measure": ingredient_all[2]
                })
            file.readline()
            cook_book[dish_name] = ingredients
    return cook_book


#Task2
def get_shop_list_by_dishes(dishes, person_count):
    """
    Функция возвращает словарь с названием ингредиентов и их количеством для блюд на заданное число персон
    """"""
    :param dishes:
    :param person_count:
    :return:
    """
    quantity_ingredients = {}
    other_ingredients = {}
    for dish in dishes:
        for ingredients in read_recipes(cook_book)[dish]:
            if ingredients["ingredient_name"] in quantity_ingredients:
                other_ingredients[ingredients["ingredient_name"]] = {
                    "measure": ingredients["measure"],
                    "quantity": (int(ingredients["quantity"]) * int(person_count))
                }
            else:
                quantity_ingredients[ingredients["ingredient_name"]] = {
                    "measure": ingredients["measure"],
                    "quantity": (int(ingredients["quantity"]) * int(person_count))
                }
                quantity_ingredients.update(other_ingredients)
    return quantity_ingredients


#pprint.pprint(cook_book)
cook_book = "recipes.txt"
read_recipes(cook_book)

#pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


#Task3
with open ("1.txt", encoding="utf-8") as file_one, open("2.txt", encoding="utf-8") as file_two, open("3.txt", encoding="utf-8") as file_three:
    all_txt_files = {}

    ffile_1 = (file_one.readlines())
    ffile_2 = (file_two.readlines())
    ffile_3 = (file_three.readlines())

    all_txt_files[len(ffile_1)] = ["1.txt", ffile_1]
    all_txt_files[len(ffile_2)] = ["2.txt", ffile_2]
    all_txt_files[len(ffile_3)] = ["3.txt", ffile_3]

#print(sorted(all_txt_files.items()))
#print(all_txt_files[9][1])

with open ("result.txt", "w", encoding="utf-8") as res:
    for i in sorted(all_txt_files):
        for a in all_txt_files[i]:
            res.write(str(all_txt_files[a][0]))
                    #"\n", i"\n", all_txt_files[i][1])
with open ("result.txt", encoding="utf-8") as f:
    print(f.read())