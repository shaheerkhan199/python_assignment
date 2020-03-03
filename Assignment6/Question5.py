class Car():
    def __init__(self,car_name,car_model,car_color,car_speed,car_price):
        self.car_name = car_name
        self.car_model = car_model
        self.car_color = car_color
        self.car_speed = car_speed
        self.car_price = car_price
    def start(self):
        print("Car is now start")
    def accelerate(self):
        print("Car is now running")
    def stop(self):
        print("Car is now Stop")
if __name__=="__main__":
    c1 = Car("Mercedes","2015","Black",400,2550000)
    c2 = Car("Fortuner","2019","White",350,3350000)
    c3 = Car("Alto","2005","Silver",250,150000)
    c4 = Car("Mehran","2012","Silver",200,170000)
    c5 = Car("BMW","2010","Black",300,6550000)
    