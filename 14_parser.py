import argparse

parser = argparse.ArgumentParser(description = "Simple Calculator")
parser.add_argument("x" , type= float, help = "First_Number")
parser.add_argument("y" , type= float, help = "Second_Number")
parser.add_argument("-a","--add", action= "store_true" , help = "Sum Two Number")
parser.add_argument("-d","--div", action= "store_true" , help = "Div Two Number")
args = parser.parse_args()
print(args)
if args.add:
    result = args.x + args.y 
elif args.div:
    try:
        result = args.x / args.y
    except ZeroDivisionError as e:
        result =e
else:
    print("Command Not Found")
print(result)