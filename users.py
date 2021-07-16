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