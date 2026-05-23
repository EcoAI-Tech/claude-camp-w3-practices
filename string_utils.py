def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    cleaned_s = ''.join(s.split()).lower()
    return cleaned_s == cleaned_s[::-1]
