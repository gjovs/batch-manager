from multiprocessing import Pool, cpu_count
from typing import Callable


class MultiProcessManager:
  def __init__(self, num_processes: int = cpu_count(), batch_size: int = 1000):
    self._num_processes = num_processes
    self._batch_size = batch_size


  def _slice_data(self, all_data: list[any], size: int | None) -> list[list[any]]:
    _size = size if size is not None else self._batch_size
    return [all_data[i:i + size] for i in range(0, len(all_data), _size)]
    
  def exec_in_batches(self, data: list, method: Callable):
        data_batches = self._slice_data(data, self._batch_size)
                
        with Pool(processes=self._num_processes) as pool:
            pool.map(method, data_batches)

        print('Finish batch insert process')