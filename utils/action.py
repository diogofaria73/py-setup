import os

def mount(comand, snap):
    return comand + snap

def clean_screan():
    return os.system('clear')

def begin_message(item):
    print('##########################################################################')
    print('{} package ' .format(item))

def end_message(item):
    print('{} was successfull ' .format(item))