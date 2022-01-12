from flask import Flask, render_template, request, jsonify
import requests
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'


@app.route('/assignment11/users')
def assignment11_users_func():
    query = ' select * from users;'
    users = interact_db(query=query, query_type='fetch')
    response = jsonify(users)
    return response


def get_user(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res

@app.route('/')
@app.route('/assignment11/outer_source')
def assignment11_outer_source_func():
    num = 1
    if "number_backend" in request.args:
        num = int(request.args['number_backend'])
        user = get_user(num)
        return render_template('assignment11_outerSource.html', User=user)
    return render_template('assignment11_outerSource.html')


if __name__ == '__main__':
    app.run(debug=True)
