# #class polymorphism
# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("drive")
#
# class boat:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("sail")
# class airplane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("fly")
#
# car1=car("tata","altroz")
# boat1=boat("mj","mj1")
# airplane1=airplane("jet","jet1")
#
# for x in (car1,boat1,airplane1):
#     x.move()



# ############### Inheritance Polymorphism ######################################
#
# class Vechicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("drive")
#
# class car(Vechicle):
#     pass
#
# class boat(Vechicle):
#     # def move(self):
#     #     print("sail")
#     pass
# class plane(Vechicle):
#     def move(self):
#         print("fly")
#
#
# car1=car("tata","altroz")
# boat1=boat("mj","boat1")
# plane1=plane("plane","plane1")
#
# for x in (car1,boat1,plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()


