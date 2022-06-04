from brownie import MusicNFT, accounts

def deploy_livepeer_nft():
    account = accounts.load('prnts-deployer')
    livepeer_nft = MusicNFT.deploy({"from": account}) 
    return livepeer_nft


def main():
    deploy_livepeer_nft()


if __name__ == "__main__":
    main()