import json 
import logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s' )
def log_json(data):
    logging.debug(json.dumps(data, indent=4))

data = {
    "nama": "Farhan",
    "umur": 25,
    "hobi": ["coding", "membaca", "menulis"]
}

log_json(data)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def to_json(self):
        return {
            "name": self.name,
            "age": self.age
        }

person = Person("John Doe", 30)
log_json(person.to_json())
        