# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(str1, str2):
    str1_convert = str1.lower()
    str2_convert = str2.lower()
    result = False

    # check if length is same
    if len(str1_convert) == len(str2_convert):

        # sort the strings
        sorted_str1 = sorted(str1_convert)
        sorted_str2 = sorted(str2_convert)

        # if sorted char arrays are same
        if sorted_str1 == sorted_str2:
            result = True
        else:
            result = False
        return result

    else:
        return result


if __name__ == '__main__':
    print(find_anagrams("Hello", "ollhe"))
