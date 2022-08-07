import logging
logging.basicConfig(filename='test3.log' , level=logging.DEBUG)

logging.debug('showing the debug error')
logging.info('enter the number presented')
logging.error('the errors in code ')
logging.warning('the code is gives some warning')

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
logging.info('enter the list only')
for i in l :
    logging.error('entered list type error')
    if type(i) == list :
        try:
            print(i)
        except Exception as e:
            logging.warning('entered the variable giving warning')
        finally:
            print('executed finally')

for i in l :
    logging.info('enter the dict type ')
    if type(i) == dict :
        try:
            logging.warning('giving the warning')
            print(i)
        except:
            logging.error('enter values in list wrong')
        finally:
            logging.info('printed sucusafully')

for i in l :
    logging.info('enter the tuple type ')
    if type(i) == tuple:
        try:
            logging.warning('giving the warning')
            print(i)
        except:
            logging.error('enter values in list wrong')

        finally:
            print('executed finally')





