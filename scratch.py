import logging
logging.basicConfig(filename='test2.log' , level=logging.INFO)

logging.info('enter the number presented')
logging.error('the errors in code ')
logging.warning('the code is gives some warning')

for i in range(6):
    logging.info('enter the right value')
    if i <= 3:
        n = i
    else:
        logging.error('mentioned the error')
        n = 6 - i
    print(("ineuron "*n).center(30 ,' '))
