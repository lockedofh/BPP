from typing import Any

def catchExceptions(func:callable) -> Any:
    """Catches any exception occured when invoking the function.
    Returns False in case any exception was catched."""
    def wrapper(*arguments, **keywordArguments) -> Any:
        try:
            returnedValue = func(*arguments, **keywordArguments)
            return returnedValue
        except Exception as error:
            return False
    return wrapper
        
def printOut(fun:callable) -> Any:
    """Wrapper that prints out the returned value from the function being wrapped.

    :param fun: any callable that returns a value.
    :return: the return of the wrapped function
    """
    def wrapper(*arguments, **keywordArguments) -> Any:
        try:
            returnedValue = fun(*arguments, **keywordArguments)
        except Exception as error:
            returnedValue = str(error)
        finally:
            print(returnedValue)
        return returnedValue
    return wrapper
