import argparse

def add(args):
    return args[0]+args[1]

def multiply(args):
    return args[0]*args[1]

def divide(args):
    return args[0]/args[1]

def subtract(args):
	return args[0]-args[1]

parser = argparse.ArgumentParser("A Command Line Calculator."+
                                 "\n\tAuthor - Abhinn Vyas")

parser.add_argument('-a','--add',nargs=2,metavar=('num1','num2'),
                    help="num1 added to num2",type=int)
parser.add_argument('-m','--mult',nargs=2,metavar=('num1','num2'),
                    help="num1 multiplied to num2",type=int)
parser.add_argument('-d','--div',nargs=2,metavar=('num1','num2'),
                    help="num1 divided by num2",type=int)
parser.add_argument('-s','--sub',nargs=2,metavar=('num1','num2'),
                    help="num2 subtracted from num1",type=int)

arg = parser.parse_args()

if arg.add != None:
    print(method.add(arg.add))
elif arg.mult != None:
    print(method.multiply(arg.mult))
elif arg.div != None:
    print(method.divide(arg.div))
elif arg.sub != None:
    print(method.subtract(arg.sub))
else:
    print("Error: No Argument specified!!!")

