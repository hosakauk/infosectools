from requests import Request, Session
import sys
from concurrent.futures import ThreadPoolExecutor
    
subdomains = sys.argv[1]
host = sys.argv[2]

f = open(subdomains, 'r')
p = f.readlines()

with ThreadPoolExecutor() as threads:
    for i in p:
        i = i.strip()
        try:
            s = Session()
            s.headers.update({'Host':'{0}.{1}'.format(i,host)})
            r = s.get('http://{0}'.format(host))
            code = r.status_code
            print("%s.%s responded with status code %s" % (i,host,code))
            s.close()
        except:
            pass
