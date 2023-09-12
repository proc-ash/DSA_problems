# Problem Statement: Given a string s, reverse the words of the string
def reverseString(sentence):
    words = ''
    temp = ''
    left = 0
    right = len(sentence)-1
    while left <= right:
        if sentence[left] != ' ':
            temp += sentence[left]
        elif sentence[left] == ' ' and temp != '':
            if words != '':
                words = temp +' '+words
            else:
                words = temp
            temp = ''
        left += 1

    if temp!='':
        if words!='':
            words = temp + ' ' + words
        else:
            words = temp
    return words

if __name__=='__main__':
    sentence = 'Welcome   to Coding Ninjas'
    print(reverseString(sentence))
