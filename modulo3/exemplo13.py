import time as tt

class Timer:
    
    def __init__(self ,horas,minutos,segundos ):
        self.h = horas
        self.m=minutos
        self.s=segundos
       
    def __str__(self):
       #return 'Memo={0}, Tag={1}'.format(self.memo, self.tags)
       
       return "{0}:{1}:{2}".format(self.h,self.m,self.s)
    
        
    def next_second(self):
        self.s=int(self.s)
        self.m=int(self.m)
        self.h=int(self.h)
        
        self.s +=1
        
        if self.s ==60:
            self.s='00'
            self.m+=1

            if self.m ==60:
                self.m='00'
                self.h +=1
                if self.h==24:
                    self.h='00'
                
            

    def prev_second(self):

        self.s=int(self.s)
        self.m=int(self.m)
        self.h=int(self.h)

        self.s -=1
        if self.s ==-1:
            self.s='59'
            self.m-=1

            if self.m ==-1:
                self.m='59'
                self.h -=1
                if self.h==-1:
                    self.h='23'


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
print(">")
for i in range (10):
    timer.next_second()
    tt.sleep(1)
    print(timer)