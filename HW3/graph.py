import numpy as np
from ast import literal_eval as make_tuple
import heapq as hq

def build_graph(name_txt_file):
    lines = open(name_txt_file,"r").readlines()
    lines = [lines[i].strip() for i in range(len(lines))]
    N = int(len(lines) / 2)
    graph = dict()
    
    for i in range(N):
        current_node = float(lines[2 * i])
        
        if len(lines[2 * i + 1]) > 0:
            current_edges = lines[2 * i + 1].split(",")
        else:
            current_edges = []
            
        num_edges = int(len(current_edges) / 2)
            
        graph[float(lines[2 * i])] = []
        
        for j in range(num_edges):
            neighbour = current_edges[2 * j]
            weight = current_edges[2 * j + 1]
            graph[float(lines[2 * i])].append((float(neighbour[1:len(neighbour)]),float(weight[0:len(weight)-1])))
    
    return graph

def find_shortest_path(name_txt_file, source, destination):
    graph = build_graph(name_txt_file)
    path = dict()
    dist = dict()
    S = []
    F = []
    hq.heappush(F,(0.,source))
    path[source] = [float(source)]
    dist[source] = 0.
    while len(F) != 0:
        min_node = hq.heappop(F)
        hq.heappush(S,min_node)
        for node in graph[min_node[1]]:
            S_node = [x[1] for x in S]
            F_node = [x[1] for x in F]
            if node[0] not in S_node and node not in F_node:
                dist[node[0]] = dist[min_node[1]] + node[1]
                hq.heappush(F,(dist[node[0]],node[0]) )
                path[node[0]] = path[min_node[1]][:]
                path[node[0]].append(node[0])
            elif dist[node[0]] > dist[min_node[1]] + node[1]:
                dist[node[0]] = dist[min_node[1]] + node[1]
                path[node[0]] = path[min_node[1]][:]
                path[node[0]].append(node[0])
                for i in range(len(F)):
                    if F[i][1] == node[0]:
                        store = F[i]
                        store[0] = dist[node[0]]
                        F.remove(F[i])
                        hq.heappush(F,store)
    
    if destination in dist.keys():
        return dist[destination],path[destination]
    else:
        return int("inf"),[]

def negative_loop(name_txt_file):
    graph = build_graph(name_txt_file)
    N = len(graph.keys())
    edges = []
    for key in graph:
        for i in range(len(graph[key])):
            current_edge = graph[key][i]
            edges.append((key,current_edge[0],current_edge[1]))
    dist = [float("inf")] * N
    dist[0] = 0
    pre = [0] * N
    
    for i in range(N - 1):
        for edge in edges:
            node_pre= int(edge[0]) - 1
            node_next = int(edge[1]) - 1
            if dist[node_next] > dist[node_pre] + edge[2]:
                pre[node_next] = node_pre
                dist[node_next] = dist[node_pre] + edge[2]
    
    exist = False
    
    for edge in edges:
        node_pre= int(edge[0]) - 1
        node_next = int(edge[1]) - 1
        if dist[node_next] > dist[node_pre] + edge[2]:
            exist = True
            break
    
    if exist:
        start = int(edge[1]) - 1
        end = int(edge[1]) - 1
        path = [end]
        previous = pre[end]
        path.append(previous)
        while previous != start:
            previous = pre[previous]
            path.append(previous)
        if start != end:
            path.append(start)
        path = [x + 1 for x in path]
        return list(reversed(path))
    else:
        return "none"
