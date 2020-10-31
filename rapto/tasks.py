from celery import task 
from celery import shared_task 
from rapto.models import Courses
# from django.db.models import Courses


@shared_task 
def delete_expired_courses():
    print('checking expired courses')
    C = Courses.objects.all()
    for c in C:
        if c.No_Of_Days <= 1:
            c.delete()
            print('deleted expired courses')
        else:
            c.No_Of_Days-=1
            c.save()
            print('reduced date by one')
    print('Here I\’m')
    # Another tricker