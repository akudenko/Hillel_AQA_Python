# Создать классы Employee (сотрудник) и Company (компания).
#
# Классы должны содержать:
# минимум два поля экземпляров и одно поле класса
# минимум два метода экземпляра
# минимум один метод класса
# минимум один статический метод
# К методам добавить строки документации.
#
# Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
# Написать код который создает несколько экземпляров и взаимодействует с объектами
# Задание в том числе и на фантазию

class Company:

    count_of_companies = 0
    updated_companies = 0

    def __init__(self, company_name, working_area, address, contact_phone, url, date_of_creation, employees):
        self.company_name = company_name
        self.working_area = working_area
        self.address = address
        self.contact_phone = contact_phone
        self.url = url
        self.date_of_creation = date_of_creation
        self.employees = employees
        Company.count_of_companies += 1

    """Get info about a company"""
    def get_info(self):
        print(self.company_name, self.working_area, self.address, self.contact_phone, self.url, self.date_of_creation, self.employees)

    """Update company info"""
    def update_info(self, company_name, working_area, address, contact_phone, url, date_of_creation, employees):
        self.company_name = company_name
        self.working_area = working_area
        self.address = address
        self.contact_phone = contact_phone
        self.url = url
        self.date_of_creation = date_of_creation
        self.employees = employees
        Company.updated_companies += 1

    """Count of companies"""
    @staticmethod
    def display_count_of_companies():
        print(f'Count of companies is: {Company.count_of_companies}')

    @classmethod
    def display_count_of_updated_companies(cls):
        print(f'Count of updated companies is: {Company.updated_companies}')


soft_serve = Company('Soft Serve', 'IT', 'Ukraine, Lviv', '+380953999999', 'https://www.soft-serve.com', '10-10-2010', 30000)
epicentr = Company('Epicentr', 'E-Commerce/Offline purchasing', 'Ukraine, Kiev', '+380953999999', 'https://www.epicentr/com', '07-12-2003', 400000)
english_dom = Company('English Dom', 'Education', 'Ukraine, Kiev', '+380953999999', 'https://www.english-dom.com', '10-10-2017', 1500)

soft_serve.get_info()
epicentr.get_info()
english_dom.get_info()

english_dom.update_info('English Dom', 'Education', 'Ukraine, Kiev', '+380953999999', 'https://www.english-dom.com', '10-10-2017', 1251)
english_dom.get_info()

Company.display_count_of_companies()
Company.display_count_of_updated_companies()


class Employee:
    default_salary = 3000
    count_employees = 0

    def __init__(self, first_name, last_name, age, month_in_company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.month_in_company = month_in_company
        Employee.count_employees += 1

    def get_employee_info(self):
        print(self.first_name, self.last_name, self.age, self.month_in_company)

    """Checking the state of an employee to increase salary"""
    def check_salary_review(self):
        years = self.month_in_company / 12

        if self.month_in_company >= 12:
            print('It\'s time for a review')
            self.default_salary = 400 * years + self.default_salary
            print(f'New salary is: {self.default_salary}')
        else:
            print('Not enough time in a company for the review')

    """Checking the probation period of an employee"""
    @staticmethod
    def is_probation_period(month_in_company):
        if month_in_company >= 3:
            return True
        else:
            return False

    """Count of employees"""
    @classmethod
    def display_count_of_employees(cls):
        print(f'Count of employees in a company: {Employee.count_employees}')


employee1 = Employee("John", "Doe", 34, 2)
employee2 = Employee("Alex", "Smith", 28, 24)
employee3 = Employee("Kris", "Pratt", 42, 12)

print(employee1, employee2, employee3)
employee1.get_employee_info()
employee2.get_employee_info()
employee3.get_employee_info()

print(Employee.is_probation_period(employee1.month_in_company))
Employee.display_count_of_employees()

employee1.check_salary_review()
employee3.check_salary_review()
employee2.check_salary_review()
