# Lambda function in Python language...

x=lambda a : a**3
print(x(4))


x=lambda a,b :a+b
print(x(3,9))


x=lambda a,b,c:a**b/c
print(x(9,5,3))

x=lambda a,b : a%b
print(x(3,10))


x=lambda i : 'even' if i%2==0 else 'odd'
print(x(9))

x=lambda age: 'adult' if age>18 else 'child'
print(x(20))

nums = [1, 2, 3, 4, 5, 6, 7, 8]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)


nums = [12, 55, 7, 89, 45, 100]

greater = list(filter(lambda x: x > 70, nums))
print(greater)


words = ["apple", "cat", "banana", "dog", "grapes"]

long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)


nums = [-5, 10, -2, 8, 0, 15]

positive = list(filter(lambda x: x > 0, nums))
print(positive)



names = ["Amit", "Rahul", "Om", "Isha", "Neel"]

vowel_names = list(filter(lambda x: x[0].lower() in "aeiou", names))
print(vowel_names)


data = ["Python", "", "Java", "", "C++"]

clean_data = list(filter(lambda x: x != "", data))
print(clean_data)


students = [("Amit", 80), ("Rahul", 72), ("Neel", 90), ("Priya", 65)]

top_students = list(filter(lambda x: x[1] > 75, students))
print(top_students)


words = ["madam", "python", "level", "code"]

palindromes = list(filter(lambda x: x == x[::-1], words))
print(palindromes)


nums = range(1, 101)

divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))
print(divisible)


#High level Lambda problems...
# filter()+ lambda problems...

nums = [2, 3, 4, 5, 6, 7, 8, 9, 11, 15]

primes = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1)), nums))
print(primes)


nums = [248, 864, 135, 420, 66, 79]

even_digit_nums = list(filter(lambda x: all(int(d) % 2 == 0 for d in str(x)), nums))
print(even_digit_nums)

words = ["team", "boot", "rain", "sky", "moon"]

two_vowels = list(filter(lambda x: sum(1 for c in x.lower() if c in "aeiou") == 2, words))
print(two_vowels)


data = [(2, 3), (5, 6), (1, 4), (7, 8)]

result = list(filter(lambda x: sum(x) > 10, data))
print(result)


nums = [1, 2, 4, 7, 9, 16, 20]

squares = list(filter(lambda x: int(x**0.5)**2 == x, nums))
print(squares)



people = [
    {"name": "Amit", "age": 20},
    {"name": "Rahul", "age": 17},
    {"name": "Neel", "age": 25}
]

adults = list(filter(lambda x: x.get("age", 0) > 18, people))
print(adults)


nums = range(1, 101)

divisible = list(filter(lambda x: x % 4 == 0 and x % 6 == 0, nums))
print(divisible)


nums = range(1, 20)

binary_filter = list(filter(lambda x: bin(x)[2:].count('1') > bin(x)[2:].count('0'), nums))
print(binary_filter)


words = ["silent", "enlist", "google", "inlets"]

anagrams = list(filter(lambda x: sorted(x) == sorted("listen"), words))
print(anagrams)


