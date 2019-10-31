import colorama
from colorama import Fore, Back, Style
import sys
from OpenSSL import crypto

colorama.init(autoreset=True)

def spinner():
    sys.stdout.write(' ')
    while True:
        for cursor in '|/-\\':
            yield cursor

def spin():
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    sys.stdout.write('\b')

p12FilePath = ""
if (len(sys.argv) > 2 and sys.argv[1] == "--p12-path"):
    p12FilePath = sys.argv[2]
else:
    print(Fore.RED + Style.BRIGHT + 'Error:' + Style.RESET_ALL + Fore.RED + 'Error: Please supply the path to the .p12 file to crack (--p12-path /home/hax/secret.p12)')
    exit(0)

wordlist = ""
if (len(sys.argv) > 4 and sys.argv[3] == "--wordlist"):
    wordlist = sys.argv[4]
else:
    print(Fore.RED + Style.BRIGHT + 'Error:' + Style.RESET_ALL + Fore.RED + ' Please supply the path to wordlist of guesses (--wordlist /home/hax/password_guesses.txt)')
    exit(0)

iterations = 0
spinner = spinner()

with open(wordlist, 'r') as fp:
    line = fp.readline()
    print('\n')
    print(Fore.CYAN + ' Brute forcing...')
    print('\n')
    while line:
        spin()
        guess = line.strip()
        try:
            p12 = crypto.load_pkcs12(open(p12FilePath, 'rb').read(), guess.encode('utf8'))
        except crypto.Error as e:
            p12 = None
        if p12:
            print(Fore.BLUE + '****************************************************************\n')
            print(' {}Success!{} Password cracked after {}{}{} attempts.'.format(Fore.GREEN, Fore.RESET, Fore.YELLOW, str(iterations), Fore.RESET))
            print('\n')

            print(" Password is: " + Style.BRIGHT + Fore.RED + guess + '\n')
            print(Fore.BLUE + ' ****************************************************************\n')
            print('\n')
            exit(0)
        else:
            iterations += 1
        line = fp.readline()

print(Fore.RED + 'Failed to crack the password - try again with a new wordlist\n')
exit(0)