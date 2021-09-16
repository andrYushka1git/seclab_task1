#!/usr/bin/python3
from flask import Flask, request, request_started
import web
import sys
from cheroot import wsgi
import sqlite3

app = Flask(__name__)

@app.route('/users')
def get_users():# select id, login from users where status='active'
    f = open('init-db.sql', 'r');
    init_script = f.read()
    cursor = sqlite3.connect('task.db').cursor();
    cursor.executescript(init_script);
    try:
        cursor.execute("SELECT id, login FROM users WHERE status='active'");
        result = cursor.fetchall()
    except sqlite3.Error as e:
        return str(e);
    ret_value = ""
    for i in result:
        ret_value += str(i) + "\n";
    cursor.close();
    return ret_value;

@app.route('/by-login', methods=['GET'])
def by_login():#select * from users where login=$login
    f = open('init-db.sql', 'r');
    init_script = f.read()
    cursor = sqlite3.connect('task.db').cursor();
    cursor.executescript(init_script);
    login = request.args.get('login', '')
    try:
        cursor.execute("SELECT * FROM users WHERE login = '%s'"% login);
        result = cursor.fetchall()
    except sqlite3.Error as e:
        return str(e);
    ret_value = ""
    for i in result:
        ret_value += str(i) + "\n";
    cursor.close();
    return ret_value;


@app.route('/by-id', methods=['GET'])
def by_id():#select * from users where login=$login
    f = open('init-db.sql', 'r');
    init_script = f.read()
    cursor = sqlite3.connect('task.db').cursor();
    cursor.executescript(init_script);
    idd = request.args.get('id', '')
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s"% idd);
        result = cursor.fetchall()
    except OSError as e:
        return str(e);
    ret_value = ""
    for i in result:
        ret_value += str(i) + "\n";
    cursor.close();
    return ret_value

@app.errorhandler(500)
def internal_servererror(error):
    print (" [!]", error)
    return "Internal Server Error", 500


@app.route('/')
def common():
    req_data = """
    <html>
        <body>
        <a href="/users">active users</a>
        <a href="/by-login?login=admin">check admin</a>
        <a href="/by-id?id=3">check id=3</a>
        </body>
    </html>
    """;
    return req_data;

if __name__ == '__main__':
    print('Default port is 8888 and host is 0.0.0.0');
    port = 8888
    urls = ("/.*", "app")
    apps = web.application(urls, globals())
    server = wsgi.Server(("0.0.0.0", port), app, server_name='localhost')
    try:
        server.start()
	#apps.run(port)
    except KeyboardInterrupt:
        server.stop()
