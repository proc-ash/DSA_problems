# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

def longestCommonPrefix(S):
    if not S: return ''
    m, M, i = min(S), max(S), 0
    print(m,M)
    for i in range(min(len(m),len(M))):
        if m[i] != M[i]: break
    else: i += 1
    return m[:i]

if __name__=='__main__':
    arr = ['abcd','ac','abref','abcde']
    print(longestCommonPrefix(arr))