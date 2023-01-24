import os


class ChainInfo:
    def __init__(self, block_explorer_url: str, websocket_url: str, alchemy_key: str):
        self.block_explorer_url = block_explorer_url
        self.websocket_url = websocket_url
        self.alchemy_key = alchemy_key


class Chain:
    Goerli = ChainInfo("https://goerli.etherscan.io/tx/",
                       "wss://eth-goerli.g.alchemy.com/v2/", os.getenv('GOERLI_ALCHEMY_KEY'))
    Polygon = ChainInfo("https://polygonscan.com/tx/",
                        "wss://polygon-mainnet.g.alchemy.com/v2/", os.getenv('POLYGON_ALCHEMY_KEY'))
    Ethereum = ChainInfo("https://etherscan.io/tx/",
                         "wss://eth-mainnet.g.alchemy.com/v2/", os.getenv('ETHEREUM_ALCHEMY_KEY'))


subscribeToChain = Chain.Polygon

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
to_phone_number = os.getenv('TWILIO_SEND_UPDATES_TO_PHONE_NUMBER')