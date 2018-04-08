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

if __name__ == '__main__':
    print('Computing x^2 for {} iterations. . .'.format(x))
    num_cores = multiprocessing.cpu_count()
    print('Number Cores: {}'.format(num_cores))
    inputs = range(x)
    start = time.process_time()
    results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
    time = round(time.process_time()-start,4)
    print('{} seconds'.format(time))
