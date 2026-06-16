"""
AI Skill Generator
Program untuk generate skill yang digunakan untuk AI dengan berbagai kategori dan level kesulitan
"""

import json
import random
from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Optional
from datetime import datetime


class SkillCategory(Enum):
    """Kategori skill untuk AI"""
    MACHINE_LEARNING = "machine_learning"
    DEEP_LEARNING = "deep_learning"
    NLP = "natural_language_processing"
    COMPUTER_VISION = "computer_vision"
    REINFORCEMENT_LEARNING = "reinforcement_learning"
    DATA_PROCESSING = "data_processing"
    OPTIMIZATION = "optimization"
    ROBOTICS = "robotics"


class DifficultyLevel(Enum):
    """Level kesulitan skill"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


@dataclass
class Skill:
    """Data class untuk skill AI"""
    id: str
    name: str
    description: str
    category: str
    difficulty: str
    required_knowledge: List[str]
    tools_frameworks: List[str]
    estimated_hours: int
    prerequisites: List[str]
    created_at: str

    def to_dict(self):
        """Convert skill ke dictionary"""
        return asdict(self)


class AISkillGenerator:
    """Generator untuk membuat skill AI"""

    def __init__(self):
        self.skills_data = {
            SkillCategory.MACHINE_LEARNING: [
                {
                    "name": "Supervised Learning",
                    "description": "Memahami dan mengimplementasikan algoritma supervised learning seperti linear regression, logistic regression, dan decision trees",
                    "required_knowledge": ["Linear Algebra", "Statistics", "Python"],
                    "tools_frameworks": ["scikit-learn", "TensorFlow", "PyTorch"],
                    "estimated_hours": 40,
                    "prerequisites": []
                },
                {
                    "name": "Unsupervised Learning",
                    "description": "Mempelajari clustering, dimensionality reduction, dan anomaly detection",
                    "required_knowledge": ["Statistics", "Linear Algebra", "Python"],
                    "tools_frameworks": ["scikit-learn", "Pandas"],
                    "estimated_hours": 35,
                    "prerequisites": ["Supervised Learning"]
                },
                {
                    "name": "Ensemble Methods",
                    "description": "Teknik menggabungkan multiple models seperti Random Forest, Gradient Boosting, Bagging",
                    "required_knowledge": ["Machine Learning", "Statistics"],
                    "tools_frameworks": ["scikit-learn", "XGBoost", "LightGBM"],
                    "estimated_hours": 45,
                    "prerequisites": ["Supervised Learning", "Unsupervised Learning"]
                }
            ],
            SkillCategory.DEEP_LEARNING: [
                {
                    "name": "Neural Networks Fundamentals",
                    "description": "Memahami konsep dasar neural networks, backpropagation, dan aktivasi functions",
                    "required_knowledge": ["Calculus", "Linear Algebra", "Python"],
                    "tools_frameworks": ["TensorFlow", "PyTorch", "Keras"],
                    "estimated_hours": 50,
                    "prerequisites": []
                },
                {
                    "name": "Convolutional Neural Networks",
                    "description": "Mempelajari CNN untuk image recognition dan computer vision tasks",
                    "required_knowledge": ["Neural Networks", "Mathematics"],
                    "tools_frameworks": ["TensorFlow", "PyTorch", "OpenCV"],
                    "estimated_hours": 45,
                    "prerequisites": ["Neural Networks Fundamentals"]
                },
                {
                    "name": "Recurrent Neural Networks",
                    "description": "Belajar RNN, LSTM, GRU untuk sequence modeling dan time series",
                    "required_knowledge": ["Neural Networks", "Sequential Data"],
                    "tools_frameworks": ["TensorFlow", "PyTorch"],
                    "estimated_hours": 40,
                    "prerequisites": ["Neural Networks Fundamentals"]
                },
                {
                    "name": "Transformers & Attention",
                    "description": "Memahami attention mechanisms dan transformer architecture",
                    "required_knowledge": ["Neural Networks", "NLP Basics"],
                    "tools_frameworks": ["Hugging Face", "PyTorch", "TensorFlow"],
                    "estimated_hours": 55,
                    "prerequisites": ["Recurrent Neural Networks"]
                }
            ],
            SkillCategory.NLP: [
                {
                    "name": "Text Preprocessing",
                    "description": "Teknik tokenization, lemmatization, stemming, dan text cleaning",
                    "required_knowledge": ["Python", "Regular Expressions"],
                    "tools_frameworks": ["NLTK", "spaCy", "Regex"],
                    "estimated_hours": 20,
                    "prerequisites": []
                },
                {
                    "name": "Word Embeddings",
                    "description": "Mempelajari Word2Vec, GloVe, FastText untuk word representations",
                    "required_knowledge": ["Linear Algebra", "Python"],
                    "tools_frameworks": ["Gensim", "spaCy", "Fasttext"],
                    "estimated_hours": 35,
                    "prerequisites": ["Text Preprocessing"]
                },
                {
                    "name": "Sentiment Analysis",
                    "description": "Build sentiment analysis models untuk klasifikasi sentimen text",
                    "required_knowledge": ["Machine Learning", "NLP Basics"],
                    "tools_frameworks": ["NLTK", "TextBlob", "Transformers"],
                    "estimated_hours": 30,
                    "prerequisites": ["Text Preprocessing", "Supervised Learning"]
                },
                {
                    "name": "Named Entity Recognition",
                    "description": "Implementasi NER untuk ekstraksi informasi dari text",
                    "required_knowledge": ["NLP", "Machine Learning"],
                    "tools_frameworks": ["spaCy", "NLTK", "Transformers"],
                    "estimated_hours": 35,
                    "prerequisites": ["Text Preprocessing"]
                }
            ],
            SkillCategory.COMPUTER_VISION: [
                {
                    "name": "Image Processing",
                    "description": "Teknik image filtering, edge detection, dan morphological operations",
                    "required_knowledge": ["Python", "Mathematics"],
                    "tools_frameworks": ["OpenCV", "PIL", "scikit-image"],
                    "estimated_hours": 30,
                    "prerequisites": []
                },
                {
                    "name": "Object Detection",
                    "description": "Implementasi YOLO, R-CNN, SSD untuk object detection",
                    "required_knowledge": ["Deep Learning", "CNNs"],
                    "tools_frameworks": ["Ultralytics YOLO", "TensorFlow Object Detection API"],
                    "estimated_hours": 50,
                    "prerequisites": ["Convolutional Neural Networks", "Image Processing"]
                },
                {
                    "name": "Image Segmentation",
                    "description": "Semantic dan instance segmentation dengan U-Net, Mask R-CNN",
                    "required_knowledge": ["Deep Learning", "CNNs"],
                    "tools_frameworks": ["TensorFlow", "PyTorch", "Detectron2"],
                    "estimated_hours": 45,
                    "prerequisites": ["Convolutional Neural Networks"]
                }
            ],
            SkillCategory.REINFORCEMENT_LEARNING: [
                {
                    "name": "RL Fundamentals",
                    "description": "Memahami Markov Decision Process, value functions, dan policies",
                    "required_knowledge": ["Probability", "Python"],
                    "tools_frameworks": ["Gym", "PyTorch"],
                    "estimated_hours": 40,
                    "prerequisites": []
                },
                {
                    "name": "Deep Q-Learning",
                    "description": "Implementasi DQN, Double DQN, Dueling DQN",
                    "required_knowledge": ["RL Fundamentals", "Deep Learning"],
                    "tools_frameworks": ["PyTorch", "Gym"],
                    "estimated_hours": 45,
                    "prerequisites": ["RL Fundamentals"]
                }
            ],
            SkillCategory.DATA_PROCESSING: [
                {
                    "name": "Data Cleaning & Wrangling",
                    "description": "Handle missing data, outliers, dan data transformation",
                    "required_knowledge": ["Python", "Statistics"],
                    "tools_frameworks": ["Pandas", "NumPy"],
                    "estimated_hours": 25,
                    "prerequisites": []
                },
                {
                    "name": "Feature Engineering",
                    "description": "Teknik membuat dan select features yang berkualitas",
                    "required_knowledge": ["Statistics", "Domain Knowledge"],
                    "tools_frameworks": ["Pandas", "scikit-learn"],
                    "estimated_hours": 35,
                    "prerequisites": ["Data Cleaning & Wrangling"]
                }
            ]
        }

    def generate_skill_id(self) -> str:
        """Generate unique skill ID"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_suffix = random.randint(1000, 9999)
        return f"SKILL_{timestamp}_{random_suffix}"

    def create_skill(
        self,
        name: str,
        description: str,
        category: SkillCategory,
        difficulty: DifficultyLevel,
        required_knowledge: List[str],
        tools_frameworks: List[str],
        estimated_hours: int,
        prerequisites: List[str] = None
    ) -> Skill:
        """Create skill dengan data yang diberikan"""
        if prerequisites is None:
            prerequisites = []

        skill = Skill(
            id=self.generate_skill_id(),
            name=name,
            description=description,
            category=category.value,
            difficulty=difficulty.value,
            required_knowledge=required_knowledge,
            tools_frameworks=tools_frameworks,
            estimated_hours=estimated_hours,
            prerequisites=prerequisites,
            created_at=datetime.now().isoformat()
        )
        return skill

    def generate_skills_by_category(
        self,
        category: SkillCategory,
        difficulty: Optional[DifficultyLevel] = None,
        count: Optional[int] = None
    ) -> List[Skill]:
        """Generate skills berdasarkan kategori"""
        if category not in self.skills_data:
            raise ValueError(f"Kategori {category} tidak ditemukan")

        skills_list = []
        category_data = self.skills_data[category]

        if count is None:
            count = len(category_data)

        selected_skills = random.sample(category_data, min(count, len(category_data)))

        for skill_data in selected_skills:
            skill = self.create_skill(
                name=skill_data["name"],
                description=skill_data["description"],
                category=category,
                difficulty=difficulty or random.choice(list(DifficultyLevel)),
                required_knowledge=skill_data["required_knowledge"],
                tools_frameworks=skill_data["tools_frameworks"],
                estimated_hours=skill_data["estimated_hours"],
                prerequisites=skill_data["prerequisites"]
            )
            skills_list.append(skill)

        return skills_list

    def generate_random_skills(self, count: int = 5) -> List[Skill]:
        """Generate random skills dari semua kategori"""
        skills_list = []
        categories = list(self.skills_data.keys())

        for _ in range(count):
            category = random.choice(categories)
            skills = self.generate_skills_by_category(
                category=category,
                count=1
            )
            skills_list.extend(skills)

        return skills_list

    def generate_learning_path(
        self,
        target_category: SkillCategory,
        start_difficulty: DifficultyLevel = DifficultyLevel.BEGINNER
    ) -> List[Skill]:
        """Generate learning path untuk mencapai target category"""
        if target_category not in self.skills_data:
            raise ValueError(f"Kategori {target_category} tidak ditemukan")

        learning_path = []
        category_data = self.skills_data[target_category]

        for skill_data in category_data:
            difficulty_levels = [DifficultyLevel.BEGINNER, DifficultyLevel.INTERMEDIATE,
                               DifficultyLevel.ADVANCED, DifficultyLevel.EXPERT]
            difficulty_index = difficulty_levels.index(start_difficulty)
            difficulty = difficulty_levels[min(difficulty_index + 1, len(difficulty_levels) - 1)]

            skill = self.create_skill(
                name=skill_data["name"],
                description=skill_data["description"],
                category=target_category,
                difficulty=difficulty,
                required_knowledge=skill_data["required_knowledge"],
                tools_frameworks=skill_data["tools_frameworks"],
                estimated_hours=skill_data["estimated_hours"],
                prerequisites=skill_data["prerequisites"]
            )
            learning_path.append(skill)

        return learning_path

    def export_skills_to_json(self, skills: List[Skill], filename: str) -> None:
        """Export skills ke JSON file"""
        skills_dict = [skill.to_dict() for skill in skills]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(skills_dict, f, indent=2, ensure_ascii=False)
        print(f"✓ Skills exported ke {filename}")

    def print_skill(self, skill: Skill) -> None:
        """Print skill details dengan format yang bagus"""
        print(f"\n{'='*60}")
        print(f"ID: {skill.id}")
        print(f"Nama: {skill.name}")
        print(f"Kategori: {skill.category}")
        print(f"Level Kesulitan: {skill.difficulty}")
        print(f"Deskripsi: {skill.description}")
        print(f"Pengetahuan Diperlukan: {', '.join(skill.required_knowledge)}")
        print(f"Tools/Framework: {', '.join(skill.tools_frameworks)}")
        print(f"Estimasi Jam: {skill.estimated_hours} jam")
        print(f"Prasyarat: {', '.join(skill.prerequisites) if skill.prerequisites else 'Tidak ada'}")
        print(f"Created At: {skill.created_at}")
        print(f"{'='*60}")

    def print_skills(self, skills: List[Skill]) -> None:
        """Print multiple skills"""
        print(f"\n\nTotal Skills: {len(skills)}\n")
        for skill in skills:
            self.print_skill(skill)


