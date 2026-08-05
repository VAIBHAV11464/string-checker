def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
def count_uppercase(s):
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = 0 
    for char in s:
        if char is up:
            x +=1
    return x

def feature_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char not in vowels:
            count += 1
    return count

if __name__ == "__main__":
    test_string = "vscode"
    test_string2 = "giithub"
    result = count_vowels(test_string)
    result_2 = count_vowels(test_string2)
    print(f"The number of vowels in '{test_string}' is: {result}")
    print(f"The number of vowels in '{test_string2}' is: {result_2}")