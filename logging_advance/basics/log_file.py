import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

n1 = 660
n2 = 770

add_result = add(n1,n2)
logging.debug(f'Add: {n1}+{n2}={add_result}')

sub_result = sub(n1,n2)
logging.debug(f'Add: {n1}+{n2}={sub_result}')

mul_result = mul(n1,n2)
logging.debug(f'Add: {n1}+{n2}={mul_result}')

div_result = div(n1,n2)
logging.debug(f'Add: {n1}+{n2}={div_result}')