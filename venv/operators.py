# Legal operators
legal_operators = {'+', '-', '*', '/', '^', '~', '%', '!', '@', '$',
                   '&', '(', ')'}

# Operators that need to be fixed
operators_to_fix = {'-', '~'}

# Dictionary of the operators and their levels.
operator_dic = {
    # Level 1
    '+': 1,
    '-': 1,
    # Level 2
    '*': 2,
    '/': 2,
    # Level 3
    '^': 3,
    # Level 4
    '%': 4,
    # Level 5
    '@': 5,
    '$': 5,
    '&': 5,
    # Level 6
    '~': 6,
    '!': 6
}

# Operators with two operands with no minus.
two_operands_no_minus = {'+', '*', '/', '^', '%', '@', '$', '&'}

# Operators with two operands with minus.
two_operands = {'+', '-', '*', '/', '^', '%', '@', '$', '&'}

# Operators with one operand that come before it.
one_operand_before = {'~'}

# Operators with one operand that come after it.
one_operand_after = {'!'}

