# How to set up a NiFi flow to stream tweets and perform sentiment analysis.

![full2](https://user-images.githubusercontent.com/20378758/41842909-b5714548-7889-11e8-9bdc-56c31561a694.jpg)

Inside the GetTweetJson processor group:
![full](https://user-images.githubusercontent.com/20378758/41842481-8fb41bec-7888-11e8-8870-2d63bb181f32.jpg)

Configure the GetTwitter Processor with the Consumer Key, Consumer Secret, Access Token, and Acess Token Secret. Get yours from https://developer.twitter.com :
![twitter2](https://user-images.githubusercontent.com/20378758/41843252-adae4738-788a-11e8-9f81-ae6f4e595af4.jpg)

Route on the following attributes:
![json3](https://user-images.githubusercontent.com/20378758/41843401-1535110c-788b-11e8-9e55-fb75bc9c3bb2.jpg)

The execute script processor will have the following configuration:
![last](https://user-images.githubusercontent.com/20378758/41843501-4b07c162-788b-11e8-819e-14dbf350c9dc.jpg)

The bash script and the python script for the same are in the 'script' folder.

The final database as viewed by phpMyAdmin is:
![sql](https://user-images.githubusercontent.com/20378758/41844007-912c3c08-788c-11e8-80e9-0f5e80aa315d.jpg)


Note: While running the whole process I found that, the python script had to be kept in the site-packages directory of the installed python for it to execute correctly. This may be a problem associated with NiFi's environment settings.

