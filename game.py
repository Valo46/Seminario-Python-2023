from random import choice, randrange
from datetime import datetime
operators = ["+", "-", "/", "*"]
times = 5
correctas = 0
init_time = datetime.now()
calculo_resuelto = 0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):

    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)


    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")

    
    result = int(input("resultado: "))
    
    
    
    match operator:
        case "+": 
            calculo_resuelto = (number_1 + number_2)
        case "-":
            calculo_resuelto = (number_1 - number_2)
        case "/":
            calculo_resuelto = (number_1 / number_2)
        case "*":
            calculo_resuelto = (number_1 * number_2)
    if result == calculo_resuelto:
        correctas = correctas + 1
        print(f'¡Correcto!')
    else:
        print(f'Mmm... No es correcto')
        
            

end_time = datetime.now()

total_time = end_time - init_time

print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Tenes {correctas} respuesta/s correcta/s")