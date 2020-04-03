from argparse import ArgumentParser
from Shunting_yard import Shunting_yard

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('expression', help='arithmetic expression', nargs='+')
    args = parser.parse_args()

    expression = ''.join(args.expression)
    replaced = expression.replace('**', '^')
    # check = eval(expression)

    yard = Shunting_yard(replaced)
    yard.replace_unary_minus()
    yard.to_postfix()

    print(f'Result: {yard.eval_postfix()}')
    # print(f'To check: {check}')