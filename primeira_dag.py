from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator


with DAG(
    dag_id="primeira_dag",
    start_date=datetime(2024, 10, 18),
    schedule_interval="@daily",
    doc_md=__doc__,
    catchup=False
) as dag:
    inicia = DummyOperator(task_id="inicia")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    finaliza = DummyOperator(task_id="finaliza")

(inicia >> hello >> finaliza)