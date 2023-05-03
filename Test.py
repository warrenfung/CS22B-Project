import csv
import datetime

from win10toast import ToastNotifier

def check_homework_assignments():
    with open('Project-SJSU-Courses.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        now = datetime.datetime.now()
        assignments_due = []
        for row in reader:
            due_date = datetime.datetime.strptime(row[1], '%Y-%m-%d')
            if (due_date - now).days == 0:
                assignments_due.append(row[0])
        if assignments_due:
            assignment_names = '\n '.join(assignments_due)
            toaster = ToastNotifier()
            toaster.show_toast('Upcoming homework assignment', f'{assignment_names} due today', duration=10)

check_homework_assignments()
    