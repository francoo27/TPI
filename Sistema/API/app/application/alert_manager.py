

def alert_warning(string):
    print(f'{Colors.WARNING}[CineAr][WARNING]: {string}{Colors.ENDC}')


def alert_error(string):
    print(f'{Colors.ERROR}[CineAr][ERROR]: {string}{Colors.ENDC}')


def alert_ok(string):
    print(f'{Colors.OKGREEN}[CineAr][OK]: {Colors.OKGREEN}{string}{Colors.ENDC}')


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
