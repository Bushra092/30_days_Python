
#! 🎯 Challenge
#? -  Build a temperature converter CLI tool

import argparse

parser = argparse.ArgumentParser(description = 'Please Enter Tempreture and convert type F or C' )

parser.add_argument('--temp', type=float, help="Temperature to convert" , required=True)
parser.add_argument('--Convert_Type', type=str,  choices=['Celsius', 'Fahrenheit'], help="Convert to which unit", required=True)
 

args = parser.parse_args()
if args.Convert_Type.lower() == 'fahrenheit':
    result = (args.temp * 9/5) + 32
    print(f"{args.temp}°C = {result:.2f}°F \n\n\n")

if args.Convert_Type.lower() == 'celsius':
    result = (args.temp - 32) * 5/9
    print(f"{args.temp}°F = {result:.2f}°C\n\n\n") 