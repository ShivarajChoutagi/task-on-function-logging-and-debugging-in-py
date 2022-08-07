import logging
logging.basicConfig(filename='test4.log' , level=logging.DEBUG)

logging.debug('showing the debug error')
logging.info('enter the number presented')
logging.error('the errors in code ')
logging.warning('the code is gives some warning')

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

l1=[]
for i in l:
    logging.debug('showing the debug error')
    if type(i) == list or type(i) == tuple or type(i) == set :
        for j in i :
            if type(j) == int :
                l1.append(j)
    logging.info('enter the number presented')
    if type(i) == dict :
        for k in i.items() :
            for g in k :
                if type(g) == int :
                    l1.append(g)
print(l1)
logging.info('s finally entered')

for i in l1 :
    try:
        if i % 2 == 0  :
            pass
        else :
            print(i)
    finally:
        logging.warning('the code is gives some warning when not executed')


    try:
        for i in set(l1) :
             print(i , ":" ,l1.count(i))
    except Exception as e:
        print(e)

    try:
        j = 1
        for i in l1:
            if type(i) == int:
                j = j * i
        print(j)
    finally:
        print(' finaslly executed')
