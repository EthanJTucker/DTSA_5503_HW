def maxSubArray(a):
    n = len(a)
    if n == 1:
        return 0
    # your code here
    minsofar = float('inf')
    maxdiff = 0
    
    for i in range(n):
        if a[i] < minsofar :
            minsofar = a[i]
        if a[i] - minsofar > maxdiff:
            maxdiff = a[i] - minsofar
    
    return maxdiff

##############################################################################################################################

from random import randint

assert(maxSubArray([100, -2, 5, 10, 11, -4, 15, 9, 18, -2, 21, -11]) == 25), 'Test 1 failed'
assert(maxSubArray([-5, 1, 10, 4, 11, 4, 15, 9, 18, 0, 21, -11]) == 26), 'Test 2 failed'
assert(maxSubArray([26, 0, 5, 18, 11, -1, 15, 9, 13, 5, 16, -11]) == 18), 'Test 3 failed'

def get_random_array(n):
    assert(n > 100)
    lst = [randint(0, 25) for j in range(n)]
    lst[0] = 1000
    lst[10] = -15
    lst[25] = 40
    lst[n-10] = 60
    lst[n-3]= -40
    return lst
assert(maxSubArray(get_random_array(50000)) == 75), 'Test on large random array 50000 failed'
assert(maxSubArray(get_random_array(500000)) == 75), 'Test on large random array of size 500000 failed'
print('All tests passed (10 points!)')

##############################################################################################################################

from numpy.fft import fft, ifft
from numpy import real, imag

def polynomial_multiply(a_coeff_list, b_coeff_list):
    # Return the coefficient list of the multiplication 
    # of the two polynomials 
    # Returned list must be a list of floating point numbers.
    # Please convert list from complex to reals by using the 
    # real function in numpy.
    # your code here
    
    m = len(a_coeff_list)
    n = len(b_coeff_list)
    
    a_coeff_list = a_coeff_list + [0]*(n-1)
    b_coeff_list = b_coeff_list + [0]*(m-1)
    
    a_fft_lst = fft(a_coeff_list)
    b_fft_lst = fft(b_coeff_list)
    
    c_fft_lst = a_fft_lst * b_fft_lst
    c_ifft_lst = ifft(c_fft_lst)
    fix_c_ifft_lst = [real(x) for x in c_ifft_lst]
    
    return fix_c_ifft_lst

##############################################################################################################################

def check_poly(lst1, lst2):
    print(f'Your code found: {lst1}')
    print(f'Expected: {lst2}')
    assert(len(lst1) == len(lst2)), 'Lists have different lengths'
    for (k,j) in zip(lst1, lst2):
        assert abs(k-j)<= 1E-05, 'Polynomials do not match'
    print('Passed!')
print('-------') 
print('Test # 1')
# multiply (1 + x - x^3) with (2 - x + x^2)
a = [1, 1, 0, -1]
b = [2, -1, 1]
c = polynomial_multiply(a,b)
assert(len(c) == 6)
print(f'c={c}')
check_poly(c, [2,1,0,-1,1,-1])
print('-------')
print('Test # 2')
# multiply 1 - x + x^2 + 2 x^3 + 3 x^5 with 
#            -x^2 + x^4 + x^6
a = [1, -1, 1, 2, 0, 3]
b = [0, 0, -1, 0, 1, 0, 1]
c = polynomial_multiply(a,b)
assert(len(c) == 12)
print(f'c={c}')
check_poly(c, [0, 0, -1, 1, 0, -3, 2, -2, 1, 5, 0, 3])
print('-------')
print('Test # 3')
# multiply 1 - 2x^3 + x^7 - 11 x^11
# with     2 - x^4 - x^6 + x^8
a = [1, 0, 0, -2, 0, 0, 0, 1, 0, 0, 0, -11]
b = [2, 0, 0, 0, -1, 0, -1, 0, 1]
c = polynomial_multiply(a, b)
assert(len(c) == 20)
print(f'c={c}')
check_poly(c, [2, 0, 0, -4, -1, 0, -1, 4, 1, 2, 0, -25, 0, -1, 0, 12, 0, 11, 0, -11])
print('All tests passed (10 points!)')

