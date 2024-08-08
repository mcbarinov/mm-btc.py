import pytest


@pytest.fixture()
def mnemonic() -> str:
    return "hub blur cliff taste afraid master game milk nest change blame code"


@pytest.fixture
def passphrase() -> str:
    return "my-secret"


@pytest.fixture()
def mainnet_bip44_address_0() -> str:
    return "1Men3kiujJH7H5NXyKpFtWWtni1cTfSk48"


@pytest.fixture
def binance_address() -> str:
    return "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo"
