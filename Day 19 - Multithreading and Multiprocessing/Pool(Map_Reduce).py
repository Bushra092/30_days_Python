


#? Pool

# def f(n):
#     return n*n

# if __name__ == '__main__':
#     array = [1,2,3,4,5]

#     result = []
#     for n in array:
#         result.append(f(n))

#     print(result)



#? Uisng Pool
# from multiprocessing import Pool

# def f(n):
#     return n*n

# if __name__ == '__main__':
#     array = [1,2,3,4,5]
#     p = Pool()

#     result = p.map(f, array)

#     print(result)



#? Just making function a bit harder


from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for i in range(100):
        sum += i*i
    return sum

if __name__ == '__main__': 
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(100000))

    p.close()
    p.join()
    print('Pool Took', time.time() -t1 ) 


    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print('Series of processing took', time.time() - t2)    