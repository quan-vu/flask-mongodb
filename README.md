# Flask and MongoDB practice

A sample for practice MongoDB in python Flask.

## Setup Database

We use mongodb as a docker container. 

**Step 1. Start MongoDB server with docker:**

    ```shell
    cd flask_mongodb
    docker-compose up
    ```

**Step 2. Connect to MongoDB server with mongo shell command:**

    ```shell
    mongo mongodb://myadmin:mypassword@localhost:27017/mytestdb
    ```

    Result

    ```
    MongoDB shell version v4.2.3
    connecting to: mongodb://localhost:27017/mytestdb?compressors=disabled&gssapiServiceName=mongodb
    Implicit session: session { "id" : UUID("8174edcb-ff3c-4b26-83f5-1d6bcc1f6b53") }
    MongoDB server version: 4.2.3   
    
    ```

    Create a collection:

    ```shell
    > db.createCollection('customers');
    # { "ok" : 1 }
    ```

    Show list of collections:

    ```shell
    > show collections;
    # customers
    ```

## Run project

**Step 1. Create virtualenv:**
    ```shell
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.in
    ```

**Step 2. Start project:**

    ```shell
    export FLASK_APP=app.py
    export FLASK_ENV=development
    python app.py
    ```

3. Result

    ```
    * Serving Flask app "app.py" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 522-870-215
    ```
