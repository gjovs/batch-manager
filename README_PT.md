# 🗃️ Inserção em Lote no PostgreSQL com Multiprocessing

Este projeto implementa uma solução de inserção em lote no PostgreSQL usando Python com `multiprocessing.Pool` e `ThreadPoolExecutor`, oferecendo suporte para threads e processos paralelos. Ideal para manipulação de grandes volumes de dados, o projeto distribui a carga de trabalho entre múltiplas threads ou processos, o que reduz o tempo de inserção e melhora o desempenho.

## 🚀 Visão Geral

Manipular grandes volumes de dados pode ser uma tarefa desafiadora quando as inserções são feitas sequencialmente. Este projeto utiliza o módulo `concurrent.futures.ThreadPoolExecutor` e o `multiprocessing.Pool` para implementar inserções paralelas ou pseudo-paralelas no PostgreSQL.

## 🔧 Funcionalidades

- 📑 **Conexão com o PostgreSQL**: Configuração simples e flexível de parâmetros de conexão.
- ⚙️ **Execução Paralela**: Suporte para processos e threads via `multiprocessing.Pool` e `ThreadPoolExecutor`.
- 📦 **Inserções em Lote**: Divide os dados em lotes para minimizar o número de transações e otimizar o **desempenho**
