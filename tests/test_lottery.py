from brownie import Lottery, accounts, config, network
from web3 import Web3
import pytest

# expectation 0,0031 ETH = 10 USD


def approx(expectation, percentage):
    print(f"[ TEST ] Appr. Wei: {expectation * (1 + percentage)}")
    return expectation * (1 + percentage)


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )

    expected_low = approx(Web3.toWei(0.0031, "ether"), -0.025)
    expected_high = approx(Web3.toWei(0.0031, "ether"), 0.025)

    actual = lottery.getEntranceFee()
    assert actual > expected_low
    assert actual <= expected_high
