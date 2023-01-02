import random


def GenerateDataForPolynomial(extent):

    myDistionary = {}

    for i in range(0, extent + 1):
        coeff = random.randint(-100, 100)

        if coeff == 0:
            continue

        myDistionary[i] = coeff

    return myDistionary


def GetPolynomial(dataForPolynomial):

    items = sorted(dataForPolynomial.items(), key=lambda x: x[0])
    sortedDataForPolynomial = dict(items)

    myList = []

    for key in sortedDataForPolynomial:
        coeff = sortedDataForPolynomial[key]
        coeffText = ''
        x = ''
        element = ''
        multiplication = ''

        if abs(coeff) != 1 or (key == 0 and abs(coeff) == 1):
            coeffText = str(abs(coeff))

        if coeff < 0:
            coeffText = ' - ' + coeffText
        else:
            coeffText = ' + ' + coeffText

        if abs(coeff) != 1:
            multiplication = "*"

        if key == 1:
            x = f'{multiplication}x'
        elif key > 1:
            x = f'{multiplication}x**' + str(key)

        element = coeffText + x
        myList.insert(0, element)

    myList[0] = myList[0].replace(' ', '').replace('+', '')

    sign = ''
    return sign.join(myList) + ' = 0'


def GetAmountPolynomialData(data1, data2):
    myDictionary = {}
    sum = 0
    for key in data1:
        sum = data1.get(key) + data2.get(key, 0)
        if sum != 0:
            myDictionary[key] = sum

    for key in data2:
        if data1.get(key, None) == None and data2.get(key) != 0:
            myDictionary[key] = data2.get(key)

    return myDictionary


def GetDataPolynomial(polynomialString):
    clearString = polynomialString.replace(' ', '').replace(
        '=0', '').replace('**', '^').lower()
    splitByPlus = clearString.split('+')
    myDistionary = {}
    for i in range(0, len(splitByPlus)):
        splitByMinus = splitByPlus[i].split('-')
        for j in range(0, len(splitByMinus)):
            if splitByMinus[j] == '':
                continue

            coeff = 1
            if j != 0:
                coeff *= -1

            splitByMulti = splitByMinus[j].split('*')
            if splitByMulti[0][0] != 'x':
                coeff *= int(splitByMulti[0])

            splitByExt = splitByMinus[j].split('^')
            ext = 0
            if len(splitByExt) > 1:
                ext = int(splitByExt[1])
            if 'x' in splitByExt[0] and len(splitByExt) == 1:
                ext = 1

            myDistionary[ext] = coeff

    return myDistionary


def SaveToFile(text, fileName='polynomial.txt'):
    file = open(fileName, 'w')
    try:
        file.write(text)
    finally:
        file.close()


def RedalineFromFile(fileName):
    file = open(fileName, 'r')
    try:
        string = file.readline()
    finally:
        file.close()
    return string


extent = int(input("Введите натуральное число: "))

# генерируем многочлен
polynomial = GetPolynomial(GenerateDataForPolynomial(extent))
# записываем в файл
SaveToFile(polynomial)

# создаем два файла с данными для пункта B
polynomial = GetPolynomial(GenerateDataForPolynomial(extent))
SaveToFile(polynomial, 'polynomial1.txt')

polynomial = GetPolynomial(GenerateDataForPolynomial(extent))
SaveToFile(polynomial, 'polynomial2.txt')

# считываем данные из файлов
polynomial1 = RedalineFromFile('polynomial1.txt')
polynomial2 = RedalineFromFile('polynomial2.txt')

# получаем сумму
amountData = GetAmountPolynomialData(GetDataPolynomial(
    polynomial1), GetDataPolynomial(polynomial2))

# из итоговых данных формируем многочлен
amountPolynomial = GetPolynomial(amountData)

# пишем в файл
SaveToFile(amountPolynomial, 'polynomialAmount.txt')
