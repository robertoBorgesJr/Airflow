from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


dag = DAG('Pool', description='pool',
          schedule_interval=None, start_date=datetime(2023,3,5),
          catchup=False)


task1 = BashOperator(task_id='tsk1',bash_command="sleep 5", dag=dag, pool='meuPool')
task2 = BashOperator(task_id='tsk2',bash_command="sleep 5", dag=dag, pool='meuPool', priority_weight=5)
task3 = BashOperator(task_id='tsk3',bash_command="sleep 5", dag=dag, pool='meuPool')
task4 = BashOperator(task_id='tsk4',bash_command="sleep 5", dag=dag, pool='meuPool', priority_weight=10)

# conclusão: apesar do paralelismo, como o pool tem 1 slot, a execução é feita 1 task por vez
# quanto maior a priority_weight, maior é a prioridade

