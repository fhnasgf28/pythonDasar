"""
AI Skill Management System
A Python module for adding and managing skills in an AI system.
"""

from typing import Dict, List, Callable, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import json


@dataclass
class Skill:
    """Represents an AI skill with metadata and execution logic."""
    name: str
    description: str
    category: str
    execute: Callable
    parameters: Dict[str, Any]
    version: str = "1.0.0"
    created_at: datetime = None
    enabled: bool = True

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def __call__(self, *args, **kwargs):
        """Execute the skill."""
        if not self.enabled:
            raise RuntimeError(f"Skill '{self.name}' is disabled.")
        return self.execute(*args, **kwargs)


class AISkillManager:
    """Manages AI skills - add, remove, execute, and list them."""

    def __init__(self):
        self.skills: Dict[str, Skill] = {}

    def add_skill(self, skill: Skill) -> None:
        """Add a new skill to the AI."""
        if skill.name in self.skills:
            raise ValueError(f"Skill '{skill.name}' already exists.")
        self.skills[skill.name] = skill
        print(f"✓ Skill '{skill.name}' added successfully.")

    def remove_skill(self, skill_name: str) -> None:
        """Remove a skill from the AI."""
        if skill_name not in self.skills:
            raise ValueError(f"Skill '{skill_name}' not found.")
        del self.skills[skill_name]
        print(f"✓ Skill '{skill_name}' removed successfully.")

    def enable_skill(self, skill_name: str) -> None:
        """Enable a skill."""
        if skill_name not in self.skills:
            raise ValueError(f"Skill '{skill_name}' not found.")
        self.skills[skill_name].enabled = True
        print(f"✓ Skill '{skill_name}' enabled.")

    def disable_skill(self, skill_name: str) -> None:
        """Disable a skill."""
        if skill_name not in self.skills:
            raise ValueError(f"Skill '{skill_name}' not found.")
        self.skills[skill_name].enabled = False
        print(f"✓ Skill '{skill_name}' disabled.")

    def execute_skill(self, skill_name: str, *args, **kwargs) -> Any:
        """Execute a specific skill."""
        if skill_name not in self.skills:
            raise ValueError(f"Skill '{skill_name}' not found.")
        skill = self.skills[skill_name]
        print(f"→ Executing skill: {skill_name}")
        return skill(*args, **kwargs)

    def list_skills(self) -> List[Dict[str, Any]]:
        """List all available skills."""
        skills_list = []
        for name, skill in self.skills.items():
            skills_list.append({
                "name": name,
                "description": skill.description,
                "category": skill.category,
                "version": skill.version,
                "enabled": skill.enabled,
                "created_at": skill.created_at.isoformat()
            })
        return skills_list

    def get_skill(self, skill_name: str) -> Optional[Skill]:
        """Get a specific skill."""
        return self.skills.get(skill_name)

    def print_skills_info(self) -> None:
        """Print formatted information about all skills."""
        if not self.skills:
            print("No skills available.")
            return
        print("\n" + "="*60)
        print("AVAILABLE SKILLS")
        print("="*60)
        for i, (name, skill) in enumerate(self.skills.items(), 1):
            status = "✓ ENABLED" if skill.enabled else "✗ DISABLED"
            print(f"\n{i}. {name} [{status}]")
            print(f"   Description: {skill.description}")
            print(f"   Category: {skill.category}")
            print(f"   Version: {skill.version}")
            print(f"   Created: {skill.created_at.strftime('%Y-%m-%d %H:%M:%S')}")


# Example Skills Implementation

