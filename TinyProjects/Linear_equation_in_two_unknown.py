from sympy import symbols, Eq, solve

if __name__ == "__main__":
    # r = (1 * 2.2 * 3.3) / (1 * 2.2 + 1 * 3.3 + 2.2 * 3.3)
    i1, i2 = symbols("i1 i2")
    eq1 = Eq(-9 + 800 * i1 + 470 * i2, 0)
    eq2 = Eq(-300 * i1 + 1330 * i2, 0)
    solutions = solve([eq1, eq2], [i1, i2])
    print(f"x = {solutions[i1]}\n"
          f"y = {solutions[i2]}")
