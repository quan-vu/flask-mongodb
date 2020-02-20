# Flask and MongoDB practice

A sample for practice MongoDB in python Flask.

## Setup Database

1. Start MongoDB server with docker:

    ```shell
    docker run -d -p 27017:27017 --name mongodb mongo
    ```

2. Create MongoDB: **mytest**

3. Import sample data: data/users.json

    ```
    mytest
        |_ users
    ```

## Run project

1. Create virtualenv:

    ```shell
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.in
    ```

2. Start project:

    ```shell
    export FLASK_APP=app.py
    export FLASK_ENV=development
    python app.py
    ```

3. Resutl

    ```
    * Serving Flask app "app.py" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 522-870-215
    ```
