from string_utils import reverse_words, count_vowels, is_palindrome

def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("hello") == "hello"
    assert reverse_words("") == ""

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("xyz") == 0
    assert count_vowels("AEIOU") == 5

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
