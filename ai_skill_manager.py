"""
AI Skill Manager - Sistem untuk menambahkan dan mengelola skill AI
"""

from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import json


@dataclass
class AISkill:
    """Representasi skill AI"""
    name: str
    category: str
    level: int  # 1-5: Beginner, Intermediate, Advanced, Expert, Master
    description: str
    dependencies: List[str] = None
    created_at: str = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Konversi ke dictionary"""
        return asdict(self)


class AISkillManager:
    """Manager untuk mengelola skill AI"""
    
    def __init__(self, storage_file: str = "ai_skills.json"):
        self.storage_file = storage_file
        self.skills: Dict[str, AISkill] = {}
        self.load_skills()
    
    def add_skill(self, skill: AISkill) -> bool:
        """
        Tambahkan skill baru
        
        Args:
            skill: Object AISkill yang akan ditambahkan
            
        Returns:
            bool: True jika berhasil, False jika skill sudah ada
        """
        if skill.name in self.skills:
            print(f"⚠️  Skill '{skill.name}' sudah ada dalam database")
            return False
        
        self.skills[skill.name] = skill
        print(f"✅ Skill '{skill.name}' berhasil ditambahkan")
        self.save_skills()
        return True
    
    def remove_skill(self, skill_name: str) -> bool:
        """
        Hapus skill
        
        Args:
            skill_name: Nama skill yang akan dihapus
            
        Returns:
            bool: True jika berhasil, False jika skill tidak ditemukan
        """
        if skill_name not in self.skills:
            print(f"❌ Skill '{skill_name}' tidak ditemukan")
            return False
        
        del self.skills[skill_name]
        print(f"✅ Skill '{skill_name}' berhasil dihapus")
        self.save_skills()
        return True
    
    def update_skill(self, skill_name: str, **kwargs) -> bool:
        """
        Update skill yang ada
        
        Args:
            skill_name: Nama skill yang akan diupdate
            **kwargs: Field yang akan diupdate
            
        Returns:
            bool: True jika berhasil, False jika skill tidak ditemukan
        """
        if skill_name not in self.skills:
            print(f"❌ Skill '{skill_name}' tidak ditemukan")
            return False
        
        skill = self.skills[skill_name]
        for key, value in kwargs.items():
            if hasattr(skill, key):
                setattr(skill, key, value)
        
        print(f"✅ Skill '{skill_name}' berhasil diupdate")
        self.save_skills()
        return True
    
    def get_skill(self, skill_name: str) -> Optional[AISkill]:
        """
        Ambil skill berdasarkan nama
        
        Args:
            skill_name: Nama skill
            
        Returns:
            AISkill atau None jika tidak ditemukan
        """
        return self.skills.get(skill_name)
    
    def get_skills_by_category(self, category: str) -> List[AISkill]:
        """
        Ambil semua skill berdasarkan kategori
        
        Args:
            category: Nama kategori
            
        Returns:
            List skill dalam kategori tersebut
        """
        return [skill for skill in self.skills.values() if skill.category == category]
    
    def get_skills_by_level(self, level: int) -> List[AISkill]:
        """
        Ambil semua skill berdasarkan level
        
        Args:
            level: Level skill (1-5)
            
        Returns:
            List skill dengan level tersebut
        """
        return [skill for skill in self.skills.values() if skill.level == level]
    
    def list_all_skills(self) -> List[AISkill]:
        """
        Ambil semua skill
        
        Returns:
            List semua skill
        """
        return list(self.skills.values())
    
    def get_summary(self) -> Dict:
        """
        Dapatkan ringkasan skill
        
        Returns:
            Dictionary berisi summary
        """
        categories = {}
        levels = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        
        for skill in self.skills.values():
            # Count by category
            if skill.category not in categories:
                categories[skill.category] = 0
            categories[skill.category] += 1
            
            # Count by level
            levels[skill.level] += 1
        
        return {
            "total_skills": len(self.skills),
            "categories": categories,
            "levels": levels,
            "timestamp": datetime.now().isoformat()
        }
    
    def save_skills(self) -> bool:
        """
        Simpan semua skill ke file
        
        Returns:
            bool: True jika berhasil
        """
        try:
            data = {
                "skills": {name: skill.to_dict() for name, skill in self.skills.items()},
                "last_updated": datetime.now().isoformat()
            }
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"💾 Data berhasil disimpan ke {self.storage_file}")
            return True
        except Exception as e:
            print(f"❌ Error saat menyimpan data: {e}")
            return False
    
    def load_skills(self) -> bool:
        """
        Muat skill dari file
        
        Returns:
            bool: True jika berhasil
        """
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.skills = {}
            for name, skill_data in data.get("skills", {}).items():
                skill = AISkill(**skill_data)
                self.skills[name] = skill
            
            print(f"📂 Loaded {len(self.skills)} skills dari {self.storage_file}")
            return True
        except FileNotFoundError:
            print(f"ℹ️  File {self.storage_file} tidak ditemukan, membuat database baru")
            return False
        except Exception as e:
            print(f"❌ Error saat membaca data: {e}")
            return False
    
    def print_skills(self):
        """Print semua skill dalam format yang rapi"""
        if not self.skills:
            print("📭 Tidak ada skill dalam database")
            return
        
        print("\n" + "="*80)
        print("📊 DAFTAR AI SKILLS")
        print("="*80)
        
        for idx, skill in enumerate(self.skills.values(), 1):
            level_text = self._get_level_text(skill.level)
            print(f"\n{idx}. {skill.name}")
            print(f"   📁 Kategori: {skill.category}")
            print(f"   📈 Level: {level_text}")
            print(f"   📝 Deskripsi: {skill.description}")
            if skill.dependencies:
                print(f"   🔗 Dependencies: {', '.join(skill.dependencies)}")
            print(f"   ⏰ Ditambahkan: {skill.created_at}")
    
    @staticmethod
    def _get_level_text(level: int) -> str:
        """Konversi level ke teks"""
        levels = {
            1: "Beginner 🟢",
            2: "Intermediate 🟡",
            3: "Advanced 🟠",
            4: "Expert 🔴",
            5: "Master 👑"
        }
        return levels.get(level, "Unknown")


def main():
    """Main function - Contoh penggunaan"""
    manager = AISkillManager()
    
    # Tambahkan beberapa skill contoh
    skills_to_add = [
        AISkill(
            name="Natural Language Processing",
            category="Deep Learning",
            level=4,
            description="Pemrosesan bahasa alami menggunakan transformer dan neural networks"
        ),
        AISkill(
            name="Computer Vision",
            category="Deep Learning",
            level=3,
            description="Pengolahan citra menggunakan CNN dan model vision terkini",
            dependencies=["Neural Networks"]
        ),
        AISkill(
            name="Machine Learning",
            category="Core AI",
            level=3,
            description="Algoritma ML klasik seperti SVM, Random Forest, dan Clustering"
        ),
        AISkill(
            name="Neural Networks",
            category="Core AI",
            level=4,
            description="Arsitektur neural networks, backpropagation, dan optimization"
        ),
        AISkill(
            name="Reinforcement Learning",
            category="Advanced AI",
            level=2,
            description="Pembelajaran melalui reward, Q-learning, dan policy gradient"
        ),
        AISkill(
            name="Data Preprocessing",
            category="Data Science",
            level=5,
            description="Pembersihan data, feature engineering, dan normalisasi"
        ),
    ]
    
    # Tambahkan semua skill
    for skill in skills_to_add:
        manager.add_skill(skill)
    
    # Print semua skills
    manager.print_skills()
    
    # Print summary
    summary = manager.get_summary()
    print("\n" + "="*80)
    print("📈 SUMMARY")
    print("="*80)
    print(f"Total Skills: {summary['total_skills']}")
    print(f"\nSkills per Category:")
    for category, count in summary['categories'].items():
        print(f"  • {category}: {count}")
    print(f"\nSkills per Level:")
    level_names = {1: "Beginner", 2: "Intermediate", 3: "Advanced", 4: "Expert", 5: "Master"}
    for level, count in summary['levels'].items():
        if count > 0:
            print(f"  • {level_names[level]}: {count}")


if __name__ == "__main__":
    main()