##############################################################################################################################

# inputs sets a, b, c
# return True if there exist n1 in a, n2 in B such that n1+n2 in C
# return False otherwise
# number n which signifies the maximum number in a, b, c
# here is a useful reference to set data structure in python
# https://docs.python.org/3/tutorial/datastructures.html#sets

def convert_to_poly(lst, n):
    result = [0]*n
    for i in lst:
        result[i] = 1
    return result

def check_sum_exists(a, b, c, n):

    # convert sets a, b into polynomials as provided in the hint
    # a_coeffs and b_coeffs should contain the result
    # your code here
    a_coeffs = convert_to_poly(a, n)
    b_coeffs = convert_to_poly(b, n)
    
    # multiply them together
    c_coeffs = polynomial_multiply(a_coeffs, b_coeffs)
    # use the result to solve the problem at hand
    # your code here
    
    float_threshold = 10**-10
    for elt in c:
        if c_coeffs[elt] > float_threshold:
            return True
        
    return False
    # return True/False

##############################################################################################################################

print('-- Test 1 --')
a = set([1, 2, 10, 11])
b = set([2, 5, 8, 10])
c = set([1, 2, 5,  8])
assert not check_sum_exists(a, b, c, 12), f'Failed Test 1: your code returned true when the expected answer is false'
print('Passed')
print('-- Test 2 --')
a = set([1, 2, 10, 11])
b = set([2, 5, 8, 10])
c = set([1, 2, 5,  8, 11])
assert check_sum_exists(a, b, c, 12), f'Failed Test 2: your code returns false but note that 1 in a + 10 in b = 11 in c '
print('Passed')

print('-- Test 3 --')
a={1, 4, 5, 7, 11, 13, 14, 15, 17, 19, 22, 23, 24, 28, 34, 35, 37, 39, 42, 44}
b={0, 1, 4, 9, 10, 11, 12, 15, 18, 20, 25, 31, 34, 36, 38, 40, 43, 44, 47, 49}
c={3, 4, 5, 7, 8, 10, 19, 20, 21, 24, 31, 35, 36, 37, 38, 39, 42, 44, 46, 49}
assert check_sum_exists(a, b, c, 50), f'Failed Test 3: your code returns False whereas the correct answer is true eg., 4 + 0 = 4'

print('-- Test 4 --')

a={98, 2, 99, 40, 77, 79, 87, 88, 89, 27}
b={64, 66, 35, 69, 70, 40, 76, 45, 12, 60}
c={36, 70, 10, 44, 15, 16, 83, 20, 84, 55}
assert not check_sum_exists(a, b, c, 100), f'Failed Test 4: your code returns True whereas the correct answer is False'

print('All Tests Passed (15 points)!')

##############################################################################################################################

import csv
from matplotlib import pyplot as plt

file = open('natural_gas_futures_weekly_all.csv','r')
csv_handle = csv.DictReader(file)

weekly_prices = []
dates = []

for rows in csv_handle:
    dates.append(rows['Date'])
    weekly_prices.append(0.5 * (float(rows['High']) + float(rows['Low'])) )
file.close()

plt.plot(range(len(weekly_prices)), weekly_prices, '-b')
plt.xlabel('Week #')
plt.ylabel('Crude Oil Future Price')

##############################################################################################################################

from numpy.fft import fft, ifft
from numpy import real,imag

# here we have computed the fft of the weekly_prices
fft_data =  fft(weekly_prices)
N = len(fft_data)
assert(N == len(weekly_prices))
# TODO: first fill in the frequencies call this list 
# fft_frequencies -- it must have length N
# it must store the frequencies of each element in the fft_data
# ensure that the frequencies of the second half are negative.
# your code here

