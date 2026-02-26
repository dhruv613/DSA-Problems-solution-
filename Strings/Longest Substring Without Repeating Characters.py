def lengthOfLongestSubstring(s):

    unique_char = ""
    max_len = 0

    for i in range(len(s)):
        if s[i] in unique_char:
            pos = unique_char.find(s[i])
            unique_char = unique_char[pos+1:]

        unique_char += s[i]

        if len(unique_char) > max_len:
            max_len = len(unique_char)

    return max_len, unique_char

print(lengthOfLongestSubstring("fgfgdhssskkss"))

