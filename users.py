from mysqlconnection import connectToMySQL

class User():

    def __init__(self, data=None):
        print(data)
        if data != None:
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.email = data['email']
            self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        return results

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"

        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete_DAuser(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def show_user(clas, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        
        # return the array of result
        results = connectToMySQL('users_schema').query_db(query, data)

        return results[0]

    @classmethod
    def edit_theuser(clas, data):

        query = " UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)
