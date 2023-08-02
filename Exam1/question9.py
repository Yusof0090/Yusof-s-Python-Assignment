

def is_vowel(single_letter):
    vowel_letters="aeiouAEIOU"
    if single_letter in vowel_letters:
        return True
    else:
        return False

print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("E"))
print(is_vowel("Z"))