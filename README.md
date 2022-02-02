# Airflow

## DAG:

In Airflow, a DAG – or a Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies.

### DAG Assignment:
A DAG can be set in three ways:
    
```dag = DAG('my_dag', start_date=datetime(2016, 1, 1))```

- sets the DAG explicitly
  - ```explicit_op = DummyOperator(task_id='op1', dag=dag)```


- deferred DAG assignment 
  - <code>deferred_op = DummyOperator(task_id='op2') 
  - deferred_op.dag = dag</code>


- inferred DAG assignment (linked operators must be in the same DAG)
  - <code>inferred_op = DummyOperator(task_id='op3')
  - inferred_op.set_upstream(deferred_op)</code>

## PythonOperator:
Is used in order to call an arbitrary Python function

- python_callable (python callable) – A reference to an object that is callable

- op_kwargs (dict (templated)) – a dictionary of keyword arguments that will get unpacked in your function

- op_args (list (templated)) – a list of positional arguments that will get unpacked when calling your callable

- provide_context (bool) – if set to true, Airflow will pass a set of keyword arguments that can be used in your function. This set of kwargs correspond exactly to what you can use in your jinja templates. For this to work, you need to define **kwargs in your function header.

- templates_dict (dict[str]) – a dictionary where the values are templates that will get templated by the Airflow engine sometime between __init__ and execute takes place and are made available in your callable’s context after the template has been applied. (templated)

- templates_exts (list[str]) – a list of file extensions to resolve while processing templated fields, for examples ['.sql', '.hql']