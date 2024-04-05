import requests

# Функция для получения случайного рецепта
def get_random_recipe():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        recipe = json_data["meals"][0]
        return recipe
    else:
        print("Ошибка при получении случайного рецепта")
        return None

# Функция для получения списка блюд из категории
def get_category_recipes(category):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        recipes = [meal["strMeal"] for meal in json_data["meals"]]
        return recipes
    else:
        print("Ошибка при получении списка блюд из категории")
        return None

# Функция для проверки наличия масла в ингредиентах рецепта
def check_for_butter(recipe_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        recipe = json_data["meals"][0]
        ingredients = [value for key, value in recipe.items() if key.startswith("strIngredient") and value is not None]
        if "Butter" in ingredients:
            return True
        else:
            return False
    else:
        print("Ошибка при получении информации о рецепте")
        return None

# Получаем 3 случайных рецепта
recipes = [get_random_recipe() for _ in range(3)]

# Выводим информацию о каждом рецепте
for recipe in recipes:
    category = recipe["strCategory"]
    print(f"Категория: {category}")
    
    # Получаем список блюд из категории
    category_recipes = get_category_recipes(category)
    if category_recipes:
        print("Блюда из категории:")
        for recipe in category_recipes:
            print(recipe)
        
        # Получаем ID рецепта для проверки наличия масла
        recipe_id = recipe["idMeal"]
        
        # Проверяем наличие масла в рецепте
        has_butter = check_for_butter(recipe_id)
        if has_butter is not None:
            if has_butter:
                print("В этой категории есть блюда с маслом")
            else:
                print("В этой категории нет блюд с маслом")
    print("----------------------------------------")
