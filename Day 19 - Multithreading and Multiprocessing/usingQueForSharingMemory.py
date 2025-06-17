import multiprocessing.queues
import time
import multiprocessing
 

def cal_sqr(nums, q): 

    print('Calculating Squares')
    for i in nums:
        q.put(i*i) 
        

 
if __name__ == '__main__':
    arr = [2,3,4,5]
    q = multiprocessing.Queue()
    mulP1 = multiprocessing.Process(target=cal_sqr, args=(arr, q))

    mulP1.start()
    mulP1.join()


    print('Result Outside Process..... Queue' )

    while q.empty() is False:
        print(q.get())



    print('Done ')