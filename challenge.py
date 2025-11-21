# Mirror Equation Challenge - Python
# Tidak menggunakan regex, eval, split, reverse builtin

def manual_reverse(num):
    rev = ""
    for i in range(len(num) - 1, -1, -1):
        rev += num[i]
    return rev

def parse_equation(eq):
    # Format selalu: angka + angka = angka
    a, b, c = "", "", ""
    part = 0  # 0=a, 1=b, 2=c

    for ch in eq:
        if ch == " ":
            continue
        if ch == "+":
            part = 1
            continue
        if ch == "=":
            part = 2
            continue
        if part == 0:
            a += ch
        elif part == 1:
            b += ch
        else:
            c += ch
    return a, b, c

def solve(eq):
    a, b, c = parse_equation(eq)

    A, B, C = int(a), int(b), int(c)

    # Check correct
    if A + B == C:
        return "correct"

    # check a first
    revA = int(manual_reverse(a))
    if revA + B == C:
        return f"a,{revA}"

    # check b
    revB = int(manual_reverse(b))
    if A + revB == C:
        return f"b,{revB}"

    # check c
    revC = int(manual_reverse(c))
    if A + B == revC:
        return f"c,{revC}"

    return "no solution"


# Example test cases (as required output from problem statement)
tests = [
    "12 + 34 = 64",
    "15 + 51 = 66",
    "16 + 23 = 93",
    "21 + 34 = 55",
    "10 + 10 = 50"
]

for t in tests:
    print(solve(t))
