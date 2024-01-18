import time

start = time.process_time()
# 任意代码块
for i in range(100000000):
    i += 1
end = time.process_time()
print('Running time: %s Seconds' % (end-start))
