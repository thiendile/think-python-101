from typing import List


def reserve(letter):
    reser = ""
    while len(letter) > 0:
        reser = reser + letter[-1]

        letter = letter[0:-1]
    return reser


print(reserve("happy"))


def reverse(letters):
    result = ""
    for i in range(len(letters) - 1, -1, -1):
        result += letters[i]
    return result


def mirror(l):
    return l + reverse(l)


print(mirror("good"))
print("aol""o")


def remove_letter(c, l):
    m = ""
    for i in l:
        if i != c:
            m += i
    return m



print(remove_letter("n", "c"))


def is_palindrome(l):
    ori = l[0:len(l) // 2]
    rese = l[len(l) // 2:]
    if reserve(ori) == rese:
        return True
    return False


print(is_palindrome("appap"))


def count(letter, string):
    found = string.find(letter, 0)
    count = 0
    while found != -1:
        count += 1
        found = string.find(letter, found + 1)
    return count


print(count("nana", "banana"))


def remove_2(substring, string, start=0):
    index = string.find(substring, start)
    if index < 0:
        return string, -1
    substring = string[:index] + string[index + len(substring):]
    return substring, index


print(remove_2("an", "banana"))


def remove_3(substring, string):
    i = string.find(substring, 0)
    while i >= 0:
        string = string[:i] + string[i + len(substring):]
        i = string.find(substring, i + 1)
    return string


print("------")
print(remove_3("ba", "bbbbaaaaaaa"))


def remove_4(substring, string):
    arr = string.split(substring)
    print(arr)
    return "".join(arr)


print(remove_4("12", "12345612"))


def remove_5(substring, string):
    (string, index) = remove_2(substring, string, 0)
    while index >= 0:
        (string, index) = remove_2(substring, string, index + 1)
    return string


print(remove_5("ba", "bbbbaaaaaaa"))
def abb(a,b):
    return a + b

print(abb(("xuna",1992),("tuna",1990)))