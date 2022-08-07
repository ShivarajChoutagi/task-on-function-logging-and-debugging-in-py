import logging
logging.basicConfig(filename='string.log',level=logging.INFO)

logging.info('entere right variablr')
logging.warning('code gives some warning in system')
logging.error('denotes error in code')


row = int(input("Please enter how many rows you want to print: "))
logging.info('enter the number')
print()
for i in range(row):
    logging.info('Please enter how many rows you want to print: ')
    print("ineuron "*(i+1))

    
for i in range(6):
    logging.info('enter the right value')
    if i <= 3:
        n = i
    else:
        logging.error('mentioned the error')
        n = 6 - i
    print(("ineuron "*n).center(30 ,' '))

