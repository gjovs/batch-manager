from time import perf_counter
from multiprocessing import cpu_count
from app.facade import create_people_facade
from app.infra.db.postgresql.database.challenge import PersonRepository
from app.usecases import DbCreatePerson
from app.infra.native.multiprocessing import MultiProcessManager
from app.infra.native.threads import MultiThreadManager

from app.util import generate_people_random_data

def main():
    num_records = 1000000
    print(f'Gerando {num_records} de seeds')

    total_records = generate_people_random_data(num_records)    

    start_time = perf_counter()

    print('Iniciando com MultiProcessManager')

    multi_process_manager = MultiProcessManager(cpu_count(), 100_000)

    multi_process_manager.exec_in_batches(total_records, create_people_facade)

    end_time = perf_counter()
    execution_time = end_time - start_time

    print(f"Tempo de execução: {execution_time} segundos via MultiProcessManager")

    ###

    start_time = perf_counter()

    print('Iniciando com MultiThreadManager')

    multi_process_manager = MultiThreadManager(cpu_count() * 4, 10_000)

    multi_process_manager.exec_in_batches(total_records, DbCreatePerson(PersonRepository().batch_insert).create_many)
    
    end_time = perf_counter()
    
    execution_time = end_time - start_time
    
    print(f"Tempo de execução: {execution_time} segundos via MultiThreadManager")
    
if __name__ == "__main__":
    main()
