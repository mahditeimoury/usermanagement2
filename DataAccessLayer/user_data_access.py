from CommonLayer.Entities.user import User
from . import conn
class UserDataAccess:
    def get_user(self, username, password):
        cursor = conn.cursor()
        query = f"""
                           select id,
                           first_name,
                           last_name,
                           user_name,
                           password,
                           status,
                           role_id
                           from users
                           where user_name = ? and password = ?
                           """
        information= (username,password)
        data = cursor.execute(query,information).fetchone()
        # cursor.close()
        # conn.close()
        if data:
            return User(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

    def register_user(self, first_name, last_name, username, password):
        cursor = conn.cursor()
        query = f"""
                insert into users (first_name, last_name, user_name, password, status, role_id)
                values (?, ?, ?, ?, ?, ?)
"""
        information = (first_name, last_name, username, password, 2, 2)
        cursor.execute(query,information)
        conn.commit()
        # cursor.close()
        # conn.close()

    def get_user_list(self):

        user_list = []
        cursor = conn.cursor()
        query = f"""
                    select id,
                    first_name,
                    last_name,
                    user_name,
                    password,
                    status,
                    role_id
                    from users
                    where role_id != ?
                    """
        information = (1,)
        data_list = cursor.execute(query, information).fetchall()

        for data in data_list:
            user=User(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            user_list.append(user)

        return user_list

    def activate_user(self, id, status):
        cursor = conn.cursor()
        query= f"""
                update users
                set status = ?
                where id = ?                
                            """
        information = (status, id)
        cursor.execute(query,information)
        conn.commit()

    def deactivate_user(self, id):
        cursor = conn.cursor()
        query= f"""
                update users
                set status = ?
                where id = ?                
                            """
        information = (0, id)
        cursor.execute(query,information)
        conn.commit()

    def search_user(self, term):
        user_list = []
        cursor = conn.cursor()
        query = f"""
                select id,
                first_name,
                last_name,
                user_name,
                status,
                role_id
                from users
                where first_name like '%{term}%' or last_name like '%{term}%'
                or user_name like '%{term}%'
                """

        data_list = cursor.execute(query).fetchall()
        for data in data_list:
            user=User(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            user_list.append(user)

        return user_list

    def change_role(self, id, role_id):
        cursor = conn.cursor()
        query = f"""
            update users
            set role_id = ?
            where id = ?
                        """
        information = (role_id, id)
        cursor.execute(query,information)
        conn.commit()