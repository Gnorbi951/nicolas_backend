# Nicolas Cage Webshop backend

## Running

### Requirements
The use of virtual environment is recommended.
Install dependencies either from `setup.py` or requirements.txt.
Note: On windows machine `psycopg2-binary` might not work, use simply `psycopg2` instead.

#### Database:
You can set up your own parameters in `db/connection.py`.
With this `docker` command you can run the db with the default test values.
`docker run -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=asdf -e POSTGRES_DB=nicolas_backend -p 5432:5432 postgres`

### Scripts:

Run `main.py` to use start the webserver