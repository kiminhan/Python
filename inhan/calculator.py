a=0
b=0
c=0
d=0
e=0

class Calculator:
    def __init__(self,cal):
        self.cal = cal
        cal = a+b+c+d+e
    def sum(self):
        result = self.cal[0]+self.cal[1]+self.cal[2]+self.cal[3]+self.cal[4]
        print(result)
    def avg(self):
        result1 = (self.cal[0]+self.cal[1]+self.cal[2]+self.cal[3]+self.cal[4])/5
        print(result1)

if __name__ =="__main__":
    cal1 = Calculator([1,2,3,4,5])
    cal1.sum()
    cal1.avg()

    cal2 = Calculator([6,7,8,9,10])
    cal2.sum()
    cal2.avg()