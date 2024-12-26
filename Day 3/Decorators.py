
def greet(fx):
    def mfx():  # this will execute before the function which is taken as a parameter
        print("Good morning")
        fx()
        print("Thanks for using this!")  # this will execute after the function which is taken as a parameter
    return mfx()


@greet
def hello():
    print("Hello !!")

hello()