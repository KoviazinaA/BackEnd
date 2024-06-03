# BackEnd
Some of my BackEnd Projects from Tuto

- [ ] Login/Registration :https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/

# Slack file upload NEW README
## Overview:
This script helps to upload one file in the channel on SLack. It uses Slack API's `files.getUploadURLExternal` and `files.completeUploadExternal`, these functions are the replacement for initial `files.upload`.

Using Slack API, this script will get a URL, upload a file by making a POST request to this URL and share within channel.

## Requirements:

* Python 3.x

* os, sys, slack_sdk, requests.

* Internet connectivity to access the Slack API and upload file.

## Usage:

Ensure Python and required libraries are installed.
Set up a Slack bot,  this script requires  `files:write` `files:read`scopes.
Run the script : `python upload_one.py file_name channel_id slack_bot_token`
Where:
1. file_name        - the correct path to the file you want to upload
2. channel_id       - the ID of channel in your Slack application where you'd like your file to appear
3. slack_bot_token  - the token of your Slack bot in the form xoxb-xxxxxxx-xxxxxxx-xxxxxxx

## Errors:
** Missing arguments ** - the number of given arguments is less then 3, you should give exactly 3 arguments: file_name, channel_id, slack_bot_token.
