list_a = ['first_name','last_name','role']
list_b= ['Aaron', 'Lopez', 'Software Engineer']

employee_dict = {}
count=0
for i in list_a:
    employee_dict[f'{list_a[count]}']=f'{list_b[count]}'
    count=count+1

print(employee_dict)