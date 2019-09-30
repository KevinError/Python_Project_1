# practice if statement

def function_argument_value(n = 5):
    print('value n: {}'.format(n))
    return n

def main():
    x = 10
    y = 20
    function_argument_value(10)
    if x < y:
        print('x < y: x is {} and y is {}'.format(x, y))
    else:
        print('x > y: x is {} and y is {}'.format(x, y))
    

if __name__ == '__main__': main()