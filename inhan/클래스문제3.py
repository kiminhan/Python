class Restaurant:
    number_served = 0
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_Restaurant(self, name, type):
        print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다." % (self.name,self.type))
    def open_Restaurant(self, name):
        print("저희 %s 레스토랑이 열렸습니다." % (self.name))
    def set_number_served(self,number):
        self.number_served=number
        print("방문한 손님은 %s명 입니다." % (self.number_served))
    def increment_number_served(self,number2):
        self.number_served+=number2
        print("방문한 총 손님은 %s명 입니다." % (self.number_served))

restaurant = Restaurant("이나니","일식")
restaurant.set_number_served(7)
restaurant.increment_number_served(9)
