# Q3: 给一堆item的arrival time，process一个item需要5分钟。有item正在被处理的时候，新到达的item会被放进一个container。
# container最多只能装10个item，满了的话会discard掉新到达的item。问当处理/丢掉完所有item后，时间是第多少秒。

def end_time_after_processing(arrivals, service_time=300, capacity=10):
    """
    arrivals:  可迭代/列表，元素是到达时刻（秒）。可无序；函数内会排序。
    service_time: 单个item处理时长（秒），题目为 300。
    capacity:   等待容器容量，题目为 10。
    返回：当处理/丢掉完所有item后，时间的秒数（int）。
    """
    if not arrivals:
        return 0

    arrivals = sorted(arrivals)
    next_free = 0
    containter = []

    for t in arrivals:
         # Process queued items if processor was idle before this arrival
        while containter and t >= next_free:
            next_free += service_time
            containter.pop(0)
            
        if t >= next_free:
             # processor idle at arrival
            next_free = t + service_time
        else:
            # processor busy
            if len(containter) < capacity:
                containter.append(t)
            else:
                pass  # discard
    return next_free + len(containter) * service_time
        
        
# Example usage:
arrivals = [0, 100, 200, 250, 300, 350, 400, 450, 500, 550, 600, 700]
result = end_time_after_processing(arrivals)
print(result)  # Output: 3600