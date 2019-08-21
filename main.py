import os
import subprocess
import sources.snap as snap
import sources.apt as apt
import utils.command as command

try:
    
    #Get All apt packages and make installation
    for apt in apt.packages():
        install = 'sudo apt install'
        subprocess.call(command.mount(install, apt), shell=True)
    
    print('All aptitude packages is installed.')
    
    #Get All curl urls and add in wget
    for url in apt.curl():
        curl = 'curl '
        subprocess.call(command.mount(curl, url))

    print('All wget packages is set.')
    
    # Get All snap itens and make installation
    for snap in snap.packages():
    
        install = 'sudo snap install '
        subprocess.call(command.mount(install, snap), shell=True)

    print('All packages is installed.')


except:
    print('Something are wrong. Please try again later')

