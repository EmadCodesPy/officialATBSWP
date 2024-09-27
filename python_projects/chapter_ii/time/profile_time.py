import time, sys, cProfile

sys.set_int_max_str_digits(500000)

def CalcProd():
    product = 1
    for i in range(1,100000):
        product *= i
    return product

startTime = time.time()
prod = CalcProd()
endTime = time.time()
print('The product is %s digit\'s long.' % len(str(prod)))
print('It took %s seconds to calculate.' % (endTime - startTime))

#cProfile.run()
#cProfile.run() can also be used to profile time