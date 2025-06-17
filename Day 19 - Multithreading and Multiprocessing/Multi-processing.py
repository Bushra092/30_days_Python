
#? using Multi processing

import time
import multiprocessing


Square_Result = []
Cube_Result = []

def cal_sqr(nums):
    global Square_Result
    print('Calculating Squares')
    for i in nums:
        time.sleep(0.2)
        print('Square:', i*i)
        Square_Result.append(i*i)
    

    print('Result Within Process..... Square', Square_Result)
        

def cal_cub(nums):
    print('Calculating Cube')
    for i in nums:
        time.sleep(0.2)
        print('Cube:', i*i*i)   
        Cube_Result.append(i*i*i)
    print('Result Within Process..... Cube', Cube_Result)    



if __name__ == '__main__':
    arr = [2,3,4,5]
    mulP1 = multiprocessing.Process(target=cal_sqr, args=(arr,))
    mulP2 = multiprocessing.Process(target=cal_cub, args=(arr,))

    mulP1.start()
    mulP2.start()

    mulP1.join()
    mulP2.join()


    print('Result Outside Process..... Square', Square_Result)
    print('Result Outside Process..... Cube', Cube_Result)

    print('Done ')

