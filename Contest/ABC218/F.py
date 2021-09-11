n, m = map(int, input().split())

st_list = []
v_list = {}
v_list_rev = {}
for i in range(m):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    st_list.append((s, t))
    v_list[s] = v_list.get(s, [])
    v_list[s].append(t)
    v_list_rev[(s, t)] = i

dist = {0: 0}
prev = {}


def dfs(node):
    if node in v_list:
        for next in v_list[node]:
            if next not in dist:
                dist[next] = dist[node] + 1
                prev[next] = node
                dfs(next)


dfs(0)
visitid_list = [n - 1]
tar = n - 1
while tar != 0:
    visitid_list.append(prev[tar])
    tar = prev[tar]

for i in range(m):
    tar_s, tar_t = st_list[i]
    if tar_s in visitid_list and tar_t in visitid_list:
        print("-1")
    else:
        print(dist[n - 1])
