class car:
    color=""
    model=""
    year=""
    brand=""
    noOfOwners=0
    regNo=""
    area=""
    def __init__(self, color, model,year,brand,noOfOwners,regNo,area):
        self.color=color
        self.model=model
        self.year=year
        self.brand=brand
        self.noOfOwners=noOfOwners
        self.regNo=regNo
        self.area=area

    def displayMyCar(self):
        print("\n",self.color,"\n",self.model,"\n",self.year,"\n",self.brand,"\n",self.noOfOwners,"\n",self.regNo,"\n",self.area)

MyCar=car("Red","Sedan","2018","BMW","10","TS07","miyapur")
MyCar.displayMyCar()
colorOfMyCar=MyCar.color
MyCar.color="green"
print(MyCar.color)

    
