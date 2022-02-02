from airflow.models import DAG
from airflow.operators import python_operator
from datetime import datetime, timedelta

# Defining deafult arguments for DAG
default_dag_args = {
    'owner': 'prajual',
    'start_date': datetime(2022, 1, 28),
    'retry_delay': timedelta(minutes=5),
    'retries': 1
}

with DAG(
        'sample_test',
        schedule_interval="@once",
        default_args=default_dag_args) as dag:
    # Defining functions which will be called while running the DAG
    def greeting():
        import logging
        logging.info("Hi python")


    def greeting2(str):
        import logging
        logging.info(str)


    # Defining tasks through which the functions are called
    op1 = python_operator.PythonOperator(task_id='greet1',
                                         dag=dag,
                                         python_callable=greeting)
    op2 = python_operator.PythonOperator(task_id='greet2',
                                         dag=dag,
                                         op_kwargs={'str':'Bye Python'},
                                         python_callable=greeting2)

    # Defining the order in which the tasks will be run
    op1 >> op2
