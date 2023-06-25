from typing import Iterable

def getMaxFromIterator(iterator:Iterable):
    """Given any iterator composed by iterators, gets the maximum value from each sub iterator."""
    maximumValues = [max(subIterator) for subIterator in iterator]
    breakpoint()
    return maximumValues

def isPrime(numberToEvaluate):
    """Evaluates if the given number is prime.
    For being prime, the number must be greater than 2 and must be divided (with no remainder) just by 1 and itself."""
    if numberToEvaluate < 2: return False
    for numberInRange in range(2, int(numberToEvaluate ** 0.5) + 1):
        remainder = numberToEvaluate % numberInRange
        if remainder == 0:
            return False
    return True

if __name__ == "__main__":
    iterator = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
    maximumValues = getMaxFromIterator(iterator)
    numbers = [3, 4, 8, 5, 5, 22, 13]
    primes = list(filter(isPrime, numbers))
    breakpoint()