class SalariedEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def CalculatePay(self):
        return f"{self.name} got {self.salary} as a salary"

class HourlyEmployee:
    def __init__(self, name, HourlyRate, HoursWorked):
        self.name = name
        self.HourlyRate = HourlyRate
        self.HoursWorked = HoursWorked

    def CalculatePay(self):
        return f"{self.name} got {self.HourlyRate*self.HoursWorked} as a salary"

if __name__ == '__main__':
    salary_Employee = SalariedEmployee("Sanjay", 500000)
    Hourly_Employee = HourlyEmployee("John", 10000, 8)
    print(salary_Employee.CalculatePay())
    print(Hourly_Employee.CalculatePay())
