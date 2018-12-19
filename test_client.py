import sys
import time
import requests

def main():
    if len(sys.argv) != 2:
        print('Usage: test_client.py <ALB endpoint>')
        sys.exit(1)

    endpoint = sys.argv[1]
    s = requests.Session()

    start = time.time()
    while True:
        print (time.time() - start)
        r = s.get('http://%s/ping_wait' % endpoint)
        print(r.text)
        time.sleep(10)

if __name__ == '__main__':
    main()