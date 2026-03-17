



def check_palindrome(word):
  x=len(word)
  p=x//2
  for i in range(p):
    y=i+1
    w=x-i
    if word[x-w] == word[x-y]:
        return True
    else:
        return False
print(check_palindrome("raccar"))