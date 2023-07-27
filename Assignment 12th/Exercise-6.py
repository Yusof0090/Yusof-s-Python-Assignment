
input_vowel=input("type one letter?")
def  is_vowel(a_single_letter):
    
    vowel_latter=["a","e","i","o","u","A","E","I""O","U"]
    if a_single_letter in vowel_latter:
        print(True)
    else:
        print(False)
is_vowel(input_vowel)