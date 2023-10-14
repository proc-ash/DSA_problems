# Problem Statement: “Given a string, check if the string is palindrome or not.”  
# A string is said to be palindrome if the reverse of the string is the same as the string.

def isPallindrome(start,string):
    if start >= len(string)//2:
        return True
    if string[start] != string[len(string)-start-1]:
            return False
    return isPallindrome(start +1, string)

if __name__ == '__main__':
    print(isPallindrome(0,'madam'))