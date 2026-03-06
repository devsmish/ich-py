'''1. Система управления кассовыми чеками
Главные действующие лица и исполнители:
`Shift` — это смена (или кассир)
`Receipts:` — это чеки, пробитые за конкретную смену 
(без смены чеков не бывает!)
Чек может быть:
обычным (`SaleReceipt`):
id: номер чека
amount: сумма чека
возвратным (`ReturnReceipt` — делается на основе обычного чека):
id: номер чека
amount: сумма чека
id_source_shift: № смены в которую был пробит обычный чек
1.1 Класс Receipt
Создайте класс Receipt, представляющий чек.
● Каждый чек должен иметь ID и сумму.
● Метод __str__() должен возвращать строку формата: Receipt <ID>: <amount>'''
class Receipt:
    def __init__(self, receipt_id, amount):
        self.receipt_id = receipt_id
        self.amount = amount

    def __str__(self):
        return f'Receipt {self.receipt_id}: {self.amount}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.receipt_id!r}: {self.amount!r})'

'''1.2 Класс Shift
Создайте класс Shift, представляющий кассовую смену.
● У каждой смены уникальный ID (нумерация с 1.
● У смены есть:
○ список чеков
○ статус (открыта или закрыта)
● Реализуйте методы:
○ is_closed() — возвращает закрыта ли смена
○ close() — закрывает смену
○ get_total() — возвращает сумму всех чеков
○ list_receipts() — выводит список чеков через print()'''
class Shift:
    id_count = 0
    def __init__(self):
        Shift.id_count += 1
        self.id = Shift.id_count
        self.receipts = list()
        self.closed = False

    def is_closed(self):
        return self.closed

    def close(self):
        self.closed = True

    def get_total(self):
        return sum(receipt.amount for receipt in self.receipts)

    def list_receipts(self):
        for receipt in self.receipts:
            print(f'Смена: {self.id} - {receipt}')

    def __str__(self):
        return f'Итог по чекам: \n\t{self.receipts}'

    def add_receipt(self, amount):
        if self.closed:
            raise ValueError("Смена закрыта! Чеки добавлять нельзя!")
        receipt_id = len(self.receipts) + 1
        new_receipt = Receipt(receipt_id, amount)
        self.receipts.append(new_receipt)

    def add_return(self, original_id, return_amount):
        if not (0 < original_id <= len(self.receipts)):
            raise ValueError("Чек продажи не найден!")
        original_receipt = self.receipts[original_id - 1]
        if return_amount > original_receipt.amount:
            raise ValueError("Сумма для возврата превышает сумму найденного чека!")
        receipt_id = len(self.receipts) + 1
        new_receipt = Receipt(receipt_id, -return_amount)
        self.receipts.append(new_receipt)

smena = Shift()
smena.receipts.append(Receipt(1, 70))
smena.receipts.append(Receipt(2, 52))
print(smena.get_total())
smena.list_receipts()
print(smena)

'''1.3 Добавление чеков
Доработайте Shift, чтобы чеки создавались только через смену.
● Метод add_receipt():
○ Создаёт объект Receipt с уникальным ID
○ Сохраняет его внутри текущей смены
● Если смена закрыта — выбрасывается ValueError
Проверьте работу метода, создав несколько чеков внутри смены.'''
# string 64 - 69
smena.add_receipt(43)
smena.add_receipt(16)
print(smena.get_total())
smena.list_receipts()
smena.close()
try:
    smena.add_receipt(10)
except ValueError as err:
    print(err)

'''1.4 Возврат по чеку
Доработайте Shift:
● Добавьте метод add_return(shift, original_id, return_amount), который:
○ Принимает объект смены (в которой была покупка), ID исходного чека и сумму возврата
○ Проверяет, что в переданной смене существует чек с таким ID
○ Убеждается, что сумма возврата не превышает сумму этого чека
○ Создаёт новый чек с отрицательной суммой
○ Добавляет его в текущую смену, как и обычные чеки'''
# string 71 - 79
try:
    smena.add_return(1, 9)
    smena.add_return(2, 100)
except ValueError as err:
    print(err)

smena.list_receipts()

'''1.5 Классы SaleReceipt и ReturnReceipt
Доработайте систему чеков, добавив наследование от базового класса Receipt:
● При создании SaleReceipt проверяйте, что сумма положительная
● При создании ReturnReceipt проверяйте, что сумма отрицательная Если сумма нарушает правило
(например, отрицательная в SaleReceipt), выбрасывается ValueError.
Добавьте метод __str__(), возвращающий строку в формате:
<ReceiptClass> <ID>: +<amount>
<ReceiptClass> <ID>: -<amount>
1.6 Обновление Shift для работы с подклассами чеков
Доработайте класс Shift:
● Метод add_receipt(amount) должен создавать объекты класса SaleReceipt
● Метод add_return(original_id, return_amount) — объекты класса ReturnReceipt
Доработайте методы:
● Метод list_receipts(receipt_type=None) — возвращает список всех чеков:
○ Если receipt_type=None — список всех чеков
○ Если receipt_type="sale" — только чеки продаж (SaleReceipt)
○ Если receipt_type="return" — только возвраты (ReturnReceipt)
● Метод get_total(receipt_type=None) — возвращает сумму:
○ Всех чеков, если receipt_type=None
○ Только продаж, если receipt_type="sale"
○ Только возвратов, если receipt_type="return"
1.7 Проверка всей системы
Проверьте работу всей логики:
● Создайте смену и добавьте 2 чека на продажу
● Создайте вторую смену и выполните возврат по одному из чеков первой
● Отобразите списки и суммы всех чеков по типам
● Убедитесь, что возврат нельзя выполнить с неверной суммой
Пример вывода:
SaleReceipt 1: +100
SaleReceipt 2: +200
ReturnReceipt 1: -50
Total sales: 300
Total returns: -50
Total: 250'''

'''2. Пользователи и уведомления
2.1 Система уведомлений
Создайте три класса, каждый из которых добавляет поддержку одного канала связи:
● EmailNotifyMixin — требует наличие поля email и реализует метод email_notify(message)
● SmsNotifyMixin — требует наличие поля phone и реализует метод sms_notify(message)
● PushNotifyMixin — реализует метод push_notify(message) и не требует дополнительных полей
Если обязательного поля нет, выбрасывайте AttributeError.
2.2 Получатели уведомлений
Создайте базовый класс User, представляющий пользователя с name.
На его основе реализуйте два типа пользователей:
● Courier — дополнительно принимает email и phone, поддерживает email и SMS уведомления
● Admin — поддерживает только push-уведомления
Каждый класс должен иметь метод notify(message), который вызывает все доступные типы уведомлений. При
реализации наследуйте классы, соответствующие типам уведомлений.
Пример вывода:
Email to alice@example.com: Package delivered.
SMS to +123456789: Package delivered.
Push notification: New report available.'''