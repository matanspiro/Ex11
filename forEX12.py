@app.route('/usersPage', defaults={'user_id': -1, 'orders': 100})
@app.route('/usersPage/<int:user_id>/<orders>')
def get_users_func(user_id, orders):
    if user_id == -1:
        return_dict = {}
        query = 'select * from users;'
        users = interact_db(query=query, query_type='fetch')
        for user in users:
            return_dict[f'user_{user.id}'] = {
                'status': 'success',
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'orders': orders
            }
    else:
        query = 'select * from users where id=%s;' % user_id
        users = interact_db(query=query, query_type='fetch')
        # json is a string dictionary
        # from flask import jsonify. in js we had parse and stringify, in flask we have jsonify
        # we return the data from our db in a json format
        if len(users) == 0:
            return_dict = {
                'status': 'failed',
                'message': 'user not found'
            }
        return_dict = {
            'status': 'success',
            'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email,
            'orders': orders
        }
    return jsonify(return_dict)

