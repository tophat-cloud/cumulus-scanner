

<p align="center">
  <p align="center">
    <a href="https://cumulus.tophat.cloud" target="_blank">
      <img src="https://jinui.s3.ap-northeast-2.amazonaws.com/tophat/logo.png" alt="Sentry" height="72">
    </a>
  </p>
  <p align="center">
    Application Weakness Monitoring Software
  </p>
</p>

# Cumulus Scanner for Python3

The official Cumulus Scanner for python3

## Environment
    Ubuntu 20.04
    Python3.8
## Installation

Run normally:

```
#install chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo apt-get update
sudo apt-get install google-chrome-stable

git clone https://github.com/tophat-cloud/cumulus-scanner.git
pip3 install -r requirements.txt
cd cumulus-scanner/thunder_mushroom
python3 mushroom_test.py -u example.com -o a
```
## Types of weakness that can be found
- Check Unnecessary Comment
- Directory Travelser
- Guessing admin page
- Find obfuscation java script

## Contents
- [Cumulus Dashboard](https://cumulus.tophat.cloud/)
- [Contributing](https://github.com/tophat-cloud/cumulus-scanner/blob/master/CONTRIBUTING.md)

## Author
<p align="center">
  <p align="center">
    <a href="https://github.com/tophat-cloud" target="_blank">
      <img src="https://jinui.s3.ap-northeast-2.amazonaws.com/tophat/tophat.png" alt="TopHat" height="100">
    </a>
  </p>

  <p align="center">
    <a href="http://github.com/lookuss" target="_blank">@lookuss</a>&nbsp from <strong>TopHat</strong>
  </p>
</p>