def main():
    """Main function untuk mendemonstrasikan penggunaan"""
    generator = AISkillGenerator()

    print("🤖 AI SKILL GENERATOR 🤖")
    print("=" * 60)

    # 1. Generate skills per kategori
    print("\n1. Generate Skills untuk Machine Learning:")
    ml_skills = generator.generate_skills_by_category(
        category=SkillCategory.MACHINE_LEARNING,
        difficulty=DifficultyLevel.BEGINNER
    )
    generator.print_skills(ml_skills)

    # 2. Generate skills untuk Deep Learning
    print("\n\n2. Generate Skills untuk Deep Learning:")
    dl_skills = generator.generate_skills_by_category(
        category=SkillCategory.DEEP_LEARNING,
        difficulty=DifficultyLevel.INTERMEDIATE,
        count=2
    )
    generator.print_skills(dl_skills)

    # 3. Generate random skills
    print("\n\n3. Generate 5 Random Skills dari berbagai kategori:")
    random_skills = generator.generate_random_skills(count=5)
    generator.print_skills(random_skills)

    # 4. Generate learning path
    print("\n\n4. Generate Learning Path untuk Natural Language Processing:")
    nlp_path = generator.generate_learning_path(
        target_category=SkillCategory.NLP,
        start_difficulty=DifficultyLevel.BEGINNER
    )
    generator.print_skills(nlp_path)

    # 5. Export ke JSON
    all_skills = ml_skills + dl_skills + random_skills + nlp_path
    generator.export_skills_to_json(all_skills, "ai_skills.json")

    # 6. Generate learning path untuk Computer Vision
    print("\n\n5. Generate Learning Path untuk Computer Vision:")
    cv_path = generator.generate_learning_path(
        target_category=SkillCategory.COMPUTER_VISION,
        start_difficulty=DifficultyLevel.BEGINNER
    )
    generator.print_skills(cv_path)
    generator.export_skills_to_json(cv_path, "cv_learning_path.json")


if __name__ == "__main__":
    main()
