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
        action.begin_message(package)
        subprocess.call(action.mount(command, package), shell=True)
        action.end_message(package)

    #Get All curl urls and add in wget
    for curl in curls:
        command = 'curl '
        action.begin_message(package)
        subprocess.call(action.mount(command, curl), shell=True)
        action.end_message(package)

    print('All wget packages is set.')
    
    #Installing node using nvm
    for nvm in nvms:
        command = 'nvm install'
        action.begin_message(package)
        subprocess.call(action.mount(command, nvm), shell=True)
        action.end_message(package)

    print('All nvm packages is installed')

    # Get All snap itens and make installation
    for snap in snaps:
        action.begin_message(package)
        install = 'sudo snap install '
        subprocess.call(action.mount(install, snap), shell=True)
        action.end_message(package)

    print('All packages is installed.')

except:
    print('Something are wrong. Please try again later {}' .format(Exception.with_traceback))
