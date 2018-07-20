class car:
    color=""
    model=""
    year=""
    brand=""
    noOfOwners=0
    def __init__(self, color, model,year,brand,noOfOwners):
        self.color=color
        self.model=model
        self.year=year
        self.brand=brand
        self.noOfOwners=noOfOwners
    def displayMyCar(self):
        print("\n",self.color,"\n",self.model,"\n",self.year,"\n",self.brand,"\n",self.noOfOwners)

MyCar=car("Red","Sedan","2018","Rolls Royace","10")
MyCar.displayMyCar()

    