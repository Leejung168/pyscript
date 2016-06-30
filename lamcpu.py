#!/usr/bin/env python
from multiprocessing import Pool,cpu_count
import time, getopt, sys,signal

def usage():
    print '''Usage: lambertcpu [OPTION]...
tool to impose cpu load on and stress test systems.
  -c, --cpu   number of cpu cores
  -h, --help  display this help and exit
  -t, --time  time of running  
      --version  output version information and exit
'''

def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    while True:
        1*1

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:ht:", ["help","cpu=","time="])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    processes = None
    T = None
    for o, a in opts:
        if o in ("-c","--cpu"):
            processes = int(a)
        elif o in ("-t","--time"):
            T = float(a)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"
    if processes is None:
        processes=cpu_count()
    if T is None:
        T=300
    print 'Initializing {0} workers......'.format(processes)
    pool = Pool(processes, init_worker)
    print 'Press Ctrl+C stop!'
    try:
        time.sleep(T)
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()

if __name__ == '__main__':
      main()
