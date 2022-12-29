class WeekDayError(Exception):
    pass
	

class Weeker:
    lista=['Mon', 'Thu' ,'Wed' ,'Thu', 'Fri' ,'Sat','Sun']
    #
    # Write code here
    #

    def __init__(self, day):
        self.valor=False
        #self.l=self.lista
        for i in range(len(self.lista)):
            if day ==self.lista[i]:
                self.day=day
                break
            else :
                self.valor=True
        if self.valor==True:
            print("Valor inserido invalido")
    
    def __str__(self):
        return "{0}".format(self.day)
    
    def add_days(self, n):
        self.n=n
        tam = len(self.lista)
        rem=n%tam
        self.day=self.lista[rem]
    def subtract_days(self, n):
        tam = len(self.lista)
        r=(-n+1)%tam
        self.day=self.lista[r]

        
    

            
                
       



weekday = Weeker('Mon')
print(weekday)
weekday.add_days(15)
print(weekday)


weekday.subtract_days(23)
print(weekday)