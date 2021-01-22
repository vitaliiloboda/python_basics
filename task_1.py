class Date:

    def __init__(self, any_date):
        self.date = any_date

    @classmethod
    def set_date(cls, day, month, year):
        try:
            day = int(day)
            month = int(month)
            year = int(year)

            str_date = f'{day}-{month}-{year}'
            cls.validation(day, month)
            return cls(str_date)

        except (ValueError):
            print('Only whole numbers are allowed.We have set a default date for you: 01-01-2000')
            return cls('01-01-2000')

    @staticmethod
    def validation(day, month):
        if day > 31 or day < 1:
            print('Your date is invalid. Enter a day from 1 to 31')
        elif month > 12 or month < 1:
            print('Your date is invalid. Enter a month from 1 to 12')


date = Date.set_date(1, 11, 2020)
print(date.date)
