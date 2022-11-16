def anagram(str11):
    if len(str11)%2!=0:
        return "the given string can not be anagram"
    mid=len(str11)//2
    str22=str11[:mid]
    str23=str11[mid:len(str11)]
    for i in str22:
      if i not in str23:
        return "the given string is not anagram"
      else:
        return "the given string is  anagram"


str11="abcabc"
print(anagram(str11))