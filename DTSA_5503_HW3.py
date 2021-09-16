# Problem one asks us to compute the total processing time used by m processors, when supplied with a list of n jobs with some times T_i. This processing time is called makespan.

def compute_makespan(times, m, assign):
    # times is an array of job times of size n
    # m is the number of processors
    # assign is an array of size n whose entries are between 0 to m-1 
    # indicating the processor number for
    # the corresponding job.
    # Return: makespan of the assignment
    # your code here
    
    total_times = [0]*m
    n = len(times)
    
    for i in range(n):
        this_processor = assign[i]
        this_time = times[i]
        total_times[this_processor] = total_times[this_processor] + this_time
        
    makespan = max(total_times)
    return(makespan)
        
#########################################################################################################################################################################################################
## BEGIN TESTS
print('Test 1 ... ', end = '')
times = [2, 2, 2, 2, 3, 3, 2]
assigns = [0, 0, 0, 0, 1, 1, 2]
m = 3
s = compute_makespan(times, m, assigns)
assert s == 8, f'Expected makespan is 8, your code returned: {s}'
print(' passed!')

print('Test 2 ...', end='')
times = [2, 1, 2, 2, 1, 3, 2, 1, 1, 3]
assigns = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
m = 3
s = compute_makespan(times, m, assigns)
assert s == 10, f' Expected makespan is 10, your code returned {s}'
print('  passed!')
print('Tests passed: 10 points!')

## END TESTS
#########################################################################################################################################################################################################
# Problem two required me to create a fast algorithm for computing the makespan. The goal was to use a greedy algorithm - pick the processor
## with the currently lowest load, and assign it the next job until there are no more jobs to assign. I used a minHeap to efficiently maintain
### the lowest - load processor, and did most of the work in that minHeap class.

import heapq

class processor:
    def __init__(self, num):
        self.number = num
        self.load = 0
        
    def update_load(self, job_time):
        self.load = self.load + job_time
    
class minHeap:
    def __init__(self, num_processors, num_jobs):
        self.processors = [processor(j) for j in range(num_processors)]
        
        ##PriorityQueue is minHeap of tuples (load, processor) with key = load
        self.priorityQ = []
        self.initialize_priority_queue(num_processors)
        self.assignments = [None]*num_jobs
        
    def insert_processor(self, i):
        this_tuple = (0, i)
        heapq.heappush(self.priorityQ, this_tuple)
        
    def initialize_priority_queue(self, num_processors):
        for i in range(num_processors):
            self.insert_processor(i)
    
    def get_next_processor(self):
        this_tuple = heapq.heappop(self.priorityQ)
        this_processor = self.processors[this_tuple[1]]
        return this_processor
    
    def add_job(self, job_time, job_num):
        ##Get next processor
        this_processor = self.get_next_processor()
        ##Update Processor Load
        this_processor.update_load(job_time)
        ##Record job assignment
        self.assignments[job_num] = this_processor.number
        ##Reinsert processor with new load
        heapq.heappush(self.priorityQ, (this_processor.load, this_processor.number))
        
        
    def extract_assignments(self):
        return self.assignments
    
    def extract_makespan(self):
        loads = [self.processors[i].load for i in range(len(self.processors))]
        return max(loads)
    

def greedy_makespan_min(times, m):
    # times is a list of n jobs.
    assert len(times) >= 1
    assert all(elt >= 0 for elt in times)
    assert m >= 2
    n = len(times)
    # please do not reorder the jobs in times or else tests will fail.
    # you can implement a priority queue if you would like.
    # use https://docs.python.org/3/library/heapq.html heapq data structure 
    # Return a tuple of two things: 
    #    - Assignment list of n numbers from 0 to m-1
    #    - The makespan of your assignment
    # your code here
    
    n = len(times)
    priorityQ = minHeap(m, n)
    
    for k in range(n):
        this_load = times[k]
        priorityQ.add_job(this_load, k)
    
    assignments = priorityQ.extract_assignments()
    makespan = priorityQ.extract_makespan()
        
    return(assignments, makespan)  
    
#########################################################################################################################################################################################################
## BEGIN TESTS
def do_test(times, m, expected):
    (a, makespan) = greedy_makespan_min(times,m )
    print('\t Assignment returned: ', a)
    print('\t Claimed makespan: ', makespan)
    assert compute_makespan(times, m, a) == makespan, 'Assignment returned is not consistent with the reported makespan'
    assert makespan == expected, f'Expected makespan should be {expected}, your core returned {makespan}'
    print('Passed')
print('Test 1:')
times = [2, 2, 2, 2, 2, 2, 2, 2, 3] 
m = 3
expected = 7
do_test(times, m, expected)

print('Test 2:')
times = [1]*20 + [5]
m = 5
expected =9
do_test(times, m, expected)

print('Test 3:')
times = [1]*40 + [2]
m = 20
expected = 4
do_test(times, m, expected)
print('All tests passed: 15 points!')
## END TESTS
#########################################################################################################################################################################################################

#########################################################################################################################################################################################################