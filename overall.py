def  student_averages(my_dict):
    resultado = {}
    for student_id, notas_dict in my_dict.items():
        grades = notas_dict.values()
        nota = round(sum(grades)/len(grades))
        resultado[student_id] = nota
    return resultado
def assignment_averages(my_dict):
    sums = {}
    cuentas = {}
    for student_id, notas_dict in my_dict.items():
        for tarea, nota in notas_dict.items():
            if tarea not in sums:
                sums[tarea] = nota
                cuentas[tarea] = 1
            else:
                sums[tarea]+= nota
                cuentas[tarea]+= 1
    final_averages = {}
    for tarea in sums:
        prom = round(sums)
        final_averages[tarea] = prom
    return final_averages
if __name__ == "__main__":
    students = {
      "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
      "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
      "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
    }
    print("Promedios por Estudiante:", student_averages(students))
    print("Promedios por Tarea:", assigment_averages(students))


