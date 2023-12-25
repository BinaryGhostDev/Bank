class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def success_message(message):
    print(ConsoleColors.OKGREEN + message + ConsoleColors.ENDC)

def error_message(message):
    print(ConsoleColors.FAIL + message + ConsoleColors.ENDC)

# Usage
# success_message("Balance added successfully. Updated Balance: ₹ 1,000,000")
# error_message("Error: PIN incorrect. Please try again.")
