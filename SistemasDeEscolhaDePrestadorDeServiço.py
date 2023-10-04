#Matheus Anthony Pereira Abreu 
#Matrícula : 2023008792

from abc import ABC, abstractmethod

class EmpDomestic(ABC):
    def __init__(self,name,telephone):
        self._name = name
        self._telephone = telephone

    @property
    def name(self):
        return self._name
    
    @property
    def telephone(self):
        return self._telephone
    
    @name.setter
    def name(self,name):
        self._name=name

    @telephone.setter
    def telephone(self,telephone):
        self._telephone=telephone

    @abstractmethod 
    def getSalary():
        pass

class hourly(EmpDomestic):
    def __init__(self, name, telephone,hoursWorked,priceHour):
        self._hoursWorked=hoursWorked
        self._priceHour=priceHour
        super().__init__(name, telephone)
   
    @property
    def hoursWorked(self):
        return self._hoursWorked
    
    @property
    def priceHour(self):
        return self._priceHour
    
    @hoursWorked.setter
    def hoursWorked(self,hoursWorked):
        self._hoursWorked=hoursWorked

    @priceHour.setter
    def priceHour(self,priceHour):
        self._priceHour=priceHour

    def getSalary(self):
        return self._hoursWorked*self._priceHour 
    
class diarist(EmpDomestic):
    def __init__(self, name, telephone,dayWorked,priceDay):
        self._dayWorked = dayWorked
        self.priceDay = priceDay
        super().__init__(name, telephone,)
    
    @property
    def dayWorked(self):
        return self._dayWorked
    
    @property
    def priceDay(self):
        return self._priceDay
    
    @dayWorked.setter
    def dayWorked(self,dayWorked):
        self._dayWorked=dayWorked
    
    @priceDay.setter
    def priceDay(self,priceDay):
        self._priceDay=priceDay

    def getSalary(self):
        return self._priceDay*self._dayWorked

class Mensalist(EmpDomestic):
    def __init__(self, name, telephone,priceMonth):
        self._priceMonth = priceMonth
        super().__init__(name, telephone)
    
    @property
    def priceMonth(self):
        return self._priceMonth
    
    @priceMonth.setter
    def priceMonth(self,priceMonth):
        self._priceMonth=priceMonth

    def getSalary(self):
        return self._priceMonth
    
if __name__=="__main__":
    
    Emp1= hourly("Carla", "(12)9888-8888",160,12)
    Emp2= diarist("Naiara","(21)9883-3333",20,65)
    Emp3= Mensalist("Marisa","(31)9666-666",1200)
    Emps=[Emp1,Emp2,Emp3]

    bestEmp=Emp1

    for Emp in Emps:
        if(bestEmp.getSalary()>Emp.getSalary()):
            bestEmp=Emp
    for Emp in Emps:
        print('Nome: {} , Telefone: {} , Salario: {} '.format(Emp.name, Emp.telephone, Emp.getSalary()))
    
    print("Melhor empregada : ")
    print("Nome: {} , Telefone: {} , Salario: {} ".format(bestEmp.name,bestEmp.telephone,bestEmp.getSalary()))