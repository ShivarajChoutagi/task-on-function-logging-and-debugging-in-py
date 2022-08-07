import logging
logging.basicConfig(filename='test6.log' , level=logging.DEBUG)

logging.info('handle the error occurred')
logging.error('shows error in the givan list')
logging.warning('enterd list of file showing some warning')

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]


for i in l:
    m = 1
    try:
        if type(i) == list or type(i) == tuple or type(i) == set:
            for j in i:
                if type(j) == int:
                    m = m * j
                    print(type(i), m)
    except:
        if type(i) == dict:
            for k in i.items():
                for n in k:
                    if type(n) == int:
                        m = m * n
                        print(type(i), m)
    finally:
        print('')


