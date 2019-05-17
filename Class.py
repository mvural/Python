class Car():
    def __init__(self,model,color,engine_horse_power):
        print("init function")
        self.model = model
        self.color = color
        self.engine_horse_power = engine_horse_power
        
Car1 = Car("BMW","white","260")
Car2 = Car("Mercedes","white","290")
Car3 = Car("Porsche","red","290")
print (Car1.model,Car1.color,Car1.engine_horse_power)
print (Car2.model,Car2.color,Car2.engine_horse_power)
print (Car3.model,Car3.color,Car3.engine_horse_power)