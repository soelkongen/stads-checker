# AAU Stads Checker
## Usage
Python script that will inform you if there is updates on your Stads site. It uses IFTTT and Webhooks to give you push notifications on your phone. It should give you a notification within second

## Setup
### IFTTT and Webhooks
*"If This Then That, also known as IFTTT is a free web-based service to create chains of simple conditional statements, called applets. An applet is triggered by changes that occur within other web services such as Gmail, Facebook, Telegram, Instagram, or Pinterest. For example, an applet may send an e-mail message if the user tweets using a hashtag, or copy a photo on Facebook to a user's archive if someone tags a user in a photo."*  


Start downloading the IFTTT app in App Store/Google Play and create an account. Afterwards it's easier to create the applet and get your Webhook key on a PC. Go to www.ifttt.com, login with your credentials. Click on your accounts image in the top right and 'Create'. Click on the '+' button and search/choose Webhooks. Choose 'Recevice a web request'. Give the event a name, like Stads (it does'nt matter) and Crate trigger. Now for the action: Click on the black '+' button. If you want it to give you a notification, you can search notification. Choose 'Send a notification from the IFTTT app'. Now you can make your own message. There are some ingredients you can choose: Value1: AAU module name. Value2: Grade. Value3: ECTS.  
You can use this standard:  
```
Your Stads has been updated with a new entry: {{Value1}}, the grade is {{Value2}} and has {{Value3}} ECTS credits
```
When you're done hit 'Create action' and 'Finish'. Your applet is ready for action.

### Find Webhooks key and test applet
To find your key go to https://ifttt.com/maker_webhooks and click on 'Documentation' in the top right corner. Here can you find your Webhooks key. You will need this in the server configuration later. You can test your applet if you fill out {event} with your eventname you created. The values is optional in this test. When you're ready, hit 'Test It'. You should get a notification on your phone. 


### Server configuration with YAML 
Start by installing the dependencies
```
pip install pyyaml bs4 requests
```
Then you should update the config.yaml file with your credentials, Webhook key, searchwords etc.  
When you're ready start the main script
```
python main.python
```
