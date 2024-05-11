from django.shortcuts import render
from static.files.supplymethods import *


# A: Valor de la primera cuota de la serie
# i: Tasa de interes de la operacion
# n: Numero de pagos o ingresos
# G: Constante en que aumenta cada cuota


# SOLO PARA GRADIENTE ARITMETICO
def calculateQuota(A, n, G):
    quotaValue = A+(n-1)*G
    return quotaValue

def calculateAnnualityValue(G, i, n):
    annualityBaseForm = G*((1/i)-(n/((1+i)**n)-1))
    return annualityBaseForm

def calculatePresentValue(A, n, i, G):
    presentValueForm = A*((((1+i)**n)-1)/(i*((1+i)**n)))+(G/i)*(((((1+i)**n)-1)/(i*((1+i)**n)))-((n)/((1+i)**n)))
    return presentValueForm

def calculeFutureValue(A, G, i, n):
    futureValueForm = A*((((1+i)**n)-1)/i)+(G/i)*(((((1+i)**n)-1)/i)-(n))
    return futureValueForm

# 1. CALCULO DEL GRADIENTE ARITMETICO
def calculate_arithmethic_gradient(request):
    result = {}
    if request.method == 'POST':
        try:
            # valor futuro (F)
            futureValue = float(request.POST['value1'])
            # valor presente (P)
            presentValue = float(request.POST['value2'])
            # valor base o anualidad (A)
            annualityValue = float(request.POST['value3'])
            # tasa de interes % (i)
            taxRateValue = float(request.POST['value4'])
            # tipo de tasa de interes
            taxTypeValue = request.POST.get('value5')
            # tipo de capitalizacion
            capTypeValue = request.POST.get('value6')
            # numero de flujos (n)
            nNumberValue = float(request.POST['value7'])
            # cuota a calcular (n)
            quotaValue = float(request.POST['value8'])
            # variacion constante (G)
            constantVarValue = float(request.POST['value9'])
            
            # transformando interes a decimal
            taxRateValue = convertPercentageToDecimal(taxRateValue)
                 
            # verificando si la tasa es anual mensual etc...
            if (taxTypeValue == "no_anu"):
                taxRateValue = calculateAnualTaxRate(taxRateValue)
            
            valueCalculate = ""
            
            # result here...
            if(presentValue == 0):
                result = calculatePresentValue(A=annualityValue, n=nNumberValue, i=taxRateValue, G=constantVarValue)
                valueCalculate = "presente"
            
            if(futureValue == 0):
                result = calculeFutureValue(A=annualityValue,G=constantVarValue,i=taxRateValue,n=nNumberValue)
                valueCalculate = "futuro"
                
            if(annualityValue == 0):
                result = calculateAnnualityValue(G=constantVarValue, i=taxRateValue, n=nNumberValue)
                valueCalculate = "del primer pago"
                
            result = round(result, 2)
            result = divideByRange(result)
            result = "El valor " + valueCalculate +" es: " + str(result) + " $"
            
            if (quotaValue != 0):
                value = result + ", La cuota deseada a calcular es: " + str(calculateQuota(A=annualityValue, n=quotaValue, G=constantVarValue)) + " $"
                result = value
                
            
        except Exception as e:
            result['error'] = "Ocurrió un error: " + str(e)
        return render(request, 'result.html', {'result': result})
    return render(request, "second_unit/subpages3/operation1.html")


# AMORTIZACION 

""" 
Valor del prestamo (M o C): 50.000$
Tiempo (n): 6 años
Interes (i): 16%
Acumular: 700.000
Cantidad a depositar para acumular el dinero (R)
"""

def calculateAmortization(vp, n, tasa, time):
    # Convertir la tasa nominal anual a efectiva periódica
    j = tasa / time
    
    # Calcular la cuota de amortización de capital
    vk = vp / n
    
    # Inicializar listas para almacenar los datos de la tabla de amortización
    periodos = []
    cuota_capital = []
    interes = []
    saldo_capital = []
    pago = []
    
    saldo_anterior = vp
    
    # Calcular la amortización para cada periodo
    for periodo in range(1, n + 1):
        # Calcular el interés del periodo
        i = saldo_anterior * j
        
        # Calcular el pago total del periodo (cuota de capital + interés)
        ak = vk + i
        
        # Calcular el nuevo saldo de capital
        saldo_actual = saldo_anterior - vk
        
        # Almacenar los datos en las listas
        periodos.append(periodo)
        cuota_capital.append(vk)
        interes.append(i)
        saldo_capital.append(saldo_actual)
        pago.append(ak)
        
        # Actualizar el saldo anterior para el siguiente periodo
        saldo_anterior = saldo_actual
    
    # Crear la tabla de amortización como una lista de tuplas
    tabla_amortizacion = list(zip(periodos, cuota_capital, interes, saldo_capital, pago))
    
    return tabla_amortizacion

def calculateAmortization(R, i, n):
    print("TODO")

# Este metodo calcula R el cual es el primer abono

def calculateMonthlyPayment(C, i, n):
    valueReturn = C/((1-((1+i)**(-n)))/(i))
    return valueReturn