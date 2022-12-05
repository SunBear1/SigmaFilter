"""
Module containing console UI functions
"""


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run_filters(word: str):
    import filters
    for i in dir(filters):
        filter = getattr(filters, i)
        if callable(filter):
            if not filter(word):
                print("-------------------------------")
                print(
                    f"Filter {filter.__qualname__} has mark word {Colors.OKCYAN}{word}{Colors.ENDC} as {Colors.FAIL}uncensored{Colors.ENDC}")
                print("-------------------------------")
                return
    print("-------------------------------")
    print(
        f"All filters passed {Colors.OKGREEN}successfully{Colors.ENDC} for word {Colors.OKCYAN}{word}{Colors.ENDC}")
    print("-------------------------------")
