
  
# Creates a decorator to handle the database connection/cursor opening/closing.
# Creates the cursor with RealDictCursor, thus it returns real dictionaries, where the column names are the keys.
import os
import psycopg2
import psycopg2.extras


def get_connection_string():
    # to do this, please define these environment variables first
    # use only for testing
    user_name = os.getenv("DB_USER_NAME")
    database_name = os.getenv("DB_NAME")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")

    # default data if env variables are not defined
    if user_name is None or database_name is None or password is None or host is None:
        user_name = "postgres"
        database_name = "nicolas_backend"
        password = "asdf"
        host = "localhost"


    env_variables_defined = user_name and password and host and database_name

    if env_variables_defined:
        return 'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
    else:
        raise KeyError('Some necessary environment variable(s) are not defined')


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value

    return wrapper
def initdb_queries():
    return (
                ["""
                    CREATE TABLE IF NOT EXISTS items(
                        id VARCHAR UNIQUE NOT NULL,
                        name VARCHAR NOT NULL,
                        image_link VARCHAR NOT NULL,
                        description TEXT NOT NULL,
                        view_count INT NOT NULL
                    );
                """
                ]
            )

def initdb():
    try:
        connection = open_database()
        cursor = connection.cursor()
        for query in initdb_queries():
            cursor.execute(query)
        cursor.close()
            # commit the changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()