from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor
from typing import Callable


class MultiThreadManager:
  def __init__(self, num_threads: int = cpu_count() * 2, batch_size: int = 1000):
    self._num_threads = num_threads
    self._batch_size = batch_size


  def _slice_data(self, all_data: list[any], size: int | None) -> list[list[any]]:
    _size = size if size is not None else self._batch_size
    return [all_data[i:i + size] for i in range(0, len(all_data), _size)]
    
  def exec_in_batches(self, data: list, method: Callable):
        data_batches = self._slice_data(data, self._batch_size)

                
        with ThreadPoolExecutor(max_workers=self._num_threads) as thread_executor:  
          thread_executor.map(method, data_batches)