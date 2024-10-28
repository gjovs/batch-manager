from app.usecases import DbCreatePerson
from app.infra.db.postgresql.database.challenge import PersonRepository

def create_people_facade(batch):
  DbCreatePerson(PersonRepository().batch_insert).create_many(batch)
