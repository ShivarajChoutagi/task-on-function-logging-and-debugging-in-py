import logging
logging.basicConfig(filename='test5.log' , level=logging.DEBUG)

logging.debug('this is shows some error')
logging.info('entered the name of list error')
logging.error('if there is type error in code')
logging.warning('the code is gives some warning')

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]


l1 = []
for i in l:
    logging.info('entered the name of list error')
    try:
        if type(i) == list or type(i) == tuple or type(i) == set :
            for j in i :
                if j == 'ineuron' :
                    l1.append(j)

    except:
        if type(i) == dict :
            for k in i.items() :
                for g in k :
                    if g == 'ineuron' :
                        l1.append(g)
    finally:
        print('entered type is str')
print(l1)


