import os
import subprocess
import sources.packages as py_manager

try:
    print('We are reading the repositories list')
    
    for snap in py_manager.snap():
    
         print('Executing: {}' .format(snap))
         subprocess.call(snap, shell=True)
         print('Installation executed successfully')
         
except:
    print('Something are wrong. Please try again later')
        
