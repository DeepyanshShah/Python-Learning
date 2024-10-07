import logging

#Logger dedicated to employee module only
logger = logging.getLogger(__name__)  

#Setting level to info 10
logger.setLevel(logging.INFO)

#Formatting our log file 'employee.log'
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

#Lets configure our specific logger here which outputs our logs to below employee.log file
file_handler = logging.FileHandler('employee.log')

#Setting our formating to our log file 'employee.log'
file_handler.setFormatter(formatter) 

logger.addHandler(file_handler)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Jotaro', 'Kujo')
emp_2 = Employee('Dio', 'Brando')
emp_3 = Employee('Jonathan', 'Joestar')