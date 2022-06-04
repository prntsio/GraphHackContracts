'''
REQUIRED TESTS:

Spotify (SF):
- Test artist follower number returned successfully

Instagram (IG):
- Test user follower number returned successfully 

Smart contracts:
- Bounty with requirements for 100 IG/ SF followers fails to assign when artist has <100 followers
- Bounty with requirements for 100 IG/ SF followers successfully assigns when artist has >100 followers

Copied from StandardBounties:
  Verifies that I can issue a bounty paying in ETH without locking up funds 
  Verifies that I can issue a bounty paying in ETH while locking up funds 
  Verifies that I can't issue a bounty contributing more than the deposit amount 
  Verifies that I can't issue a bounty contributing less than the deposit amount 
  Verifies that I can contribute to a bounty in ETH 
  Verifies that I can't contribute to a bounty which is out of bounds 
  Verifies that I can't contribute to a bounty and send less than the deposit amount 
  Verifies that contributing emits an event 
  Verifies that I can refund a contribution in ETH 
  Verifies that I can't refund a contribution to a bounty which is out of bounds 
  Verifies that I can't refund a contribution which is out of bounds 
  Verifies that I can't refund a contribution which isn't mine 
  Verifies that I can't refund a contribution which has already been refunded 
  Verifies that I can't refund a contribution before the deadline has elapsed 
  Verifies that refunding a contribution emits an event 
  Verifies that I can refund all of my contributions 
  Verifies that I can't refund contributions if one of them isn't mine 
  Verifies that I can refund a set of contributions as an issuer 
  Verifies that I can't refund contributions if I'm not an issuer 
  Verifies that I can't refund contributions for an invalid bounty 
  Verifies that I can't refund contributions with an out of bounds contribution ID 
  Verifies that I can't refund contributions when one of them has been refunded already 
  Verifies that refunding several contributions emits an event 
  Verifies that I can drain my bounty 
  Verifies that I can drain a bounty as a 2nd issuer 
  Verifies that I can't drain someone else's bounty 
  Verifies that I can't drain a bounty without passing in an array of correct length 
  Verifies that I can't drain a bounty of more funds than its balance 
  Verifies that draining a bounty emits an event 
  Verifies that I can perform an action for a bounty 
  Verifies that I can't perform an action for an out of bounds bounty 
  Verifies that performing an action emits an event 
  Verifies that I can fulfill a bounty 
  Verifies that I can't fulfill an out of bounds bounty 
  Verifies that I can't fulfill a bounty after the deadline has elapsed 
  Verifies that I can't fulfill a bounty with 0 fulfillers 
  Verifies that fulfilling a bounty emits an event 
  Verifies that I can update a fulfillment 
  Verifies that I can't update a fulfillment for an out of bounds bounty 
  Verifies that I can't update an out of bounds fulfillment 
  Verifies that I can't update a fulfillment which was submitted by someone else 
  Verifies that updating a fulfillment emits an event 
  Verifies that I can accept a fulfillment as an issuer 
  Verifies that I can accept a fulfillment paying different amounts to different fulfillers 
  Verifies that I can accept a fulfillment as an approver 
  Verifies that I can't accept a fulfillment on an out of bounds bounty 
  Verifies that I can't accept a fulfillment which is out of bounds 
  Verifies that I can't accept a fulfillment if I'm not an approver 
  Verifies that I can't accept a fulfillment by passing in the wrong number of token amounts corresponding to the number of fulfillers 
  Verifies that I can't accept a fulfillment paying out more than the balance of my bounty 
  Verifies that accepting a fulfillment emits an event 
  Verifies that I can fulfill and accept a bounty simultaneously 
  Verifies that I can change all of a bounty's info 
  Verifies that I can't change an out of bounds bounty 
  Verifies that I can't change a bounty if I'm not an issuer' 
  Verifies that I can change the issuer of my bounty 
  Verifies that I can't change the issuer of an out of bounds bounty 
  Verifies that I can't change the issuer of a bounty if I didn't issue it 
  Verifies that I can't the issuer with an out of bounds issuer ID 
  Verifies that I can't the issuer changing an out of bounds issuer ID 
  Verifies that changing a bounty's issuer emits an event 
  Verifies that I can change the approver of my bounty 
  Verifies that I can't change the approver of an out of bounds bounty 
  Verifies that I can't change the approver of a bounty if I didn't issue it 
  Verifies that I can't the issuer with an out of bounds issuer ID 
  Verifies that I can't the issuer changing an out of bounds approver ID 
  Verifies that changing a bounty's approver emits an event 
  Verifies that I can change the data of my bounty 
  Verifies that I can't change the data of an out of bounds bounty 
  Verifies that I can't change the data of a bounty if I didn't issue it 
  Verifies that I can't change the data with an out of bounds issuer ID 
  Verifies that changing a bounty's data emits an event 
  Verifies that I can change the deadline of my bounty 
  Verifies that I can't change the deadline of an out of bounds bounty 
  Verifies that I can't change the deadline of a bounty if I didn't issue it 
  Verifies that I can't change the deadline with an out of bounds issuer ID 
  Verifies that changing a bounty's deadline emits an event 
  Verifies that I can add issuers to my bounty 
  Verifies that I can't add issuers to an out of bounds bounty 
  Verifies that I can't add issuers to a bounty if I didn't issue it 
  Verifies that I can't add issuers with an out of bounds issuer ID 
  Verifies that adding issuers to a bounty emits an event 
  Verifies that I can add approvers to my bounty 
  Verifies that I can't add approvers to an out of bounds bounty 
  Verifies that I can't add approvers to a bounty if I didn't issue it 
  Verifies that I can't add approvers with an out of bounds issuer ID 
  Verifies that adding approvers to a bounty emits an event 
  Verifies that I can't accept a fulfillment, and still try to refund everyone's contributions 
  Verifies that I can accept a fulfillment, and still try to refund some contributions 
  Verifies that I can refund a contribution, and still drain the remaining funds 
  Verifies that I can't refund a contribution, and still drain all of the funds 

'''
from brownie import accounts
from scripts.deploy_standard_bounties import deploy_standard_bounties

