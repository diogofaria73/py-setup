def packages():
   
    aptList = []

    aptList.append('update')
    aptList.append('install build-essential')
    aptList.append('install libssl-dev')

    return aptList

def curl():

    curList = []

    curList.append('https://raw.githubusercontent.com/creationix/nvm/v0.25.0/install.sh | bash')

    return curList

def nvm():

    return 'nvm install node'