from app.infra.db.postgresql.util import Repository
from app.domain.models import PersonDataModel
from typing import Callable


class PersonRepository(Repository):
    def __init__(self):
        super().__init__()

    def batch_insert(self, persons: list[PersonDataModel]):
        query = "INSERT INTO people (name, age) VALUES "
        values = ', '.join(["(%s, %s)"] * len(persons))
        query = query + values + ";"
        
        person_values = []
        for person in persons:
            person_values.extend([person.name, person.age])

            
        with self.connection.cursor() as cursor:
            cursor.execute(query, person_values)  
            self.connection.commit()


        self.connection.close()