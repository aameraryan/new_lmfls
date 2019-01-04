import csv
from datetime import datetime
from portal.models import Employee, Date, Attendance, ValueModel
errors = 0
emp_added = 0
for row in csv.DictReader(open('feb-18-csv.csv', 'r')):
    for col in row:
        name = row.get('Name')
        if col == 'Name':
            print('Employee -->>>', name, ' : ', col, '-', row[col])
        else:
            try:
                emp = Employee.objects.get_or_create(Name=name)[0]
                date_format = datetime.strptime(col.strip(), '%m/%d/%Y')
                date = Date.objects.get_or_create(My_Date=date_format)[0]
                att = Attendance.objects.create(Date=date, Value=(ValueModel.objects.get_or_create(Point=float(row[col]))[0]), User=emp)
                print(att.Value)
                att.User.save()
                print(att)
            except:
                errors += 1
                print(errors, '----------------------------------------------->>>', name, ' : ', col, '-', row[col])