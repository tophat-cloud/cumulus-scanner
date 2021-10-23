import sys, getopt
import platform
from mushroom_spores import mushroom_spore

def main(argv):

    FILE_NAME = argv[0]
    OPTION_NAME = ""
    URL = ""

    try:
        opts, etc_args = getopt.getopt(argv[1:], "hu:o:", ["help", "url=", "options="])
    
    except getopt.GetoptError:
        body = '-u <Url> -o <Options>'
        print(FILE_NAME, body)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            body = '-u <url> -o <options> -t <ostype>\n'
            body += 'Url -u : Please enter the url you want to scan.\n\n'
            body += 'Options -o :\n'
            body += '\ta => use all module\n'
            body += '\tc => use check unnecessary comment module\n'
            body += '\td => use directory travelser module\n'
            body += '\tg => use guessing attack module\n'
            body += '\tf => use find unobfuscation code module\n'
            print(FILE_NAME, body)
            
        elif opt in ("-u", "--url"):
            URL = arg
        elif opt in ("-o", "--options"):
            OPTION_NAME = arg
    if len(URL) < 1 or len(OPTION_NAME) < 1:
        print(FILE_NAME,'-u, -o option is mandatory\nIf you need help please use -h')
        sys.exit(2)
    else:
        what_os = platform.system()
        if what_os == "Darwin":
            while 1:
                w = input("What is your mac os cpu 1) intel 2) m1 \nPlease choose number:")
                if w == 1 or w == 2:
                    break
                print("Please input just number 1 or 2")
            if w == 2:
                what_os == "m1"
        mushroom = mushroom_spore(URL, what_os)
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