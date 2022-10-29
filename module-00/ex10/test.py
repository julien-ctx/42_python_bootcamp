from time import sleep, perf_counter

fmt = "  Progress: {:>3}% estimated {:>3}s remaining"
num = 1000

start = perf_counter()
for i in range(1, num + 1):
    # Simulate doing a few calculations
    sleep(0.01)

    stop = perf_counter()
    remaining = round((stop - start) * (num / i - 1))
    print(fmt.format(100 * i // num, remaining), end='\r')
print()
