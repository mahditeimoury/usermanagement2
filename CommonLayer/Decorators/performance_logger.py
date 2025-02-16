import time
from datetime import datetime
import CommonLayer
from DataAccessLayer import *
import CommonLayer.State.user_state


def performance_logger_decorator(class_name):
    def decorator(main_function):
        def wrapper(*args, **kwargs):
            function_name = main_function.__name__
            call_datetime = datetime.now()
            start_time = time.time()
            output = main_function(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            user_id = CommonLayer.State.user_state.current_user_id

            cursor= conn.cursor()
            query = """
            insert into performance_logger (function_name, execution_time, call_datetime, user_id, class_name)
            values (?, ?, ?, ?, ?)            
            """
            information = (function_name, execution_time, call_datetime, user_id, class_name)
            cursor.execute(query, information)
            conn.commit()

            return output
        return wrapper
    return decorator