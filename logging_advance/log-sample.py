import logging
import employee 

#Logger dedicated to log-sample module only
logger = logging.getLogger(__name__)  

#Setting level to DEBUG 20
logger.setLevel(logging.DEBUG)

#Formatting our log file 'log-sample.log'
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

#Lets configure our specific logger here which outputs our logs to below employee.log file
file_handler = logging.FileHandler('log-sample.log')

# Lets say i only want errors to be printed in my output log file
file_handler.setLevel(logging.ERROR)

#Setting our formating to our log file 'log-sample.log'
file_handler.setFormatter(formatter) 

# Lets say i want to output other function without error ones 
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return x / y

n1 = 660
n2 = 0

add_result = add(n1,n2)
logger.debug(f'Add: {n1}+{n2}={add_result}')

sub_result = sub(n1,n2)
logger.debug(f'Sub: {n1}-{n2}={sub_result}')

mul_result = mul(n1,n2)
logger.debug(f'Mul: {n1}x{n2}={mul_result}')

div_result = div(n1,n2)
logger.debug(f'Div: {n1}/{n2}={div_result}')