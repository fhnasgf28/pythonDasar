from resep_masakan import Ingredient, Recipe, RecipeManager

def input_ingredient():
    ingredients = []
    while True:
        name = input("Nama bahan (kosongkan untuk selesai): ")
        if not name:
            break
        quantity = input("Jumlah bahan: ")
        ingredients.append(Ingredient(name, quantity))
    return ingredients

def main():
    manager = RecipeManager()
    while True:
        print("\nMenu:")
        print("1. Tambah Resep")
        print("2. Lihat Resep")
        print("3. Buat Daftar Belanja")
        print("4. Keluar")
        
        choice = input("Pilih opsi (1-4): ")
        
        if choice == '1':
            name = input("Nama resep: ")
            ingredients = input_ingredient()
            instructions = input("Instruksi memasak: ")
            recipe = Recipe(name, ingredients, instructions)
            manager.add_recipe(recipe)
        
        elif choice == '2':
            manager.list_recipes()
        
        elif choice == '3':
            indices = input("Masukkan nomor resep yang ingin dibuat daftar belanja (pisahkan dengan koma): ")
            selected_indices = [int(i.strip()) - 1 for i in indices.split(',')]
            shopping_list = manager.generate_shopping_list(selected_indices)
            print("\nDaftar Belanja:")
            for item, quantity in shopping_list.items():
                print(f"{item}: {quantity}")
        
        elif choice == '4':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
if __name__ == "__main__":
    main()