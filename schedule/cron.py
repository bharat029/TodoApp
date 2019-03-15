from django.utils import timezone
from .models import Schedule
import django_cron 

class SendEmail(django_cron.CronJobBase):
    RUN_EVERY_MINS = 60

    schedule = django_cron.Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        for schedule in Schedule.objects.all():
            if schedule.deadline - timezone.now() < 60:
                schedule.user.email_user(schedule.title, schedule.description, 'mydreamfutureworld@gmail.com')
