class add_sub:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
        
    def subtract(self):
        return self.x - self.y
if __name__ == '__main__':
    x = 10
    y = 6
# create an instance
opp = add_sub(x,y)
# call add method
print(f'{x} + {y} = {opp.add()}')
#print(opp.add())
# call subtract method
print(f'{x} - {y} = {opp.subtract()}')