import time
from celery import shared_task

@shared_task()
def mr_save_task(first_name):
    time.sleep(5)
    def check_mr_start(string):
        if not string.startswith('mr.'):
            return True
        return False
    def check_mr_end(string):
        if string.endswith('mr.'):
            return True
        return False
    
    fname = first_name
    fname = fname.lower()
    new_fname = ''
    if check_mr_start(fname) == True:
        new_fname = 'Mr.' + ' ' + fname
    if check_mr_end(fname) == True:
        fname = fname.replace('mr.', '')
        new_fname = 'Mr.' + ' ' + fname
    return new_fname
