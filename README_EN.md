# 🗃️ Batch Insertion in PostgreSQL with Multiprocessing

This project implements a batch insertion solution in PostgreSQL using Python with `multiprocessing.Pool` and `ThreadPoolExecutor`, providing support for parallel threads and processes. Ideal for handling large volumes of data, the project distributes the workload across multiple threads or processes, reducing insertion time and improving performance.

## 🚀 Overview

Handling large volumes of data can be challenging when insertions are performed sequentially. This project uses the `concurrent.futures.ThreadPoolExecutor` and `multiprocessing.Pool` modules to implement parallel or pseudo-parallel batch insertions in PostgreSQL.

## 🔧 Features

- 📑 **PostgreSQL Connection**: Simple and flexible configuration of connection parameters.
- ⚙️ **Parallel Execution**: Support for both processes and threads via `multiprocessing.Pool` and `ThreadPoolExecutor`.
- 📦 **Batch Insertions**: Divides data into batches to minimize the number of transactions and optimize performance.
