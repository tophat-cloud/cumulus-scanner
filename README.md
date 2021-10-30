

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

# Cumulus Scanner

Web weakness scanner for [cumulus](https://cumulus.tophat.cloud).

also can use as CLI scanner like nikto, sqlmap.

## Get Started
### Install Chrome
If you have already chrome skip this part
```
#install chrome 95.0.4638.54
#cumulus scanner use chromedriver ver 95.0.4638.17
https://support.google.com/chrome/answer/95346?hl=ko&co=GENIE.Platform%3DDesktop
```
### Installation 
Give the chromedriver the executive authority according to your os.
Chromedriver is in cumulus-scanner/thunder_mushroom folder
```
chmod 555 chromedriver_mac64
chmod 555 chromedriver_mac_m1
chmod 555 chromedriver_linux
```

```
git clone https://github.com/tophat-cloud/cumulus-scanner.git
cd cumulus-scanner
pip3 install -r requirements.txt
cd thunder_mushroom
```

cumulus-scanner works out of the box with Python version 3.x on any platform.
### Run

```
python3 mushroom_test.py -u example.com -o a
```

## Usage

```
    -u, --url # set scan target url
    
    -o --options # set all module or single module
        - a # use all scanner module
        - c # use check unnecessary comment module
        - d # use directory traversal module
        - g # use guessing moduele
        - f # use find unobfuscated code module
```
    
## Types of weakness that can be found
- Unnecessary Comment
- Directory Traversal
- Guessing
- Unobfuscated Code

## Contents
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
