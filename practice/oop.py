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


class Cars:

    Dealer_ship = "Voyager Cars"

    car_health = 0


    def __init__(self,brand,model,color,hp):
        self.brand_name = brand
        self.model_number = model
        self.color_code = color
        self.horse_power = hp

    def get_car_info(cars_list):

        for car in cars_list:
            print(car.brand_name,"\n",car.color_code,"\n",car.model_number,"\n",car.horse_power)
            print("\n")

    def damage():

        # if collisions are equal to 3, car = "Totaled"
        #else collisions++
        #health_health - 30



        # if collision:

        #     damage()








car1 = Cars("Mercedes",2027,"black",1600)
car2 = Cars("Ferrari",2023,"pink",1500)
car3 = Cars("BMW M8",2022,"red",1200)
car4 = Cars("Bugatti",2024,"blue",1100)
car5 = Cars("Lamborghini",2026,"yellow",100)
car6 = Cars("Toyota",2028,"grey",1000)

cars_list = [car1,car2,car3,car4,car5,car6]


Cars.get_car_info(cars_list)









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