f0 = [0]
f1 = [k/N for k in range(1, N//2)]
fmid = [(N//2)/N]
f2 = [-(N-k)/N for k in range(N//2 + 1, N)]

fft_frequencies = f0 + f1 + fmid + f2

# This function will be useful for you. Please go through the code.

def select_all_items_in_freq_range(lo, hi):
    # TODO: go through the fft_data and select only those frequencies in the range lo/hi
    new_fft_data = [] # make sure we have the 0 frequency component
    for (fft_val, fft_freq) in zip(fft_data, fft_frequencies):
        if lo <= fft_freq and fft_freq < hi:
            new_fft_data.append(fft_val)
        elif -hi < fft_freq and fft_freq <= -lo:
            new_fft_data.append(fft_val)
        else:
            new_fft_data.append(0.0)
    filtered_data = ifft(new_fft_data)
    assert all( abs(imag(x)) <= 1E-10 for x in filtered_data)
    return [real(x) for x in filtered_data]

upto_1_year = [] # All signal components with frequency < 1/52
one_year_to_1_quarter = [] # All signal components with frequency between 1/52 (inclusive) and 1/13 weeks (not inclusive)
less_than_1_quarter = [] # All signal components with frequency >= 1/13 

# TODO: Redefine the three lists using the select_all_items function
# your code here
upto_1_year = select_all_items_in_freq_range(0, 1/52)
one_year_to_1_quarter = select_all_items_in_freq_range(1/52, 1/13)
less_that_1_quarter = select_all_items_in_freq_range(1/13, float('inf'))

##############################################################################################################################

from matplotlib import pyplot as plt
plt.plot(upto_1_year,'-b',lw=2)
plt.plot(weekly_prices,'--r',lw=0.2)
plt.xlabel('Week #')
plt.ylabel('Price')
plt.title('Frequency components < once/year')
plt.figure()
plt.plot(one_year_to_1_quarter,'-b',lw=2)
plt.plot(weekly_prices,'--r',lw=0.2)
plt.title('Frequency components between once/year and once/quarter')
plt.xlabel('Week #')
plt.ylabel('Price')
plt.figure()
plt.plot(less_than_1_quarter,'-b',lw=2)
plt.plot(weekly_prices,'--r',lw=0.2)
plt.title('Frequency components >  once/quarter')
plt.xlabel('Week #')
plt.ylabel('Price')

plt.figure()
plt.plot([(v1 + v2 + v3) for (v1, v2, v3) in zip(upto_1_year,one_year_to_1_quarter,less_than_1_quarter)],'-b',lw=2)
plt.plot(weekly_prices,'--r',lw=0.2)
plt.title('Sum of all the components')
plt.xlabel('Week #')
plt.ylabel('Prices')

N = len(weekly_prices)
assert(len(fft_frequencies) == len(weekly_prices))
assert(fft_frequencies[0] == 0.0)
assert(abs(fft_frequencies[N//2] - 0.5 ) <= 0.05), f'fft frequncies incorrect: {fft_frequencies[N//2]} does not equal 0.5'
assert(abs(fft_frequencies[N//4] - 0.25 ) <= 0.05), f'fft frequncies incorrect:  {fft_frequencies[N//4]} does not equal 0.25'
assert(abs(fft_frequencies[3*N//4] + 0.25 ) <= 0.05), f'fft frequncies incorrect:  {fft_frequencies[3*N//4]} does not equal -0.25'
assert(abs(fft_frequencies[1] - 1/N ) <= 0.05), f'fft frequncies incorrect:  {fft_frequencies[1]} does not equal {1/N}'
assert(abs(fft_frequencies[N-1] + 1/N ) <= 0.05), f'fft frequncies incorrect:  {fft_frequencies[N-1]} does not equal {-1/N}'

for (v1, v2, v3, v4) in zip(weekly_prices, upto_1_year,one_year_to_1_quarter,less_than_1_quarter ):
    assert ( abs(v1 - (v2 + v3+v4)) <= 0.01), 'The components are not adding up -- there is a mistake in the way you split your original signal into various components'
print('All tests OK -- 10 points!!')