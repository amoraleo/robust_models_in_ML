def network_delay_time(times, N, X):
    dist_list = [-1 for _ in range(N)]
    dist_list[X-1] = 0
    visited_nodes = {X}
    indeces_stack = []
    
    while times:
        for index, [depart, arriv, dist] in enumerate(times):
            if depart in visited_nodes:
                if arriv in visited_nodes:
                    dist_list[arriv-1] = min(dist_list[arriv-1], dist_list[depart-1] + dist)
                else:
                    dist_list[arriv-1] = dist_list[depart-1] + dist
                    visited_nodes.add(arriv)
                indeces_stack.append(index)
        if not indeces_stack:
            break
        while indeces_stack:
            del times[indeces_stack.pop()]
    
    if -1 in dist_list:
        return -1
    else:
        return max(dist_list)

if __name__ == "__main__":
    times  = eval(input())
    N = int(input())
    X = int(input())
    print(network_delay_time(times, N, X))
