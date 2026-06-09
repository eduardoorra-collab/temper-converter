celsios1 = float(input('digite temperatura em celsios: '))

fahrenheit1 = float(input('digite a temperatura em fahrenheit: '))

celsios2 = (fahrenheit1 -32) / 1.8
fahrenheit2 = (celsios1 * 1.8) + 32

print( f"A temperatura convertida sera {fahrenheit2:.2f}ºF")
print( f"A temperatura convertida sera {celsios2:.2f}ºC")
