from brownie import StandardBounties, accounts

def deploy_standard_bounties():
    account = accounts.load('prnts-deployer')
    standard_bounties = StandardBounties.deploy({"from": account}) 
    return standard_bounties


def main():
    deploy_standard_bounties()


if __name__ == "__main__":
    main()