from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    ordering = 'group'
    students = Student.objects.order_by(ordering).prefetch_related('teacher').values('id', 'name', 'group',
                                                                                     'teacher__name',
                                                                                     'teacher__subject')

    object_list = []
    ids = []  # вспомогательный списко

    for student in students:
        if student['id'] not in ids:

            ids.append(student['id'])

            object_list.append({
                'id': student['id'],
                'name': student['name'],
                'group': student['group'],
                'teachers': [{'name': student['teacher__name'], 'subject': student['teacher__subject']}],
            }
            )

        else:
            for element in object_list:
                if element['id'] == student['id']:
                    element['teachers'].append(
                        {'name': student['teacher__name'], 'subject': student['teacher__subject']}
                    )

    context = {
        'object_list': object_list
    }

    print(context)

    return render(request, template, context)
