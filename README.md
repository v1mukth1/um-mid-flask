# um-mid-flask-assignment.v1.00
Clone the git repository and move to the working directory. On the terminal execute the below command to create the projects.
```bash
$ git clone https://github.com/v1mukth1/um-mid-flask.git
$ cd um-mid-flask

```
In the projects' working directory execute the below command to download the dependencies.

```bash

$ pip install flask flask-mongoengine

```

Execute the below command to run the project
```bash
$ flask run
```

Use the below command to import books.json to mongodb

```bash
$ mongoimport --db shakir --collection books --file books.json --jsonArray
```
