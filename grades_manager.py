def initialize_dict(student_name, subject_grades):
    student = {
        student_name: subject_grades
    }
    return student
def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    nombre = input("Enter student name: ")
    nombree = nombre.strip().title()
    materias = {} 
    while True:
        entrada = input("Enter subject and grade (or 'exit' to finish): ")
        if entrada.lower() == 'exit':
            break       
        if "," in entrada:
            parte = entrada.split(",")
            materia = parte[0].strip().title() 
            nota = float(parte[1].strip())
            materias[materia] = nota
    new_student_data = initialize_dict(nombree, materias)
    student_grades.update(new_student_data) 
    print(f"Student {nombree} successfully added to the grades management system.")
    return student_grades
def get_students(student_grades, keys):
    encontrados = {}  
    for nombre_buscado in keys:
        nombre_formateado = nombre_buscado.strip().title()   
        if nombre_formateado in student_grades:
            encontrados[nombre_formateado] = student_grades[nombre_formateado]
        else:
            print(f"{nombre_formateado} not found!")      
    return encontrados
def avg_by_student(student_grades, keys=None):
    if keys is None:
        estudiantes_objetivo = student_grades
    else:
        estudiantes_objetivo = get_students(student_grades, keys)
    for nombre_est, sus_materias in estudiantes_objetivo.items():
        if len(sus_materias) > 0:
            notas_solo = sus_materias.values()
            promedio = sum(notas_solo) / len(notas_solo)
            print(f"{nombre_est}: {round(promedio, 1)}")
if __name__ == "__main__":
    pass