import os
import subprocess
import sources.snap as snap
import utils.command as command

try:
    # Get definied list and install all packages
    for snap in snap.hasInstalled(snap.packages()):
        install = 'sudo snap install '
        subprocess.call(command.mount(install, snap), shell=True)

except:
    print('Something are wrong. Please try again later')

