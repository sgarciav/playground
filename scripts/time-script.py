#!/usr/bin/env python3

# pylint: disable=C0103

import sys
import time
import numpy as np

def main_loop():
    ''' main loop '''

    print("Press Ctrl+C to stop the script.")

    try:
        for i in range(60):
            print(f'time: {i}')
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nInterrupt received! Cleaning up resources...")
        sys.exit(0)


if __name__ == '__main__':
    main_loop()