class AI:
    """Simple AI class that uses the skill manager."""

    def __init__(self):
        self.skill_manager = AISkillManager()
        self._setup_default_skills()

    def _setup_default_skills(self):
        """Setup default skills for the AI."""

        # Skill 1: Math operations
        def math_skill(operation: str, num1: float, num2: float) -> float:
            operations = {
                'add': lambda a, b: a + b,
                'subtract': lambda a, b: a - b,
                'multiply': lambda a, b: a * b,
                'divide': lambda a, b: a / b if b != 0 else None,
            }
            result = operations.get(operation, lambda a, b: None)(num1, num2)
            print(f"   {num1} {operation} {num2} = {result}")
            return result

        # Skill 2: Text processing
        def text_skill(text: str, operation: str) -> str:
            operations = {
                'uppercase': text.upper(),
                'lowercase': text.lower(),
                'reverse': text[::-1],
                'capitalize': text.capitalize(),
            }
            result = operations.get(operation, text)
            print(f"   Text after '{operation}': {result}")
            return result

        # Skill 3: Language translation (mock)
        def translate_skill(text: str, target_lang: str) -> str:
            translations = {
                'es': 'Hola',
                'fr': 'Bonjour',
                'de': 'Hallo',
                'it': 'Ciao',
            }
            result = translations.get(target_lang, text)
            print(f"   Translation to {target_lang}: {result}")
            return result

        # Skill 4: Data analysis
        def analyze_skill(data: List[float]) -> Dict[str, float]:
            if not data:
                return {}
            analysis = {
                'mean': sum(data) / len(data),
                'max': max(data),
                'min': min(data),
                'sum': sum(data),
            }
            print(f"   Data analysis: {analysis}")
            return analysis

        # Add skills to AI
        self.skill_manager.add_skill(Skill(
            name="math",
            description="Perform mathematical operations",
            category="computation",
            execute=math_skill,
            parameters={"operation": str, "num1": float, "num2": float}
        ))

        self.skill_manager.add_skill(Skill(
            name="text_processing",
            description="Process and transform text",
            category="text",
            execute=text_skill,
            parameters={"text": str, "operation": str}
        ))

        self.skill_manager.add_skill(Skill(
            name="translate",
            description="Translate text to different languages",
            category="language",
            execute=translate_skill,
            parameters={"text": str, "target_lang": str}
        ))

        self.skill_manager.add_skill(Skill(
            name="analyze_data",
            description="Analyze numerical data",
            category="analysis",
            execute=analyze_skill,
            parameters={"data": list}
        ))

    def use_skill(self, skill_name: str, *args, **kwargs):
        """Use a skill by name."""
        return self.skill_manager.execute_skill(skill_name, *args, **kwargs)

    def show_skills(self):
        """Show all available skills."""
        self.skill_manager.print_skills_info()


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    # Create AI instance
    ai = AI()

    print("\n🤖 AI SKILL SYSTEM DEMO\n")

    # Show available skills
    ai.show_skills()

    print("\n" + "="*60)
    print("USING SKILLS")
    print("="*60)

    # Use math skill
    print("\n1️⃣  Math Skill:")
    ai.use_skill("math", "add", 10, 5)
    ai.use_skill("math", "multiply", 3, 7)

    # Use text processing skill
    print("\n2️⃣  Text Processing Skill:")
    ai.use_skill("text_processing", "Hello World", "uppercase")
    ai.use_skill("text_processing", "Hello World", "reverse")

    # Use translation skill
    print("\n3️⃣  Translation Skill:")
    ai.use_skill("translate", "Hello", "es")
    ai.use_skill("translate", "Hello", "fr")

    # Use data analysis skill
    print("\n4️⃣  Data Analysis Skill:")
    ai.use_skill("analyze_data", [1, 2, 3, 4, 5, 10, 20])

    # Disable a skill
    print("\n" + "="*60)
    print("MANAGING SKILLS")
    print("="*60)
    ai.skill_manager.disable_skill("math")

    # Try to use disabled skill
    print("\nTrying to use disabled skill:")
    try:
        ai.use_skill("math", "add", 2, 3)
    except RuntimeError as e:
        print(f"   ✗ Error: {e}")

    # Re-enable and use
    ai.skill_manager.enable_skill("math")
    print("\nAfter re-enabling:")
    ai.use_skill("math", "add", 2, 3)

    # Export skills as JSON
    print("\n" + "="*60)
    print("SKILL EXPORT")
    print("="*60)
    skills_data = ai.skill_manager.list_skills()
    print(json.dumps(skills_data, indent=2))
