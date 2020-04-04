#!/usr/bin/python3


import os
from datetime import datetime
from crontab import CronTab


def schedule_job(cron,comment):
    
    job = cron.new(command='cd son/x/dropbox-file-upload && python app.py >> a.txt',comment='dateinfo')
    job.minute.every(1)
    cron.write()

def update_job(cron):

    for job in cron:
        if job.comment == 'dateinfo':
            job.hour.every(10)
            cron.write()
    print('Cron job modified successfully')

def remove_job(cron):

    for job in cron:
        if job.comment == 'dateinfo':
            cron.remove(job)
            cron.write()

def main():
    user_name=input('username of your system : ')

    my_cron=CronTab(user=user_name)
    comment=input('comment of the job : ')

    schedule_job(my_cron,comment)




if __name__=='__main__':
    main()
    
