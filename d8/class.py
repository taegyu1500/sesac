from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass


class Car(vehicle):
    speed = 0
    __position = [0,0]
    directions = ['left', 'right', 'up', 'down']
    color = ""
    __price = 0
    count = 0 
    
    def __init__(self, speed=0, position=[0,0], color='white', price=100):
        self.speed = speed
        self.__position = position
        self.color = color
        self.__price = price
        Car.count += 1
        
    def accel(self):
        if self.speed <= 10:
            self.speed += 1
    def brake(self):
        if self.speed >= 0:
            self.speed -= 1
    def move_car(self,direction):
        if direction not in self.directions or self.speed == 0:
            return False
        dx, dy = [[-1,0], [1,0], [0,1], [0,-1]][self.directions.index(direction)]
        x,y = self.__position
        self.__position = [x+(dx*self.speed), y+(dy*self.speed)]
    def show_position(self):
        print(self.__position)
    def get_position(self):
        return self.__position
    def set_color(self, color):
        self.color = color
    def print_info(self):
        print(f"{Car.count}번 {self.color}색 {self.__price}원 트럭의 위치: {self.__position}")
    
    @classmethod
    def create_fast_car(cls, position, color):
        return cls(speed=10, position=position, color=color)
    
    @staticmethod
    def show_speed(speed):
        print(f'현재 속도는 {speed * 10} km/s 입니다.')
        
    def start_engine(self):
        print(f'{Car.count}번 {self.color}색 차량 엔진 시동')
    def stop_engine(self):
        print(f'{Car.count}번 {self.color}색 차량 엔진 정지')
    
truck = Car(price=300)
truck.set_color('red')
# truck._price2(33)
# truck.speed = 4
# truck._Car__price = 3
truck.accel()
truck.accel()
truck.move_car('left')
truck.show_position()
truck.accel()
truck.move_car('up')
truck.show_position()
truck.print_info()
truck2 = Car(speed=4, position=[5,5])
truck2.set_color('blue')
truck2.accel()
truck2.accel()
truck2.accel()
truck2.move_car('right')
truck2.show_position()
truck2.print_info()
truck3 = Car.create_fast_car([10,10], "black")
truck3.move_car("up")
truck3.print_info()
trucks = [Car() for _ in range(10)]
trucks[0].print_info()
trucks[-1].print_info()
Car.show_speed(50)

class public_transit(Car):
    number = 0
    def __init__(self, number):
        super(public_transit, self).__init__()
        self.number = number
    def set_number(self, number):
        self.number = number

class fast_car(Car):
    def __init__(self):
        super(fast_car, self).__init__()
        self.speed = 10
bus = public_transit(3)
bus.set_number(6)
bus.accel()
bus.move_car('up')
bus.print_info()
class printer():
    def prints(self):
        a = []
        for i in self.__dict__.items():
            if(i[0][0] != '_'):
                a.append(f"{i[0]} : {i[1]}")
        return "\n".join(a)

class electric_bus(public_transit):
    fuel = ''
    def __init__(self, fuel):
        super(electric_bus, self).__init__(5)
        self.fuel = fuel

class dual_class(printer, electric_bus):
    def __init__(self, fuel):
        super(dual_class, self).__init__(fuel)

bus_2 = electric_bus('energy')
print(bus_2.number, bus_2.fuel)

bus_3 = dual_class('gas')
print( bus_3.prints())
bus_3.accel()

class string_bus () :
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return self.string
    
bus_4 = string_bus('aa')
print(bus_4)
print(str(bus_4))

class Sedan(Car):
    def accel(self):
        super().accel()
        return f'세단 엑셀'
    def brake(self):
        super().brake()
        return f'세단 브레이크'
    
class pick_up_truck(Car):
    def accel(self):
        super().accel()
        return f'픽업트럭 엑셀'
    def brake(self):
        super().brake()
        return f'픽업트럭 브레이크'

sedan = Sedan()
pcTruck = pick_up_truck()


print(sedan.accel())
print(sedan.brake())
print(pcTruck.accel())
print(pcTruck.brake()) 

car_list = [sedan, pcTruck, truck]
for c in car_list:
    c.start_engine()
    c.stop_engine()