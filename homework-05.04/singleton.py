class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        self.value = value
        
singl1 = Singleton("First")
singl2 = Singleton("Second")

print(singl1.value)
print(singl2.value)