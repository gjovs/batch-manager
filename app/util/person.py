import random
import string
from app.domain.models import PersonDataModel

def generate_people_random_data(num_records: int) -> list[PersonDataModel]:
    people_data = []
    for _ in range(num_records):
        name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
        
        age = random.randint(18, 80)
        
        person = PersonDataModel(name=name, age=age)
        people_data.append(person)
    
    return people_data
