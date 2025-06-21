import argparse

# parse = argparse.ArgumentParser(description="Geeting someone for with their name.")

# parse.add_argument('--name', type=str, help="Name of the Person", required=True)

# args = parse.parse_args()


# print(f"Hello, {args.name}!")



#? 🔹 Step 3: Try It Yourself
#? Let’s build a calculator CLI app step-by-step. We’ll support:

#? --operation: add, sub, mul, div

#? --x: first number

#? --y: second number

parser = argparse.ArgumentParser()

parser.add_argument('--num1', type=float, required= True )
parser.add_argument('--num2', type=float, required= True )
parser.add_argument('--operation', type=str, required= True )

args = parser.parse_args()

if args.operation ==  'add':
    result = args.num1 + args.num2
elif args.operation == 'sub':
    result = args.num1 - args.num2
elif args.operation == 'mul':
    result = args.num1 * args.num2
elif args.operation == 'div':
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation. Use add, sub, mul, or div."

print("Result:", result)
