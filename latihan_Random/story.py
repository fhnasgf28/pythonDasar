"""
Story dengan konsep OOP
Membuat sistem cerita interaktif dengan karakter, alur cerita, dan pilihan
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class Character:
    """Kelas untuk merepresentasikan karakter dalam cerita"""
    
    def __init__(self, name: str, role: str, health: int = 100):
        self.name = name
        self.role = role
        self.health = health
        self.inventory: List[str] = []
    
    def take_damage(self, damage: int):
        """Karakter menerima damage"""
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount: int):
        """Karakter sembuh"""
        self.health = min(self.health + amount, 100)
    
    def add_item(self, item: str):
        """Tambah item ke inventory"""
        self.inventory.append(item)
    
    def remove_item(self, item: str):
        """Hapus item dari inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
    
    def display_info(self):
        """Tampilkan informasi karakter"""
        print(f"\n{'='*50}")
        print(f"Nama: {self.name}")
        print(f"Peran: {self.role}")
        print(f"Kesehatan: {self.health}%")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Kosong'}")
        print(f"{'='*50}\n")


class Scene(ABC):
    """Kelas abstrak untuk scene dalam cerita"""
    
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.choices: Dict[int, tuple] = {}
    
    @abstractmethod
    def execute(self, character: Character):
        """Jalankan scene ini"""
        pass
    
    def add_choice(self, choice_num: int, text: str, next_scene: Optional['Scene'] = None):
        """Tambah pilihan untuk scene ini"""
        self.choices[choice_num] = (text, next_scene)
    
    def display(self):
        """Tampilkan scene"""
        print(f"\n{'='*60}")
        print(f"📖 {self.title}")
        print(f"{'='*60}")
        print(f"\n{self.description}\n")
        
        if self.choices:
            print("Pilihan:")
            for num, (text, _) in sorted(self.choices.items()):
                print(f"  {num}. {text}")


class NormalScene(Scene):
    """Scene normal yang hanya menceritakan"""
    
    def execute(self, character: Character):
        self.display()
        if self.choices:
            choice = int(input("\nPilihan Anda: "))
            return self.choices.get(choice, (None, None))[1]
        return None


class BattleScene(Scene):
    """Scene pertarungan dengan musuh"""
    
    def __init__(self, title: str, description: str, enemy_name: str, enemy_damage: int):
        super().__init__(title, description)
        self.enemy_name = enemy_name
        self.enemy_damage = enemy_damage
        self.enemy_health = 50
    
    def execute(self, character: Character):
        self.display()
        print(f"\n⚔️  MUSUH: {self.enemy_name} (HP: {self.enemy_health})\n")
        
        while self.enemy_health > 0 and character.health > 0:
            action = input("Pilihan: [1]Serang [2]Bertahan [3]Lari\n> ")
            
            if action == "1":
                damage = 30
                self.enemy_health -= damage
                print(f"\n✅ Anda menyerang musuh dengan damage {damage}!")
                
                if self.enemy_health > 0:
                    character.take_damage(self.enemy_damage)
                    print(f"❌ {self.enemy_name} menyerang balik dengan damage {self.enemy_damage}!")
                    print(f"HP Anda: {character.health}%\n")
            
            elif action == "2":
                reduced_damage = self.enemy_damage // 2
                character.take_damage(reduced_damage)
                print(f"\n🛡️  Anda bertahan! Damage berkurang menjadi {reduced_damage}!")
                print(f"HP Anda: {character.health}%\n")
            
            elif action == "3":
                print("\n🏃 Anda berhasil melarikan diri!")
                return None
        
        if character.health > 0:
            print(f"\n🎉 Anda memenangkan pertarungan! {self.enemy_name} telah dikalahkan!")
            character.add_item("Pedang Legendaris")
            choice = int(input("\nLanjutkan ke scene berikutnya? [1]Ya [2]Tidak\n> "))
            if choice == 1:
                return self.choices.get(1, (None, None))[1]
        else:
            print(f"\n💀 Anda telah dikalahkan oleh {self.enemy_name}... Game Over!")
            return None


