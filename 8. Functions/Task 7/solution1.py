def is_palindrome(str):
    str = str.lower()
    if str[::-1] == str:
        return True
    else:
        return False
print(is_palindrome("Tenet"))