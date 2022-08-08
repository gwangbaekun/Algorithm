def generate_hashtag(s):
    string = "#"
    for charIndex in range(0,len(s)):
        char = s[charIndex]
        if char != " ":
            if s[charIndex - 1] == " ":
                string += char.upper()
            elif charIndex == 0:
                string += char.upper()
            else:
                string += char.lower()
    
    if (string == "#"):
        return False
    if (len(string) >= 140):
        return False
    return string