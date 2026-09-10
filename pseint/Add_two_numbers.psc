Algoritmo Add_two_numbers
	Definir numb1, numb2 Como Entero
	Escribir "Please enter N1"
	leer numb1 
	Escribir "Please enter N2"
	leer numb2
	Escribir "The addition is " numb1+numb2
	Escribir "The substraction is " numb1-numb2
	Escribir "The multiplication is " numb1*numb2
	Si numb2 = 0 Entonces
		Escribir "It is not possible to divide or remove the module by zero."
	sino 
		Escribir "The division is " numb1/numb2
		Escribir "The residue is " numb1 MOD numb2
	FinSi
FinAlgoritmo