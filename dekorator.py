def my_decorator(func):
    def sey_hi():
        print("Hello dior collega")
        func()
    return sey_hi
    
@my_decorator
def sey_how_are_you():
    print("How are you")
    
sey_how_are_you()