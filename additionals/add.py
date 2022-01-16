from functools import wraps

def func_name(func):
    @wraps(func)
    def print_func(*args,**kwargs):
        print("---------------------------")
        print("Called method:", func.__name__, "...")
        func()
        print("... finish method:", func.__name__)
        print("---------------------------")
    return print_func

    # def __str__(self):
    #     return f"{self.__class__.__name__} module is called"