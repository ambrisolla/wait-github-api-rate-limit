# wait-github-api-rate-limit
Anonymous Github API access is limited to 60 requests per hour, so if this number is exceeded a 403 return code will be returned. To avoid the Pipeline failure this script will wait if the limit is exceeded.

# Example of rate limit exceeded
<img src='ss.png' />
