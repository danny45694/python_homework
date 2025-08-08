import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
...
# To write a log record:
logger.log(logging.INFO, "this string would be logged")


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}, args: {args}, kwargs: {kwargs}, return: {result}")
        return result
    return wrapper

@logger_decorator
def none():
    return

@logger_decorator
def arguments(*args):
    return True

@logger_decorator
def keyarguments(**kwargs):
    return True




