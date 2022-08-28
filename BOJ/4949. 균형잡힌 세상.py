import sys
hash = {']' : '[', ')' : '('}
def balancedOrNot(words):
    mystack = []
    for char in words:
        if char in hash.values(): mystack.append(char);
        if char in hash.keys():
            if mystack != []:
                if mystack[-1] == hash[char]:
                    mystack.pop()
                else:
                    return 'no'
            else:
                return 'no'
    return 'yes' if mystack == [] else 'no'

while True:
    read = sys.stdin.readline
    string = read().rstrip()
    if string == '.': break
    print(balancedOrNot(string))


