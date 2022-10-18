def fizzbuzz(num):
    """
    If a number is a multiple of 3 the answer is Fizz.  If a number is a multiple of 5 the answer is Buzz.
    If a number is a multiple of both 3 and 5 the answer is FizzBuzz.  Otherwise the answer is the value.
    """
    ans = ((num != 0)*(num%3 == 0)*"Fizz" + (num != 0)*(num%5 == 0)*"Buzz") or num
    return ans 