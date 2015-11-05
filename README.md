# crossbrowsertesting.com-api

The CrossBrowserTesting.com (http://crossbrowsertesting.com/) API allows you to implement our browser testing services within your own web and desktop applications via HTTP, enabling you to customize your website-testing process and workflow.

The API specification can be found here:
https://crossbrowsertesting.com/apidocs/v3/screenshots

## Getting Started
1. Rename the file `\src\auth.config.example` to `\src\auth.config`.
2. Put your own CrossBrowserTesting.com credentials in the file. The file looks like this:
```
[Authentication]
username=John Doe
password=aabbccdd99ddee00
```

## Example 1
`show-tested-browser-list.py` show information about a specific screenshot result.
```
python show-tested-browser-list.py --id=822563
```
An example output would look something like this:
```
Tested Browsers: http://app.crossbrowsertesting.com/public/i4899d87d7d1546d/screenshots/z2aa7c5b82c5f3350378
# Windows 10 / Google Chrome 45
# Windows 10 / Firefox 41
# Windows 10 / Internet Explorer 11
# Windows 10 / Microsoft Edge
# Windows 10 / Opera 32
# Windows 8.1 / Google Chrome 45
# Windows 8.1 / Firefox 41
# Windows 8.1 / Internet Explorer 11
# Windows 8.1 / Opera 32
# Windows 8 / Google Chrome 45
# Windows 8 / Firefox 41
# Windows 8 / Internet Explorer 10
# Windows 8 / Opera 32
# Windows 8 / Safari 5.1
# Windows 7 64-Bit / Internet Explorer 10
# Windows 7 64-Bit / Google Chrome 45
# Windows 7 64-Bit / Firefox 41
# Windows 7 64-Bit / Internet Explorer 9 (64-bit)
# Windows 7 64-Bit / Opera 32
# Windows 7 64-Bit / Internet Explorer 11
# Windows 7 / Internet Explorer 9
# Windows 7 / Safari 5.1
# Windows 7 / Google Chrome 45
# Windows 7 / Firefox 41
# Windows 7 / Opera 32
# Windows Vista / Google Chrome 45
# Windows Vista / Firefox 41
# Windows Vista / Internet Explorer 9
# Windows Vista / Opera 32
# Windows XP SP3 / Google Chrome 45
# Windows XP SP3 / Firefox 41
# Windows XP SP3 / Opera 32
# Windows XP SP2 / Google Chrome 45
# Windows XP SP2 / Firefox 41
# Windows XP SP2 / Opera 32
# Mac OSX 10.11 / Google Chrome 45 (64-bit)
# Mac OSX 10.11 / Firefox 41
# Mac OSX 10.11 / Opera 32
# Mac OSX 10.11 / Safari 9
# Mac OSX 10.10 / Google Chrome 45 (64-bit)
# Mac OSX 10.10 / Firefox 41
# Mac OSX 10.10 / Opera 32
# Mac OSX 10.10 / Safari 8
# Mac OSX 10.9 / Google Chrome 45 (64-bit)
# Mac OSX 10.9 / Firefox 41
# Mac OSX 10.9 / Opera 32
# Mac OSX 10.9 / Safari 7
# Mac OSX 10.8 / Google Chrome 45 (64-bit)
# Mac OSX 10.8 / Firefox 41
# Mac OSX 10.8 / Opera 32
# Mac OSX 10.8 / Safari 6.2
# Mac OSX 10.6 / Google Chrome 32
# Mac OSX 10.6 / Firefox 26
# Mac OSX 10.6 / Safari 5.1
# Android Nexus 9 / 5.0 / Chrome Mobile 44
# Android Nexus 7 / 4.2 / Chrome Mobile 37
# Android Nexus 6 / 5.0 / Chrome Mobile 40
# Android Nexus 5 / 4.4 / Chrome Mobile 44
# Android Galaxy Note 3 / 4.4 / Chrome Mobile 44
# Android Galaxy S5 / 4.4 / Chrome Mobile 35
# Android Galaxy S3 / 4.1 / Chrome Mobile 34
# Android Galaxy Tab 2 / 4.1 / Chrome Mobile 38
# iPad Air / 8.1 Simulator / Mobile Safari 8.0
# iPad Mini Retina / 7.1 Simulator / Mobile Safari 7.0
# iPad 3 / 6.1 Simulator / Mobile Safari 6.0
# iPhone 6 Plus / 8.1 Simulator / Mobile Safari 8.0
# iPhone 6 / 8.1 Simulator / Mobile Safari 8.0
# iPhone 5s / 7.1 Simulator / Mobile Safari 7.0
```
