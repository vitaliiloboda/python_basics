class WareHouse:
    transfers = []
    printers = {}
    scanners = {}
    xeroxes = {}
    types = {1: 'printer', 2: 'scanner', 3: 'xerox', 4: 'stop'}

    def __init__(self, square, floors, warehouse_class):
        self.square = square
        self.floors = floors
        self.warehouse_class = warehouse_class  # A+, A, B+, B, C, D

    def transfer(self, equipment):
        for k, item in enumerate(equipment.keys(), 1):
            print(f'#{k}: {item}, в количестве: {equipment.get(item)}')

        item = int(input('Выберите номер оборудование, которое нужно передать: '))
        number = int(input('Какое количество этого оборудования нужно передать: '))
        division = input('Укажите подразделение компании, куда передать оборудование: ')

        if equipment.get(list(equipment.keys())[item - 1]) <= 1 or equipment.get(
                list(equipment.keys())[item - 1]) - number < 1:
            equipment.pop(list(equipment.keys())[item - 1])
        else:
            equipment.update(
                {list(equipment.keys())[item - 1]: equipment.get(list(equipment.keys())[item - 1]) - 1})

        if number > equipment.get(list(equipment.keys())[item - 1]):
            print(
                f'На складе было только {equipment.get(list(equipment.keys())[item - 1])} устройств. '
                f'Если необходимо передать еще, выберите дургие устройства')
            number = equipment.get(list(equipment.keys())[item - 1])

        self.transfers.append(
            f'{list(equipment.keys())[item - 1]} в количестве {number} было передано в подразделение {division}')

        print(f'{list(equipment.keys())[item - 1]} в количестве {number} было передано в подразделение {division}')

    def equipment_reception(self):
        purposes = {1: 'office', 2: 'home'}
        yes_no = {0: False, 1: True}
        sizes = {1: 'A3', 2: 'A4'}
        i = 0

        while True:

            try:
                type = self.types.get(int(input(
                    'Отправка оборудования на склад. Для завершения отправки нажмите - 4. '
                    'Выберите тип устройства: 1 - принтер, 2 - сканер, 3 - ксерокс: ')))
            except ValueError:
                print('Выберите 1, 2, 3 или 4')
                continue

            if type == 'stop':
                break

            elif type not in self.types.values():
                print('Выберите 1, 2, 3 или 4')
                continue

            while i != 1:
                try:
                    amount = int(input('Введите количесто отправляемых устройств: '))
                    i = 1
                except ValueError:
                    continue
            model = input('Введите название модели: ')
            purpose = purposes.get(int(input(
                'Выберите назначение устройства: 1 - office, 2 - home: ')))

            if type == 'printer':
                colors_number = int(input('Введите количество цветов (от 1 до 8): '))
                print_photo = yes_no.get(
                    int(input('Введите 1, если фукнция печати фото присутствует, 0 - если отсутствует: ')))

                if Printer(model, purpose, colors_number, print_photo).specification in self.printers.keys():
                    self.printers.update(
                        {Printer(model, purpose, colors_number, print_photo).specification: self.printers.get(
                            Printer(model, purpose, colors_number, print_photo).specification) + amount})
                else:
                    self.printers.update({Printer(model, purpose, colors_number, print_photo).specification: amount})

            elif type == 'scanner':
                size_format = sizes.get(
                    int(input('Выберите максимальный размер сканирования. Введите 1 для А3, 2 для А4: ')))
                resolution = f'{int(input("Укажите максимальное разрешение сканирования (от 400 до 6400): "))}dpi'

                if Scanner(model, purpose, size_format, resolution).specification in self.scanners.keys():
                    self.scanners.update(
                        {Scanner(model, purpose, size_format, resolution).specification: self.scanners.get(
                            Scanner(model, purpose, size_format, resolution).specification) + amount})
                else:
                    self.scanners.update({Scanner(model, purpose, size_format, resolution).specification: amount})

            elif type == 'xerox':
                colors_number = int(input('Введите количество цветов (от 1 до 8): '))
                usb = yes_no.get(
                    int(input('Введите 1 если возможна печать с usb носителя, 0 - если если такой возможности нет: ')))

                if Xerox(model, purpose, colors_number, usb).specification in self.xeroxes.keys():
                    self.xeroxes.update(
                        {Xerox(model, purpose, colors_number, usb).specification: self.xeroxes.get(
                            Xerox(model, purpose, colors_number, usb).specification) + amount})
                else:
                    self.xeroxes.update({Xerox(model, purpose, colors_number, usb).specification: amount})

    def transfer_equipment(self):
        while True:
            try:
                type = self.types.get(int(input(
                    'Передача оборудования со склада. Для завершения отправки нажмите - 4. '
                    'Выберите тип устройства: 1 - принтер, 2 - сканер, 3 - ксерокс: ')))
            except ValueError:
                print('Выберите 1, 2, 3 или 4')
                continue

            if type == 'stop':
                break

            elif type not in self.types.values():
                print('Выберите 1, 2, 3 или 4')
                continue

            if type == 'printer':
                self.transfer(self.printers)

            elif type == 'scanner':
                self.transfer(self.scanners)

            elif type == 'xerox':
                self.transfer(self.xeroxes)


