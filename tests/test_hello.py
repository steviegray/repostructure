#from .context import mymodule
import mymodule.hello

def test1():
	mymodule.hello.say_hello('stevie')


def main():
    test1()

if __name__ == "__main__":
    main()
