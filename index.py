import platform

# Starting python

def main():
    print('Hello world')
    print('This is python version {}'.format(platform.python_version()))

# it this file is imported and used as API
# this __name__ would be the name of the file
# instead of __main__. Therefore,
# it doesn't run main() function
if __name__ == '__main__': main()