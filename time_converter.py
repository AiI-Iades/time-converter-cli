import argparse

def convert_time(value, input_unit, output_unit):
    units = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
    return (value * units[input_unit]) / units[output_unit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('value', type=float)
    parser.add_argument('--input', choices=['s','m','h','d'], required=True)
    parser.add_argument('--output', choices=['s','m','h','d'], required=True)
    args = parser.parse_args()
    result = convert_time(args.value, args.input, args.output)
    print(f'{args.value} {args.input} = {result:.2f} {args.output}')