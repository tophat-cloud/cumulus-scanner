import sys, getopt
from mushroom_spores import mushroom_spore

def main(argv):

    FILE_NAME = argv[0]
    OPTION_NAME = ""
    URL = ""

    try:
        opts, etc_args = getopt.getopt(argv[1:], "hu:o:", ["help", "url=", "options="])
    
    except getopt.GetoptError:
        body = '-u <Url> -o <Options> -t <Thunder name>'
        print(FILE_NAME, body)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            body = '-u <url> -o <options>'
            body += 'Options :\n'
            body += 'a => use all module\n'
            body += 'c => use check unnecessary comment module\n'
            body += 'd => use directory travelser module\n'
            body += 'g => use guessing admin moduel\n'
            body += 'f => use find obfuscation javascript module'
            print(FILE_NAME, body)
        elif opt in ("-u", "--url"):
            URL = arg
        elif opt in ("-o", "--options"):
            OPTION_NAME = arg
        
    if len(URL) < 1 or len(OPTION_NAME) < 1:
        print(FILE_NAME,'-u, -o option is mandatory')
        sys.exit(2)
    mushroom = mushroom_spore(URL)
    if OPTION_NAME == "a":
        mushroom.run_all()
    elif OPTION_NAME == "c":
        mushroom.check()
    elif OPTION_NAME == "d":
        mushroom.directory()
    elif OPTION_NAME == "g":
        mushroom.guessing()
    elif OPTION_NAME == "f":
        mushroom.find()

if __name__ == "__main__":
    main(sys.argv)