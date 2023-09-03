class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        results = []
        for employee in self.employees:
            if employee.age == target_age:
                results.append(employee)
        return results

    def search_by_name(self, target_name):
        results = []
        for employee in self.employees:
            if employee.name == target_name:
                results.append(employee)
        return results

    def search_by_salary(self, operator, target_salary):
        results = []
        if operator == '>':
            for employee in self.employees:
                if employee.salary > target_salary:
                    results.append(employee)
        elif operator == '<':
            for employee in self.employees:
                if employee.salary < target_salary:
                    results.append(employee)
        elif operator == '>=':
            for employee in self.employees:
                if employee.salary >= target_salary:
                    results.append(employee)
        elif operator == '<=':
            for employee in self.employees:
                if employee.salary <= target_salary:
                    results.append(employee)
        return results

def main():
    database = EmployeeDatabase()

    # Add employees to the database
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Parameters:")
    print("1. Age\n2. Name\n3. Salary (>, <, <=, >=)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter target age: "))
        results = database.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter target name: ")
        results = database.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter operator (> / < / <= / >=): ")
        target_salary = int(input("Enter target salary: "))
        results = database.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if results:
        print("\nSearch Results:")
        for result in results:
            print(f"Employee ID: {result.emp_id}, Full_Name: {result.name}, Age: {result.age}, Salary: {result.salary}")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
