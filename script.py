""" numbers """

# Define a function is_even that will take a number x as input.
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
        
# Define a function is_int that takes a number x as an input.
def is_int(x):
    if x - int(x) == 0:
        return True
    else:
        return False
        
# Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.
def digit_sum(n):
    string = str(n)
    total = 0
    for char in string:
        num = int(char)
        total += num
    return total
    
# Define a function factorial that takes an integer x as input.
def factorial(x):
    total = 1
    for n in range(1,x + 1):
        total *= n
    return total

# Define a function called is_prime that takes a number x as input.
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        else:
            return True

""" strings """

# Define a function called reverse that takes a string textand returns that string in reverse.
# You may not use reversed or [::-1] to help you with this.
def reverse(text):
    text = str(text)
    reversed_string = ""
    for n in range(len(text)-1, 0-1, -1):
        print text[n]
        reversed_string += text[n]
    return reversed_string

# Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
def anti_vowel(text):
    vowels = ["a", "e", 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in vowels:
        text = text.replace(i, "")
    return text

# Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word = word.lower()
    total_score = 0
    for l in word:
        total_score += score[l]
    return total_score

# Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.
def censor(text, word):
    censored = "*" * len(word)
    return text.replace(word, censored)
    
""" lists """    
    
# Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list.    
def count(sequence, item):
    counter = 0
    for i in sequence:
        if i == item:
            counter += 1
    return counter
   
# Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
def purify(nums):
    odd = list(filter(lambda x: x % 2 == 0, nums))
    return odd
    
# Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.
def product(ints):
    product = 1
    for i in ints:
        product *= i
    return product
    
# Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
def remove_duplicates(nums):
    nums_unique = set(nums)
    return nums_unique
    
# Write a function called median that takes a list as an input and returns the median value of the list.
def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        middle = len(lst) / 2
        median_value = float(lst[middle - 1] + lst[middle]) / 2
    else:
        median_value = lst[len(lst) / 2]
    return median_value