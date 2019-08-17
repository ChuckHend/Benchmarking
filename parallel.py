from joblib import Parallel, delayed
import multiprocessing
import time
import sys

if len(sys.argv) >1:
    x = int(sys.argv[1])
else:
    x = 1000

def processInput(i):
	return i * i

def for_loop(inputs):
    results = []
    for x in inputs:
        results.append( processInput(x) )
    return results

def list_comp(inputs):
    return [ processInput(x) for x in inputs ]

def parallel(inputs): 
    num_cores = multiprocessing.cpu_count()
    # print('\nNumber Cores: {}'.format(num_cores))
    results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
    return results


methods = {
    'loop' : for_loop,
    'list_comp' : list_comp,
    'parallel' : parallel
    }

if __name__ == '__main__':
    print('Computing x^2 for {} iterations. . .'.format(x))
    inputs = range(x)
    
    for alg, fun in methods.items():
        print(f"Starting-{alg}--- ", end='\t')
        start = time.process_time()
        results = fun(inputs)
        # results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
        proc_time = round(time.process_time()-start,4)
        print(f'{proc_time} seconds')
