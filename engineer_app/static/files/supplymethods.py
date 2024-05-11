from datetime import datetime

errorMessage = "An Error ocurred: "

def toDateTimeString(dateString):
    try:
        fecha_str = dateString
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        return fecha
    except Exception as e:
        print(errorMessage, e)
        return None
    
def divideByRange(number):
    int_part, decimal_part = str(number).split('.')
    int_part_formatted = "{:,}".format(int(int_part))
    return int_part_formatted + ('.' + decimal_part if decimal_part else '')

def calculateAnualTaxRate(taxRate):
    try:
        taxRate = taxRate/12
        print("La tasa de interes: ", taxRate)
        return taxRate
    except Exception as e:
        print(errorMessage, e)
        return None

def returnDaysBetweenDates(initialDate, finalDate):
    try:
        difference = finalDate - initialDate
        days = difference.days
        return days
    except Exception as e:
        print(errorMessage, e)
        return None
    
def fractureDaysToYears(days):
    try:
        returnValue = days/365
        return returnValue
    except Exception as e:
        print(errorMessage, e)
        return None

def validateField(value):
    try:
        if (value == "" or value == None):
            return False
        return True
    except Exception as e:
        return False

def convertPercentageToDecimal(value):
    try:
        valueToReturn = value/100
        return valueToReturn
    except Exception as e:
        print(errorMessage, e)
        return None