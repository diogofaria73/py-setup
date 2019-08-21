import os
import subprocess


def packages():

    snapList = []
    snapList.append('snapd')
    snapList.append('snapcraft --classic')
    snapList.append('node --classic')
    snapList.append('spotify')
    snapList.append('discord')
    snapList.append('slack --classic')
    snapList.append('telegram-desktop')
    snapList.append('--classic code')
    snapList.append('postman')
    snapList.append('htop')

    return snapList
