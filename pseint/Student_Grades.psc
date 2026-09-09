Algoritmo Student_Grades
	//Get data 
	// Identify process fianlly 
	// 1st. level (Grade 1): 30%
	// 2nd. level (Grade 2): 30%
	// 3th. level (Grade 3): 40%
	//Step 1: Defin
	Definir numb1, numb2, numb3 Como Real
	nombre <- caracter
	Escribir "Enter your complete names "
	Leer nombre
	Escribir "Enter the final grade for the fist grading period."
	Leer numb1
	Escribir "Enter the final grade for the second grading period."
	Leer numb2
	Escribir "Enter the final grade for the third grading period."
	Leer numb3
	numb4 <- numb1*0.3 + numb2*0.3 + numb3*0.4
	Escribir nombre " Your final grade for the semester is " numb4
	Escribir "Grades averages is: " (numb1+numb2+numb3)/3
FinAlgoritmo