'''
Not sure why, but when trying to declare standard_bounties = deploy_standard_bounties() as global, the imported script fails to execute with an error related to accounts
'''

def test_create_bounty():
  # Arrange
  standard_bounties = deploy_standard_bounties() # ContractTx
  #contract_owner = accounts[0]
  sender = accounts[0] # this should normally be msg.sender in the contract unless coming through meta tx relayer
  issuers = [accounts[0], accounts[3]]
  approvers = [accounts[0], accounts[2]]
  data = "QmNnWrwfAbsnWvyTgGpaYLdh1oAkBR5B74MjwZh8stTL97" # need an example IPFS hash here; this is an NFT hash currently
  deadline = "1654045200" # May 31st, 2022 at 18:00 UTC
  token = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48" # using USDC; not sure this is needed when using ETH
  token_version = "20" # 0 for ETH, 20 for ERC20, 721 for ERC721'
  bounty_id = 0
  print(f"Output from deployment: {standard_bounties}")


  # Act - check that we can issue a bounty
  tx = standard_bounties.issueBounty(sender, issuers, approvers, data, deadline, token, token_version, {"from": sender}) # TransactionReceipt
  tx.wait(1)

  # Assert - check that bounty is set up correctly
  assert tx.return_value == bounty_id, "Bounty ID is incorrect"
  assert tx.sender == sender, "Sender is incorrect"

  # Act 
  tx_get_bounty = standard_bounties.getBounty(bounty_id, {"from": accounts[5]}) # TransactionReceipt
  #tx_get_bounty.wait(1)

  # Assert - get resulting bounty
  #assert simple_storage.getNumber() == expected
  print(f"Output from getBounty: {tx_get_bounty}")
  #assert tx_get_bounty.return_value == bounty_id, "Bounty ID is correct"


def test_issue_and_contribute():
  pass 


def test_contribute():
  pass 


def test_refund_contribution():
  pass


def test_refund_contribution():
  pass 


def test_refund_my_contributions():
  pass 


def test_refund_my_contributions():
  pass 


def test_drain_bounty():
  pass


def test_perform_action():
  pass


def test_fulfill_bounty():
  pass


def test_update_fulfillment():
  pass


def test_accept_fulfillment():
  pass


def test_fulfill_and_accept():
  pass


def test_change_bounty():
  pass


def test_change_issuer():
  pass


def test_change_approver():
  pass


def test_change_issuer_and_approver():
  pass


def test_change_data():
  pass


def test_change_deadline():
  pass


def test_add_issuers():
  pass


def test_add_approvers():
  pass


def test_get_bounty():
  pass


def test_transfer_tokens():
  pass
