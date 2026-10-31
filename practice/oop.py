#OOP (Object Oriented Programing) 

#a way of writing code

# class Student:

#     def get_name():
#         return "Arib"

# name = "Arif"

# print(Student.get_name())
# print(name)



#Cars blue print

#brand
#model
#number plate
#color
#seats
#HP


# class Cars:

#     Dealer_ship = "Voyager Cars"

#     car_health = 0


#     def __init__(self,brand,model,color,hp):
#         self.brand_name = brand
#         self.model_number = model
#         self.color_code = color
#         self.horse_power = hp

#     def get_car_info(cars_list):

#         for car in cars_list:
#             print(car.brand_name,"\n",car.color_code,"\n",car.model_number,"\n",car.horse_power)
#             print("\n")

#     def damage():
#         pass

        # if collisions are equal to 3, car = "Totaled"
        #else collisions++
        #health_health - 30



        # if collision:

        #     damage()


# print(Cars.car_health)

# car1 = Cars("Mercedes",2027,"black",1600)
# car2 = Cars("Ferrari",2023,"pink",1500)
# car3 = Cars("BMW M8",2022,"red",1200)
# car4 = Cars("Bugatti",2024,"blue",1100)
# car5 = Cars("Lamborghini",2026,"yellow",100)
# car6 = Cars("Toyota",2028,"grey",1000)

# cars_list = [car1,car2,car3,car4,car5,car6]


# Cars.get_car_info(cars_list)



#access modifyer
# public





# car = "Mehran"
# car = "Lambourghini"


# print(car)

# profile = {
#     "name": "SHAHAB"
# }

# profile["name"] = "Abeera"


# print(profile["name"])




# self = {

# }


# self.car = "Ferrari"

# print(self["car"])







# Four Pillars of Object Oriented Programing.

#Encapsulation
#Inheritance
#Polymorphism
#Abstraction









# class Car:
#     def acceleration(self):
#         print("The car is accelerating")

#     def brake(self):
#         print("The car is braking")


# class SportsCar(Car):
#     def turbo(self):
#         print("Turbo Acivated")

# class ElectricCar(SportsCar):
#     def recharge(self):
#         print("battery is recharging")


# sports_car = SportsCar()

# electric_car = ElectricCar()

# sports_car.acceleration()
# sports_car.brake()
# sports_car.turbo()

# electric_car.acceleration()
# electric_car.brake()
# electric_car.turbo()
# electric_car.recharge()






# class Car:
#     def __init__(self,brand):
#         self.brand = brand
#         self.__speed = 0

#     def accelerate(self):
#         if self.__speed < 200:
#             self.__speed += 10

#         print("Speed: ", self.__speed)

#     def brake(self):
#         if self.__speed >=10:
#             self.__speed -=10
#         print("Speed: ", self.__speed)


# car1 = Car("Mercedes")

# car1.accelerate()
# car1.accelerate()
# car1.accelerate()

# car1.brake()


# hackSpeed = car1.__speed + 500

#print(hackSpeed) #AttributeError: 'Car' object has no attribute '__speed'





#polymorphism

# class truck:

#     def accelerate(self):
#         print("VROOOOM-RUMBLE-CHUG-CHUG")

# class mercedes:

#     def accelerate(self):
#         print("Vrmmm-shhh Zzzzt-hum")




# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start_engine(self):
#         pass
        


# class SportsCar(Vehicle):

#     def start_engine(self):
#         print("checking engine...")
#         print("Starting Sport car engine...")


# class ElectriCar(Vehicle):
#     def start_engine(self):
#             print("checking engine...")
#             print("Starting electric car motor...")


# car1 = SportsCar()
# car2 = ElectriCar()

# car1.start_engine()
# car2.start_engine()





