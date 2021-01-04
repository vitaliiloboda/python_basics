class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'Full name: {self.name} {self.surname}'

    def get_total_income(self):
        return f"Full income: {self._income['wage'] + self._income['bonus']}"


a = Position('Alex', 'Bond', 'Architect', 85, 10)
print(a.get_full_name())
print(f'Position: {a.position}')
print(a.get_total_income())

b = Position('Lilu', 'Manchester', 'Philosopher', 100, 5)
print(b.get_full_name())
print(f'Position: {b.position}')
print(b.get_total_income())
