#!/usr/bin/env python3
from flask import Flask
from router.router import main_router
from db.connection import initdb

app = Flask(__name__)
app.register_blueprint(main_router)

if __name__ == '__main__':
    initdb()
    app.run(
        debug=False,
        host='127.0.0.1',
        port=8080
    )
