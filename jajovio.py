import requests 
import json
import sys

API_USER_ID = ''
API_SECRET = ''

def get_access_token():
    params = {
        'grant_type':'client_credentials',
        'client_id':API_USER_ID,
        'client_secret': API_SECRET
    }

    res = requests.post('https://app.snov.io/oauth/access_token', data=params)
    resText = res.text.encode('ascii','ignore')


    return json.loads(resText)['access_token']

def get_domain_search(domain):
    token = get_access_token()
    params = {'access_token':token,
            'domain':domain,
              'type': 'all',
              'limit': 100
    }

    res = requests.post('https://app.snov.io/restapi/get-domain-emails-with-info', data=params)

    return json.loads(res.text)

if len(sys.argv) < 2:
    print "usage: python jajovio.py domainsearch"
    sys.exit(0)

domainsearch = sys.argv[1]
result = get_domain_search(domainsearch)

if "errors" in result:
    print "Error :"+str(result["errors"][0]["error_description"])
    sys.exit(0)

print "Mail for "+domainsearch+" :"

file = open(domainsearch.replace('.', '_')+".txt","w")

count = 0

print result

for current in result["emails"]:
    print '\033[1;32m[+] \033[1;m'+current["email"]
    file.write(current["email"]+"\n")
    count+=1

file.close()

print '\033[1;34m[+] '+str(count)+' emails found\033[1;m'


















































#c est pas important mais bon -> #https://www.youtube.com/watch?v=SQoA_wjmE9w
