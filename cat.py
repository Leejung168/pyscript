import getopt, sys, os

def usage():
    print('''Usage: cat [OPTION]... [FILE]...
Concatenate FILE(s), or standard input, to standard output.
  -n, --number   number all output lines
      --help     display this help and exit
      --version  output version information and exit
Examples:
  cat f - g  Output f's contents.
  cat        Copy standard input to standard output.''')


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:vn:", ["help","silence","version","number="])
        for i in (sys.argv[1:]):
            if os.path.isfile(i):
                with open(i) as f:
                    print(f.read())
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    else:
        for o, a in opts:
            if o in ("-v","--version"):
                version = "cat (Lz coreutils) 1.0"
                print(version)
                sys.exit()
            elif o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-n", "--number"):
                for i in (sys.argv[2:]):
                    if os.path.isfile(i):
                        with open(i) as f:
                            for (num, value) in enumerate(f):
                                print(num, value.strip())
                    else:
                        print("cat: {0}: No such file or directory".format(i))
            else:
                pass
if __name__ == "__main__":
    main()
