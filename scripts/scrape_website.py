#!/usr/bin/env python3

# system includes
import sys
import requests

def main():
    res = requests.get('https://codedamn.com')

    # print(res.text)
    print(res.status_code)


if __name__ == '__main__':
    sys.exit(main())
