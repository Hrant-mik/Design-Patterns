class House:
    _house_xaracteristic = {
        "count_walls" : None,
        "count_windows" : None,
        "roof" : None,
        "trees" : None,
        "Doors" : None
    }
    
    
class Home_preparation:
    def __init__(self):
    
        self._house_xaracteristic = {
            "count_walls" : 0,
            "count_windows" : 0,
            "roof" : None,
            "trees" : None,
            "Doors" : None
        }
   
    def create_walls(self, count):
        self._house_xaracteristic["count_walls"] = count
        
    def create_windows(self, count):
        self._house_xaracteristic["count_windows"] = count
    
    def create_roof(self, count):
        self._house_xaracteristic["roof"] = count
    
    def create_trees(self, count):
        self._house_xaracteristic["trees"] = count
        
    def create_doors(self, count):
        self._house_xaracteristic["Doors"] = count
    
    def view(self):
        return self._house_xaracteristic
        


created = Home_preparation()


# created.create_doors(5)
# created.create_roof(2)
# created.create_trees(3)
# created.create_windows(5)
created.create_walls(3)
created.view()




# class House:
#     def __init__(self,count_walls = None, count_windows = None, roof = None, trees = None, Doors = None):
#         self.count_walls = count_walls
#         self.count