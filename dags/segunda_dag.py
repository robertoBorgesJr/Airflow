from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('Segunda_dag', description='Segunda DAG',
          schedule_interval=None, start_date=datetime(2023,3,5),
          catchup=False)

task1 = BashOperator(task_id='tsk1',bash_command="sleep 5",dag=dag)
task2 = BashOperator(task_id='tsk2',bash_command="sleep 5",dag=dag)
task3 = BashOperator(task_id='tsk3',bash_command="sleep 5",dag=dag)

task1 >> [task2, task3] # vai rodar primeiro a 1 e posteriormente as 2 outras em paralelo