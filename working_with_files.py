import pprint as pprint

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