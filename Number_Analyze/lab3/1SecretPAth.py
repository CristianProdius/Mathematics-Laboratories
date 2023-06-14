from sympy import symbols, Eq, solve

x, y = symbols('x y')

equations = [
    Eq(2*x - y, 4),   
    Eq(3*x + 2*y, 7), 
    Eq(x + y, 3),    
    Eq(4*x - y, 1),  
    Eq(x - 3*y, -2)   
]

solution = solve(equations, (x, y))

if solution:
    substitutions = [equation.subs({x: solution[x], y: solution[y]}) for equation in equations]
    order = [i+1 for i, sub in enumerate(substitutions) if sub == 0]

    if order:
        print(f"The solution to the system of linear equations is: x = {solution[x]}, y = {solution[y]}")
        print("The correct order of stepping stones is:")
        for i, stone in enumerate(order):
            print(f"Stone {stone}: Step {i+1}")
    else:
        print("No valid solution found for the system of linear equations.")
else:
    print("No solution found for the system of linear equations.")