class Story:
    """Kelas utama untuk menjalankan cerita"""
    
    def __init__(self, title: str, protagonist_name: str):
        self.title = title
        self.protagonist = Character(name=protagonist_name, role="Petualang", health=100)
        self.current_scene: Optional[Scene] = None
        self.scenes: Dict[str, Scene] = {}
    
    def add_scene(self, scene_name: str, scene: Scene):
        """Tambah scene ke cerita"""
        self.scenes[scene_name] = scene
    
    def start(self, scene_name: str):
        """Mulai cerita dari scene tertentu"""
        print(f"\n{'*'*60}")
        print(f"🎬 {self.title}")
        print(f"{'*'*60}")
        print(f"Tokoh Utama: {self.protagonist.name}\n")
        
        self.current_scene = self.scenes.get(scene_name)
        
        while self.current_scene:
            self.current_scene.execute(self.protagonist)
            next_scene_name = self.current_scene.choices.get(
                int(input("\nPilihan Anda: ")) if self.current_scene.choices else 1
            )
            
            if next_scene_name and isinstance(next_scene_name, tuple):
                self.current_scene = next_scene_name[1]
            else:
                break
        
        self.show_ending()
    
    def show_ending(self):
        """Tampilkan ending cerita"""
        print(f"\n{'='*60}")
        print("🏁 CERITA BERAKHIR")
        print(f"{'='*60}")
        self.protagonist.display_info()


# ==================== CONTOH PENGGUNAAN ====================

def main():
    """Fungsi utama untuk menjalankan contoh cerita"""
    
    # Buat cerita
    story = Story("Petualangan di Hutan Mistis", "Anda")
    
    # Buat scene-scene
    scene_intro = NormalScene(
        title="Pengenalan",
        description="""Anda adalah seorang petualang yang berani. Setelah mendengar 
cerita tentang harta karun tersembunyi di Hutan Mistis, Anda memutuskan 
untuk mencarinya. Perjalanan dimulai di tepi hutan yang gelap dan 
misterius."""
    )
    
    scene_fork = NormalScene(
        title="Persimpangan Jalan",
        description="""Setelah berjalan sebentar, Anda menemukan persimpangan jalan. 
Ada dua jalur di depan Anda:
- Jalur kiri mengarah ke dalam lebih dalam
- Jalur kanan mengarah ke desa tua yang sudah ditinggal"""
    )
    
    scene_battle = BattleScene(
        title="Pertarungan dengan Makhluk Gelap",
        description="""Tiba-tiba, Anda melihat bayangan hitam bergerak cepat! 
Makhluk gelap muncul dan menghalangi jalan Anda!""",
        enemy_name="Makhluk Gelap",
        enemy_damage=20
    )
    
    scene_treasure = NormalScene(
        title="Harta Karun Ditemukan",
        description="""Setelah mengalahkan makhluk gelap, Anda melanjutkan perjalanan 
dan akhirnya menemukan gua rahasia. Di dalam gua tersebut, ada 
harta karun yang bersinar! Anda telah berhasil menyelesaikan misi!""")
    
    # Hubungkan scene-scene
    scene_intro.add_choice(1, "Mulai petualangan", scene_fork)
    
    scene_fork.add_choice(1, "Ambil jalur kiri (lebih dalam)", scene_battle)
    scene_fork.add_choice(2, "Ambil jalur kanan (desa tua)", scene_treasure)
    
    scene_battle.add_choice(1, "Lanjut ke harta karun", scene_treasure)
    
    # Tambahkan scene ke story
    story.add_scene("intro", scene_intro)
    story.add_scene("fork", scene_fork)
    story.add_scene("battle", scene_battle)
    story.add_scene("treasure", scene_treasure)
    
    # Mulai cerita
    story.start("intro")


if __name__ == "__main__":
    main()
