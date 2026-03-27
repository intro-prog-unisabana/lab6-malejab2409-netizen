def employee_print(employee_info):
    nombre = employee_info.get("Name", "N/A")
    salario = employee_info.get ("Salary", "N/A")
    rol= employee_info.get ("Role", "N/A")
    print(f"Name: {nombre}")
    print(f"Salary: {salario}")
    print(f"Role: {rol}")
    dato_extra = employee_info.copy()
    dato_extra.pop("Name", None)
    dato_extra.pop("Salary", None)
    dato_extra.pop("Role", None)
    if len(dato_extra) == 0:
        print("No other info!")
    else:
        for key, value in dato_extra.items():
            print(f"{key}: {value}")    
employee_info = {
     "Name": "Diego",
     "Salary": 5000000,
     "Role": "Janitor",
     "Years at company": 9001,
     "Hours per week": 2
 }
employee_print(employee_info)