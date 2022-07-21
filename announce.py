def announce(f):
    def wrapper():
        print("About to run the function")
        f()                         #this will execute by printing hello world
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("hello wolrd!")

hello()