from users_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query =  "SELECT * FROM users"
        results = connectToMySQL('users_db').query_db(query)
        object_users = []
        for data_dict in results:
            object_users.append(cls(data_dict))
        return object_users
    
    @classmethod
    def create_new_user(cls,data):
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        resultado = connectToMySQL( "users_db" ).query_db( query, data )
        return resultado