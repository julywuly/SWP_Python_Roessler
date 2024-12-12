class Company:

    def __init__(self) -> None:
        self.departments = []

    # Alle Mitarbeiter
    def total_employees(self):
        return sum(len(department.employees) for department in self.departments)

    # Alle Abteilungsleiter
    def total_department_heads(self):
        return len([
            employee for department in self.departments for employee in department.employees
            if isinstance(employee, DepartmentHead)
        ])

    # Alle Abteilungen
    def total_departments(self):
        return len(self.departments)

    # größte Abteilung
    def department_with_max_employees(self):
        return max(self.departments, key=lambda department: len(department.employees))

    # Frauenanteil
    def percent_women(self):
        women_count = len([
            employee for department in self.departments for employee in department.employees if employee.gender
        ])
        total_employees = self.total_employees()
        return f"{(women_count * 100 / total_employees):.2f}" if total_employees > 0 else 0  # Division durch 0 vermeiden


class Department:

    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def total_employees(self):
        return len(self.employees)

    def add_employee(self, employee):
        if isinstance(employee, DepartmentHead):
            if any(isinstance(emp, DepartmentHead) for emp in self.employees):  # Pro Abteilung ein Vorstand
                raise Exception("A department can only have one head.")
        self.employees.append(employee)


class Person:

    def __init__(self, name: str, is_female: bool) -> None:
        self.name = name
        self.gender = is_female  # True = Frau, False = Mann


class Employee(Person):

    def __init__(self, name: str, is_female: bool) -> None:
        super(Employee, self).__init__(name, is_female)


class DepartmentHead(Employee):

    def __init__(self, name: str, is_female: bool) -> None:
        super(DepartmentHead, self).__init__(name, is_female)


if __name__ == '__main__':
    company = Company()

    # Abteilung Sales
    sales_department = Department("Sales")
    sales_department.add_employee(DepartmentHead("John Doe", False))
    sales_department.add_employee(Employee("Jane Smith", True))
    sales_department.add_employee(Employee("Emily Davis", True))
    sales_department.add_employee(Employee("Michael Brown", False))
    sales_department.add_employee(Employee("Anna White", True))
    company.departments.append(sales_department)

    # Abteilung IT
    it_department = Department("IT")
    it_department.add_employee(DepartmentHead("Chris Green", False))
    it_department.add_employee(Employee("Laura Adams", True))
    it_department.add_employee(Employee("James Clark", False))
    it_department.add_employee(Employee("Sarah Wilson", True))
    it_department.add_employee(Employee("Mark Lewis", False))
    it_department.add_employee(Employee("Sophia Hall", True))
    company.departments.append(it_department)

    # Statistik
    print("Total employees:", company.total_employees())
    print("Total department heads:", company.total_department_heads())
    print("Total departments:", company.total_departments())
    print("Department with the most employees:", len(company.department_with_max_employees().employees))
    print("Percentage of women in the company:", company.percent_women(), "%")
