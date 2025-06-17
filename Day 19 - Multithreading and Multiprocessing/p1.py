

#! Share memoryh 


#? using Multi processing

import time
import multiprocessing


Square_Result = []
Cube_Result = []

def cal_sqr(nums, result, v):
    v.value = 5.67
    # global Square_Result
    print('Calculating Squares')
    for idx, i in enumerate(nums):
        time.sleep(0.2)
        print('Square:', i*i)
        result[idx] = i*i
        

 
if __name__ == '__main__':
    arr = [2,3,4,5]
    result = multiprocessing.Array('i',4)
    v = multiprocessing.Value('d',0.0)
    mulP1 = multiprocessing.Process(target=cal_sqr, args=(arr, result, v))

    mulP1.start()
    mulP1.join()


    print('Result Outside Process..... Square', result[:]) 
    print('Result Outside Process using Value', v.value) 

    print('Done ')


