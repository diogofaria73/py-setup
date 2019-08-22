import os

def mount(comand, snap):
    return comand + snap

def clean_screan():
    return os.system('clear')