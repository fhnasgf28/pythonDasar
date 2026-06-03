
## 3. **Generator Dinamis dari Dictionary**

```python name=dynamic_md_generator.py
"""
Dynamic Markdown Generator from Dictionary
"""
import json

def generate_from_dict(data, filename="output.md"):
    """Generate Markdown from dictionary structure"""
    content = ""
    
    for key, value in data.items():
        if key == "title":
            content += f"# {value}\n\n"
        elif key == "sections":
            for section in value:
                content += f"## {section['name']}\n\n"
                content += f"{section['content']}\n\n"
        elif key == "items":
            content += "- " + "\n- ".join(value) + "\n\n"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return content


# Usage
data = {
    "title": "Project Documentation",
    "sections": [
        {
            "name": "Introduction",
            "content": "This is the introduction section."
        },
        {
            "name": "Getting Started",
            "content": "Follow these steps to get started."
        }
    ],
    "items": ["Item 1", "Item 2", "Item 3"]
}

result = generate_from_dict(data, "doc.md")
print(result)
