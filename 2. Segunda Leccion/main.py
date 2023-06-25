from functools import reduce
from operator import mul
from typing import Union

class Calculator(object):
    """Class containing really basic funtionalities to 
    operate with float and int values."""        
        
    def isDigit(self, valueToCheck:object) -> bool:
        """Checks if the value passed is either a float or an int."""
        isInt = isinstance(valueToCheck, int)
        isFloat = isinstance(valueToCheck, float)
        return isInt or isFloat
    
    def sum(self, *args) -> float:
        """Sums up all the values entered in the method. Keeps only the numbers (float | int)."""
        numbersTuSumUp = filter(self.isDigit, args)
        total = sum(numbersTuSumUp)
        return float(total)
        
    def multiply(self, *args) -> float:
        """Multiplies all the values entered (they must be int or float)."""
        numbersToMultiply = filter(self.isDigit, args)
        numbersToMultiply = map(float, numbersToMultiply)
        total = reduce(mul, numbersToMultiply)
        return total
    
    def elevate(self, numberToElevate:Union[int, float], timesToElevate:Union[int, float]) -> float:
        """Elevate one number the times needed.
        
        :param numberToElevate: the number that is multiply by itself.
        :param timesToElevate: the amount of times the number is elevated."""
        if (self.isDigit(numberToElevate) and self.isDigit(timesToElevate)):
            total = numberToElevate ** timesToElevate
            return float(total)
        else:
            print(f"Check the value for {numberToElevate} and {timesToElevate}. One or both are not operable.")
            
    def divide(self, dividend:Union[int, float], divisor:Union[int, float]) -> float:
        """Divides given dividend by the divisor."""
        if (self.isDigit(dividend) and self.isDigit(divisor)):
            try:
                result = dividend / divisor
                return result
            except ZeroDivisionError as error:
                print(f"{divisor} cannot be divisor.")
        else:
            print(f"Check dividend ({dividend}) and divisor ({divisor}) values. One or both are not operable.")