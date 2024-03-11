# py-todo-list
>Simple project for Django Practice

## Technological stack

For this project i used:

>* python 3.11
>* django 5.0.3
>* crispy-bootstrap 2024.1
>* django-crispy-forms 2.1


## Installation instructions

For beginning you have to install Python3+ 

In terminal write down following commands:

```shell
git clone https://github.com/ArturPoltser/py-todo-list.git
python -m venv venv
venv\Scripts\activate  #for MacOS/Linux use: source vevn/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Also for testing you can load already prepared data:

```shell
python manage.py loaddata todo_list_db_data.json
