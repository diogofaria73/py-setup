def snap():
    
    snap_list = []

    snap_list.append('sudo apt install snapd')
    snap_list.append('sudo snap install snapcraft --classic')
    snap_list.append('sudo snap install node --classic')
    snap_list.append('sudo snap install spotify')
    snap_list.append('sudo snap install discord')
    snap_list.append('sudo snap install slack --classic')
    snap_list.append('sudo snap install telegram-desktop')
    snap_list.append('sudo snap install --classic code')
    snap_list.append('sudo snap install postman')
    snap_list.append('sudo snap install htop')
    
    return snap_list
