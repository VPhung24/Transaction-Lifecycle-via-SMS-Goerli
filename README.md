## Transaction Lifecycle via SMS from Goerli

This is working off of [Alchemy's](https://www.alchemy.com/) [Transaction-Lifecycle-via-SMS](https://github.com/alchemyplatform/Transaction-Lifecycle-via-SMS) repo, an example to show how "your dApp can integrate the power of Alchemy's Enhanced API suite"

Since the repo's last update, Rinkeby has been depricated. Currently this repo enabales users to choose between `Goerli`, `Polygon`, and `Eth` for pending tranactions.

### Geting Started

#### Virtual Environment

- `python3 -m venv venv` create virtual env folder (run once)
- `. venv/bin/activate` enter virtual env
- `deactivate` leave virtual env

#### APIs (create an `.env` in the home directory. .env.example is an example)

- [Twilio SMS](https://www.twilio.com/): Account SID, Auth Token, Twilio Phone Number
- [Alchemy](https://www.alchemy.com/): API Key
  - [Alchemy's Goerli faucet](https://goerlifaucet.com/): 0.2 Goerli ETH every 24h

### (currently hardcoded) Chain to get notifed pending transactions from (options Goerli, Polygon, Ethereum)

- change `subscribeToChain` in `helper.py` to wanted chain

### Test and Run Locally

- `foreman start`
- On macOS, if running into error "Port 5000 is in use by another program", try turning off Airplay Reciever (System Preferences -> Sharing -> AirPlay Receiver)

### Deploy on Heroku

- `heroku create`
- `git add .`
- `git commit -m "<comment>"`
- `git push heroku main`
