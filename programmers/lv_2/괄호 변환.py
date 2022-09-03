# All the problem took was patience, not others :( #

p = "()))((()"

def solution(p):
    def converter(string):
        new = ''
        for char in string:
            if char == '(':
                new += ')'
            else:
                new += '('
        return new

    def short_balance(brackets):
        open, close, idx = 0, 0, 0
        stack = 0
        flag = ''

        while True:
            if brackets[idx] == ')':
                close += 1
                stack -= 1
            else:
                open += 1
                stack += 1

            if stack < 0 : flag = False;

            if close == open:
                break

            idx += 1

        return (True, idx) if ((stack == 0) and (flag == '')) else (False, idx)

    def maker(p):
        if p == '':
            return ''

        flag, idx = short_balance(p)

        u, v = p[:idx + 1], p[idx + 1:]
        print(v)
        if flag == True:
            return u + maker(v)

        else:
            return '(' + maker(v) + ')' + converter(u[1:-1])

    return maker(p)

print(solution(p))
