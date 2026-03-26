def employee_print(employee_info):
    nombre = employee_info.pop("Name", "N/A")
    salario = employee_info.pop ("Salary", "N/A")
    rol= employee_info.pop ("Role", "N/A")
    print(f"Name: {nombre}")
    print(f"Salary: {salario}")
    print(f"Role: {rol}")
