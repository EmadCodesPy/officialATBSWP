import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#This line is required for logging and you can add file using filename='(path)'
#ogging.disable(logging.CRITICAL)
#This removes all the logs instead of manually deleting each one

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s%%)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial (%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
    