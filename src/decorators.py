from datetime import datetime
from functools import wraps


def log(filename=None):
    """Декоратор который логирует вызов функции и ее результат в файл или в консоль"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_start = datetime.now()
                result = func(*args, **kwargs)
                log_message = f"""{func.__name__} started at {time_start} and finished at {datetime.now()}
{func.__name__} ok. Result {result}. Inputs: {args}, {kwargs}\n"""
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message = f"""{func.__name__} started at {time_start} and finished at {datetime.now()}
{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}\n"""
                raise
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator
