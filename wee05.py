def intersection(foo: str, bar: str) -> str | None:
    """
    Return a string containing each unique character that appears in both foo and bar.
    If there are no common characters, return None.
    """
    # quick reminder to self: foo and bar are just placeholder names
    # Collect characters from foo that also appear in bar, avoiding duplicates
    common_chars = []
    for ch in foo:
        if ch in bar and ch not in common_chars:
            common_chars.append(ch)

    # Build the result string or set it to None if empty
    result = "".join(common_chars) if common_chars else None
    # only one return statement here, per assignment rules
    return result

def is_alphabetical(string: str) -> bool:
    # remind myself: assume it’s all letters until I find a non-letter
    valid = True  # flag stays True unless a bad char shows up
    for ch in string:
        code = ord(ch)  # get ASCII code for this character
        # check: A–Z is 65–90, a–z is 97–122
        if not (65 <= code <= 90 or 97 <= code <= 122):
            valid = False  # oops, found something that’s not a letter
    # only one return statement, per assignment rules
    return valid

def letters_only(string: str) -> str | None:
    # quick reminder: strip out spaces, punctuation, and numbers
    result = ""  # build up only the letters from the original string
    for ch in string:
        code = ord(ch)  # get ASCII code to check if it's a letter
        if 65 <= code <= 90 or 97 <= code <= 122:
            result += ch  # keep this character, it’s A–Z or a–z
    # remind myself: return None when there aren’t any letters left
    return result if result else None

def generate_palindrome(string: str) -> str | None:
    # remind myself: if the string is empty, there’s nothing to mirror
    # build the palindrome by sticking the reverse of the string onto itself
    palindrome = string + string[::-1] if string else None
    # only one return statement allowed, so return the final result here
    return palindrome

def is_palindrome(string: str) -> bool:
    # quick reminder: only keep letters and digits, drop spaces/punctuation
    # remind myself to compare in lowercase so case doesn’t matter
    cleaned = ""
    for ch in string:
        code = ord(ch)
        if (65 <= code <= 90) or (97 <= code <= 122) or (48 <= code <= 57):
            cleaned += ch.lower()

    # check if the cleaned string reads the same forwards and backwards
    result = cleaned == cleaned[::-1]
    # only one return allowed by assignment rules
    return result


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
