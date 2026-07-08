import heapq

class Graph:
    def __init__(self, v):
        self.v = v # number of vertices
        self.adj = [[] for _ in range(v)] # store vertex and weight (distance)

    def add_edge(self, u, v, w):
        # compare weight (distance first), then vertex arrival sequence
        self.adj[u].append((w, v))
        self.adj[v].append((w, u))

    def dijkstra(self, src):
        pq = [(0, src)]

        # create a distance list init with infinite
        dist = [float("inf")] * self.v
        
        # init index src with value 0
        # we start at src, src to src is distance 0
        dist[src] = 0

        while pq:
            
            # get the (weight, u) pair
            cur_dist, u = heapq.heappop(pq)

            # go through the edges of this u (relaxation)
            for weight, v in self.adj[u]:

                # in theory, cur_dist == dist[u]                
                # if dist[v] > weight + cur_dist:
                if dist[v] > weight + dist[u]:                    

                    # we found a shorter distance, update the dist array
                    # push it to the heap
                    dist[v] = weight + dist[u]
                    heapq.heappush(pq, (dist[v], v))

        # print shortest distances
        print("Vertex Distance from Source")
        for i in range(self.v):
            print(f"{i}\t\t{dist[i]}")


if __name__ == "__main__":
    # Create the graph given in the above figure
    v = 6
    g = Graph(v)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)

    g.add_edge(1, 0, 4)
    g.add_edge(1, 2, 2)

    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 4, 1)
    g.add_edge(2, 5, 6)

    g.add_edge(3, 2, 3)
    g.add_edge(3, 5, 2)

    g.add_edge(4, 2, 1)
    g.add_edge(4, 5, 3)

    g.add_edge(5, 2, 6)
    g.add_edge(5, 3, 2)
    g.add_edge(5, 4, 3)

    g.dijkstra(0)