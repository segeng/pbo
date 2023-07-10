class employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class salaryemployee(employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
    
class HourlyEmployee(employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
    
class commissionEmployee(salaryemployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
    
class manager(salaryemployee):
    def work(self, hours):
        print(f'{self.name} bekerja untuk{hours} hours.')

class secretary(salaryemployee):
    def work(self, hours):
        print(f'{self.name} menghabiskan{hours} hours untuk komunikasi.')

class factoryworker(salaryemployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for{hours} hours.')
    
    