def reverse_fizzbuzz(string):
    fb, s_str = {'Fizz': 3, 'Buzz': 5, 'FizzBuzz': 15}, [int(x) if x.isnumeric() else x for x in string.split()]
    num_str = list(enumerate(s_str, start=-3))
    if all(isinstance(x, str) for x in s_str) and s_str[0:2] != ['Buzz', 'Fizz']:
        return [fb[x] * abs(num_str[s_str.index(x)][0]) if
                len(s_str) > 1 else
                fb[x] if all(isinstance(x, str) for x in s_str) else 0 for x in s_str]
    elif any(isinstance(x, int) for x in s_str):
        for x in s_str:
            if type(x) is int:
                return [x[0] for x in list(enumerate(s_str, start=x - s_str.index(x)))]
    elif s_str[0] == 'Buzz' and s_str[1] == 'Fizz':
        return [5, 6]
<<<<<<< HEAD
# Я и сам немного программист
=======
# Я и сам немного программист !
>>>>>>> 3731693153ed978cbd06b0046c04080a59b21b60
