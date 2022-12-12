#!/usr/bin/python3
#
# Goal    : Anonymous Github API access is limited to 60 requests per hour, so if this number
#           is exceeded a 403 return code will be returned. To avoid the Pipeline failure this 
#           script will wait if the limit is exceeded.
# Author  : Andre Muzel Brisolla
# Date    : Dec 12, 2022
# Version : 0.1

# import libs
import time
import sys
import requests
from   datetime import datetime, timedelta

# This repository is used by packer to download the latest version of packer 
# plugin that will be used during the template generation.
GITHUB_API_URL = 'https://api.github.com/repos/hashicorp/packer-plugin-vsphere'

# API Request 
req = requests.get(GITHUB_API_URL)

# Set rate limit to accept as "ok"
wait_to_reset_rate_limit = 5

# get remaining requests
remaining_requests       = int(req.headers['X-RateLimit-Remaining'])

# Check if requests limit is exceeded
if remaining_requests <= wait_to_reset_rate_limit:
  date_to_reset         = datetime.fromtimestamp(int(req.headers['x-ratelimit-reset']))
  date_now              = datetime.now()
  date_diff_seconds     = abs(int((date_now - date_to_reset).total_seconds()))+2  
  print(f'Checking Github API rate limit... waiting (remaingin requests: {remaining_requests})')
  print(f'Waiting until {date_to_reset} to reset Github API rate limit')
  time.sleep(date_diff_seconds)
else:
  print(f'Checking Github API rate limit... ok (remaingin requests: {remaining_requests})')

# continue script
