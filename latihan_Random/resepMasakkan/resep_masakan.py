from typing import List, Dict
import json 

class Ingredient:
    def __init__(self, name: str, quantity: str):
        self.name = name
        self.quantity = quantity

    
    def __repr__(self):
        return f"{self.quantity} {self.name}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity
        }
    
class Recipe:
    def __init__(self, name: str, ingridients: list[Ingredient], instructions: str):
        self.name = name 
        self.ingridients = ingridients
        self.instructions = instructions

    def __repr__(self):
        return f"Recipe(name={self.name}, ingridients={self.ingridients}, instructions={self.instructions})"
    
    def to_dict(self):
        return {
            'name': self.name,
            'ingridients': [ingredient.to_dict() for ingredient in self.ingridients],
            'instructions': self.instructions
        }

class RecipeManager:
    def __init__(self):
        self.recipes: List[Recipe] = []

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)
        print(f"Recipe '{recipe.name}' added successfully.")

    def list_recipes(self):
        if not self.recipes:
            print("No recipes available")
            return
        for idx, r in enumerate(self.recipes, 1):
            print(f"{idx}. {r.name}")
    
    def generate_shopping_list(self, selected_indices: List[int]) -> Dict[str, str]:
        shopping_list = {}
        for idx in selected_indices:
            if 0 <= idx < len(self.recipes):
                for ingredient in self.recipes[idx].ingridients:
                    if ingredient.name in shopping_list:
                        shopping_list[ingredient.name] += f", {ingredient.quantity}"
                    else:
                        shopping_list[ingredient.name] = ingredient.quantity
                        print(f'shopping_list:{shopping_list[ingredient.name]}')
        return shopping_list
    
    def save_to_file(self, filename= "recipes.json"):
        with open(filename, 'w') as file:
            json.dump([recipe.to_dict() for recipe in self.recipes], file, indent=4)
        print(f"Recipes saved to {filename}")
        