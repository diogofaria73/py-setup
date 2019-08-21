def packages():
   
    aptList = []

    aptList.append('update')
    aptList.append('build-essential')
    aptList.append('libssl-dev')

    return aptList

def curl():

    curList = []

    #NVM: https://www.liquidweb.com/kb/how-to-install-nvm-node-version-manager-for-node-js-on-ubuntu-12-04-lts/
    curList.append('https://raw.githubusercontent.com/creationix/nvm/v0.25.0/install.sh | bash')