# Semana 13: Cálculo del salario semanal

## Estudiante

David Alejandro Silva Zambrano

## Descripción

Este programa permite calcular el salario semanal de un trabajador. El usuario ingresa las horas trabajadas y el pago correspondiente por cada hora. La función recibe estos dos valores, realiza la multiplicación y retorna el salario total.

## Pseudocódigo

FUNCION calcularSalario(horasTrabajadas, pagoPorHora)
    salarioTotal ← horasTrabajadas * pagoPorHora
    RETORNAR salarioTotal
FIN FUNCION

INICIO
    LEER horasTrabajadas
    LEER pagoPorHora
    resultado ← calcularSalario(horasTrabajadas, pagoPorHora)
    IMPRIMIR resultado
FIN

## Ejecución

Para ejecutar el programa:

python calcular_salario.py