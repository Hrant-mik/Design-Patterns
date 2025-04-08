
    
class Home_preparation:
    def __init__(self):
        self.count_walls = None
        self.count_windows = None
        self.roof = None
        self.trees = None
        self.Doors = None
        
   
    def create_walls(self, count):
        self.count_walls = count
        
    def create_windows(self, count):
        self.count_windows = count
    
    def create_roof(self, count):
        self.roof = count
    
    def create_trees(self, count):
        self.trees = count
        
    def create_doors(self, count):
        self.Doors = count
    
    def __str__(self):
        
        return str({key : value for (key, value) in self.__dict__.items() if value})


created = Home_preparation()


created.create_doors(5)
created.create_roof(2)
# created.create_trees(3)
# created.create_windows(5)
created.create_walls(3)
print(created)




# class House:
#     def __init__(self,count_walls = None, count_windows = None, roof = None, trees = None, Doors = None):
#         self.count_walls = count_walls
#         self.count