class OfficeEquipment:

    def __init__(self, model, purpose):
        self.purpose = purpose  # назначение: офис/дом
        self.model = model


class Printer(OfficeEquipment):
    name = 'printer'

    def __init__(self, model, purpose, colors_number, print_photo):
        self.model = model
        self.purpose = purpose
        self.colors_number = colors_number
        self.print_photo = print_photo
        self.specification = f'модель - {self.model}, назначение - {self.purpose}, ' \
                             f'количество цветов - {self.colors_number}, фотопечать - {self.print_photo}'

    @staticmethod
    def print_page():
        print('Printed')


class Scanner(OfficeEquipment):
    name = 'scanner'

    def __init__(self, model, purpose, size_format, resolution):
        self.model = model
        self.purpose = purpose
        self.size_format = size_format
        self.resolution = resolution
        self.specification = f'модель: {self.model}, назначение: {self.purpose}, ' \
                             f'максимальный размер сканирования: {self.size_format}, максимальное разрешение: {self.resolution}'

    @staticmethod
    def scan_page():
        print('Scanned')


class Xerox(OfficeEquipment):
    name = 'Xerox'

    def __init__(self, model, purpose, colors_number, usb):
        self.model = model
        self.purpose = purpose
        self.colors_number = colors_number
        self.usb = usb
        self.specification = f'модель: {self.model}, назначение: {self.purpose}, ' \
                             f'количество цветов: {self.colors_number}, печать с usb носителя: {self.usb}'

    @staticmethod
    def copy_page():
        print('Copied')


warehouse = WareHouse(400, 2, 'A')

# warehouse.printers = {'модель - 1, назначение - office, количество цветов - 3, фотопечать - True': 2,
#                       'модель - 2, назначение - office, количество цветов - 1, фотопечать - True': 2,
#                       'модель - 1, назначение - office, количество цветов - 1, фотопечать - True': 4,
#                       'модель - 5, назначение - office, количество цветов - 2, фотопечать - True': 1}
#
# warehouse.scanners = {
#     'модель - 1, назначение - office, кмаксимальный размер сканирования - A3, максимальное разрешение - 400': 2,
#     'модель - 2, назначение - office, максимальный размер сканирования - A3, максимальное разрешение - 600': 2,
#     'модель - 1, назначение - office, максимальный размер сканирования - A3, максимальное разрешение - 800': 4,
#     'модель - 5, назначение - office, максимальный размер сканирования - A4, максимальное разрешение - 1000': 1}
#
# warehouse.xeroxes = {'модель: FF28, назначение: office, количество цветов: 5, печать с usb носителя: False': 4,
#                      'модель: FF8, назначение: home, количество цветов: 5, печать с usb носителя: True': 8,
#                      'модель: FF41, назначение: office, количество цветов: 5, печать с usb носителя: False': 1,
#                      'модель: FF47, назначение: home, количество цветов: 5, печать с usb носителя: False': 2,
#                      'модель: FF1, назначение: home, количество цветов: 5, печать с usb носителя: True': 5, }

warehouse.equipment_reception()
warehouse.transfer_equipment()
