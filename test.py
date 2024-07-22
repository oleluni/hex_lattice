from sympy import symbols

# Step 1: Define the symbols
mL0, mL2, mR3 = symbols('mL0 mL2 mR3')

# Step 2: Create the list of expressions
expressions = [mL2, -mL0, -mL0 - mR3]

# Step 3: Substitute mL0 with 0.5 in each expression
substituted_expressions = [expr.subs(mL0, 0.5) for expr in expressions]

# Display the result
print(substituted_expressions)
