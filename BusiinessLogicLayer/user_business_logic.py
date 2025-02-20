import CommonLayer.State.user_state
from CommonLayer.model.response import Response
import CommonLayer.State.user_state
from CommonLayer.Decorators.performance_logger import performance_logger_decorator
from DataAccessLayer.user_data_access import UserDataAccess
from CommonLayer.Entities.user import User
import hashlib


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    # @performance_logger_decorator("UserBusinessLogic")
    def login(self, username, password):
        try:
            user = User(None, None, None, username, password, None, None)
        except ValueError as error:
            return Response(False, None, error.args[0])
        # hash password
        password_hash = hashlib.md5(password.encode()).hexdigest()

        user = self.user_data_access.get_user(username, password_hash)
        if user:
            match user.status:
                case 0:
                    return Response(False, None, "Your Account Is Deactivated")
                case 1:
                    CommonLayer.State.user_state.current_user_id = user.id
                    return Response(True, user, None)
                case 2:
                    return Response(False, None, "Your Account Is Pending")

        else:
            return Response(False, None, "Invalid username or password")

    # @performance_logger_decorator("UserBusinessLogic")
    def register(self, first_name, last_name, username, password):

        password_hash = hashlib.md5(password.encode()).hexdigest()
        try:
            self.user_data_access.register_user(first_name, last_name, username, password_hash)

        except:
            return Response(False, None, "User Name Exists Please Choose A Different One")

        else:
            message = f"welcome {first_name} {last_name}! you are now Registered as {username}"
            return Response(True, None, message=message)

    def get_user_management_list(self, current_user):
        if current_user.role_id == 1:
            user_list = self.user_data_access.get_user_list()
            return Response(True, user_list, None)
        else:
            return Response(False, None, "Access Denied.")

    def activate_user(self, id_list):
        for id in id_list:
            self.user_data_access.activate_user(id, 1)

    def deactivate_user(self, id_list):
        for id in id_list:
            self.user_data_access.deactivate_user(id)

    def pending_user(self, id_list):
        for id in id_list:
            self.user_data_access.activate_user(id, 2)

    def search_user(self, term):
        user_list = self.user_data_access.search_user(term)
        return user_list

    def change_role(self, id, role):
        for i in id:
            self.user_data_access.change_role(i, role)
