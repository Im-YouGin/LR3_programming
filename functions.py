def presedence(operator):
    operator_dct = {3: ('^','#'),
                    2:('*','/'),
                    1:('+', '-')}

    for key, value in operator_dct.items():
        if operator in value:
            return key

def association(operator):
    operator_dct = {'right': ('^', '#'),
                    'left': ('*', '/', '+', '-')}

    for key, value in operator_dct.items():
        if operator in value:
            return key

def evaluate(left, right, operator):
    left = left.replace('(', '').replace(')', '')
    right = right.replace('(', '').replace(')', '')

    if operator == '+':
        return float(left) + float(right)

    elif operator == '-':
        return float(left) - float(right)

    elif operator == '*':
        return float(left) * float(right)

    elif operator == '/':
        return float(left) / float(right)

    elif operator == '^':
        return float(left) ** float(right)