from collections import deque


# https://blog.csdn.net/weixin_40953222/article/details/80544928?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# 第一步构建图的关系
graph = {}
graph["v0"] = ["v2", "v1", "v3"]
graph["v2"] = ["v4"]
graph["v1"] = ["v4", "v5"]
graph["v3"] = ["v5"]
graph["v4"] = ["v6"]
graph["v5"] = ["v6"]

# 查找
def bfs(start_node, search_key):
    search_queue = deque()
    visited = set()
    search_queue += graph[start_node]
    while search_queue:
        next = search_queue.popleft()
        if next not in visited:
            if next == search_key:
                print("find key -> ", search_key)
                break
            else:
                search_queue += graph[next]
                visited.add(next)


bfs("v0", "v3")
