from airflow import DAG
from airflow import Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

dag = DAG('Producer', description='Producer',
          schedule_interval=None, start_date=datetime(2023,3,5),
          catchup=False)

myDataset = Dataset('/opt/airflow/data/Churn_new.csv')

def my_file():
    dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
    dataset.to_csv('/opt/airflow/data/Churn_new.csv', sep=';')

t1 = PythonOperator(task_id='t1', python_callable=my_file, dag=dag, outlets=[myDataset])    
t1