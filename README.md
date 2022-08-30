# HR SYSTEM
Welcome to Equevo HR system. This is a guide on how to install and run the project.

## Installation and configuration

Enviornment:
- Make sure you have python 3.10 on your installed on your machine.
  
- Create a virtual environment in the project root directory with the following command :
  ```shell 
  python3.10 -m venv <your_env_name>
  ```

- On Linux OS activate the virtual environment :
  ```shell 
  source ./<your_env_name>/bin/activate
  ``` 
    Make sure the environment is activated.
  
- install project requirements:
  ```shell
  pip install -r requirements.txt
  ```
  
- Make sure you have postgres 12 on your machine, if not follow this guide to install it and set up the db [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04) .

- create `.env` file in [equevo project directory](equevo) the open  [.env.sample](equevo/.env.sample) and copy it's content in the created .env file. provide the needed information such as: SECRET_KEY, Database and AWS S3 configs.

- Once the above step is done, run makemigrations and migrate as following:
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

- Create super user:
  ```shell
  python manage.py createsuperuser --username <your_admin_ username> --email <your-admin@user.email>
  ```
  follow the prompt after to set up your password.

- run the project :
    ```shell
    python manage.py runserver
    ```
- For API docs, see it [here](docs/API-DOCS.md).

## Frontend part:
- cd into [frontend](./frontend).
- install dependencies : 
    ```shell
    npm -i
    ```
- Run the project:
    ```shell
    npm start
    ```