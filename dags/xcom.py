from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag = DAG('Exemplo_xcom', description='xcom',
          schedule_interval=None, start_date=datetime(2023,3,5),
          catchup=False)

def task_write(**kwarg): 
    kwarg['ti'].xcom_push(key='valorXcom1', value=10200)

task1 = PythonOperator(task_id='tsk1', python_callable=task_write,dag=dag)

def task_read(**kwarg):
    valor = kwarg['ti'].xcom_pull(key='valorXcom1')
    print(f"valor recuperado: {valor}")

task2 = PythonOperator(task_id='tsk2', python_callable=task_read,dag=dag)

task1 >> task2
