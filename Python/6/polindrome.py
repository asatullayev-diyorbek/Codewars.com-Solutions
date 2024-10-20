"""https://www.codewars.com/kata/5a1560c980171f3f68000037/train/python"""
TABLE = {
    (True, True): "both",
    (True, False): "vowel",
    (False, True): "consonant",
    (False, False): "neither"
}

def palindrome(s):
    vowels, consonants = [], []

    for char in s.lower():
        if char in 'aeiou':
            vowels.append(char)
        elif char in 'bcdfghjklmnpqrstvwxyz':
            consonants.append(char)

    is_vowel = vowels == vowels[::-1]
    is_consonant = consonants == consonants[::-1]

    return TABLE[(is_vowel, is_consonant)]


if __name__ == '__main__':
    print(palindrome(' *73_ ab'))  # result: both
