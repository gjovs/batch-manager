from app.domain.models import PersonDataModel
from typing import Callable

CreatePersonRepositoryType = Callable[[list[PersonDataModel]], None]

class DbCreatePerson:
  def __init__(self, createPersonRepository: CreatePersonRepositoryType):
    self._createPersonRepository = createPersonRepository
  
  def create_many(self, people: list[PersonDataModel]):
    return self._createPersonRepository(people)