class restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_restaurant(self, name, type):
        print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다." % (self.name,self.type))
    def open_restaurant(self, name):
        print("저희 %s 레스토랑이 열렸습니다." % (self.name))

a=restaurant("이나니","일식")
b=restaurant("기정이","한식")
c=restaurant("거농이","가나")
a.describe_restaurant("이나니","일식")
a.open_restaurant("이나니")
b.describe_restaurant("기정이","한식")
b.open_restaurant("기정이")
c.describe_restaurant("거농이","가나")
c.open_restaurant("거농이")