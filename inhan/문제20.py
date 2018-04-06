class Restaurant:
    def __init__(self,name):
        self.name = name
    def star_Restaurant(self,star):
        print("저희 레스토랑은 미슐랭 스타 %d개 레스토랑입니다." % star)
    def traditional_Restaurant(self, years):
        print("저희 레스토랑은 %d년의 정통을 가지고 있습니다." % years)
    def customer_Restaurant(self, people):
        print("저희 레스토랑은 %s명의 손님을 한번에 받을 수 있습니다." % people)

class inania(Restaurant):
    def type_(self, type):
        print ("저희 레스토랑은 %s 전문점입니다." % type)
    def event(self, event):
        print ("저희 레스토랑 매주 수요일 %s 공연을 합니다." % event)

class inanib(Restaurant):
    def type_(self, type):
        print ("저희 레스토랑은 %s 전문점입니다." % type)
    def event(self, event):
        print ("저희 레스토랑 매주 수요일 %s 공연을 합니다." % event)

inani = Restaurant("이나니")
inan = inania()
inans = inanib()
inani.star_Restaurant(3)
inani.traditional_Restaurant(132)
inani.customer_Restaurant(18)
inan.type_("철판요리")
inanib.type_("스테이크")
inania.event("라이브")
inanib.event("k-pop")