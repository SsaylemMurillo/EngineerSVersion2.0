from django.shortcuts import render
from static.files.supplymethods import *

# INTERES SIMPLE
# 1. CALCULO DE MONTO/VALOR FUTURO
def calculate_capital_value(request):
    result = {}
    if request.method == 'POST':
        try:
            # capital
            capitalValue = float(request.POST['value1'])
            # porcentaje de interes
            itPercentage = float(request.POST['value2'])
            # tipo de tasa de interes
            taxType = request.POST.get('value3')
            # fecha inicial
            initialDate = request.POST['value4']
            # fecha final
            finalDate = request.POST['value5']
            
            # transformando fechas de str a datetime
            initialDate = toDateTimeString(initialDate)
            finalDate = toDateTimeString(finalDate)
            
            print(taxType)
            
            # transformando interes a decimal
            itPercentage = convertPercentageToDecimal(itPercentage)
            # obteniendo la diferencia en dias
            time = returnDaysBetweenDates(initialDate=initialDate, finalDate=finalDate)
            time = fractureDaysToYears(time)
            
            # verificando si la tasa es anual mensual etc...
            if (taxType == "anu"):
                itPercentage = calculateAnualTaxRate(itPercentage)
            
            # result here...
            
            result = capitalValue*(1+(itPercentage)*time)
            
            result = round(result, 2)
            result = divideByRange(result)
            result = str(result) + " $"
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, "first_unit/subpages1/operation1.html")