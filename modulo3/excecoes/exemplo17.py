class Ex (Exception):
    def __init__(self,mesg):
        Exception.__init__(self,msg+msg)
        self.args =(msg,)


try:
    raise Ex('ex')
    print("entrou")
except Ex as e:
    print("executou?",e) 
except Exception as e :
    print(".",e)     