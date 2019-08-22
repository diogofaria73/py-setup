import os
import subprocess
import sources.snap as snap
import sources.aptitude as apt
import utils.action as action

try:

    packages = apt.packages()
    curls = apt.curl()
    nvms = apt.nvm()
    snaps = snap.packages()

    action.clean_screan()

    #Get All apt packages and make installation
    for package in packages:
        command = 'sudo apt '
        subprocess.call(action.mount(command, package), shell=True)

    print('All aptitude packages is installed.')

    action.clean_screan()
    #Get All curl urls and add in wget
    for curl in curls:
        command = 'curl '
        subprocess.call(action.mount(command, curl), shell=True)

    print('All wget packages is set.')
    
    action.clean_screan()
    #Installing node using nvm
    for nvm in nvms:
        command = 'nvm install'
        subprocess.call(action.mount(command, nvm), shell=True)

    print('All nvm packages is installed')

    # Get All snap itens and make installation
    action.clean_screan()
    for snap in snaps:
        install = 'sudo snap install '
        subprocess.call(action.mount(install, snap), shell=True)

    print('All packages is installed.')

except:
    print('Something are wrong. Please try again later {}' .format(Exception.with_traceback))
