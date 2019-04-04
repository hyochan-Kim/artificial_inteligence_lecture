from heapq import *

def heuristic(a,b):
    (x1,y1)=a
    (x2,y2)=b
    return abs(x1-x2) + abs(y1-y2)


def first_floor(maze,start,key,end,m,n):
    length=0
    time=0
    can_go = [(0,1),(1,0),(-1,0),(0,-1)]
    came_from ={}
    gdistance = {start:0}
    fdistance = {start:heuristic(start,key)}
    came_from[start]=None
    close_set = set()
    heap = []

    heappush(heap, (heuristic(start,key)+0, start))

    while heap:

        now = heappop(heap)[1]
        time=time+1
        if now == key:
            maze[now[0]][now[1]]=5
            while came_from[now]!=start:
                now=came_from[now]
                maze[now[0]][now[1]]=5
                length=length+1
            length=length+1
            break;

        close_set.add(now)
        for i,j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and new_distance >= gdistance.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1] for i in heap]:
                gdistance[neighbor] = new_distance
                fdistance[neighbor] = new_distance + heuristic(neighbor,key)
                came_from[neighbor] = now
                heappush(heap, (fdistance[neighbor], neighbor))

    came_from2 = {}
    gdistance2 = {key: 0}
    fdistance2 = {key: heuristic(key, end)}
    came_from2[key] = None
    close_set2 = set()
    heap2 = []

    heappush(heap2, (fdistance2[key], key))

    while heap2:

        now = heappop(heap2)[1]
        time=time+1
        if now == end:
            now=came_from2[now]
            length=length+1
            maze[now[0]][now[1]]=5
            while came_from2[now]!=key:
                now=came_from2[now]
                maze[now[0]][now[1]]=5
                length=length+1
            maze [key[0]][key[1]]=5
            length=length+1
            break;

        close_set2.add(now)
        for i, j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance2[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
            if neighbor in close_set2 and new_distance >= gdistance2.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1]for i in heap2]:
                came_from2[neighbor] = now
                gdistance2[neighbor] = new_distance
                fdistance2[neighbor] = new_distance + heuristic(neighbor, key)
                heappush(heap2, (fdistance2[neighbor], neighbor))

    fw = open("first_floor_output.txt", 'w')
    for i in range(m) :
        for j in range(m):
            fw.write(str(maze[i][j])+" ")
        fw.write("\n")

    fw.write("---\n")
    fw.write("length = {0} \ntime = {1}".format(length,time))
    fw.close()


def second_floor(maze,start,key,end,m,n):
    length=0
    time=0
    can_go = [(0,1),(1,0),(-1,0),(0,-1)]
    came_from ={}
    gdistance = {start:0}
    fdistance = {start:heuristic(start,key)}
    came_from[start]=None
    close_set = set()
    heap = []

    heappush(heap, (heuristic(start,key)+0, start))

    while heap:

        now = heappop(heap)[1]
        time=time+1
        if now == key:
            maze[now[0]][now[1]]=5
            while came_from[now]!=start:
                now=came_from[now]
                maze[now[0]][now[1]]=5
                length=length+1
            length=length+1
            break;

        close_set.add(now)
        for i,j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and new_distance >= gdistance.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1] for i in heap]:
                gdistance[neighbor] = new_distance
                fdistance[neighbor] = new_distance + heuristic(neighbor,key)
                came_from[neighbor] = now
                heappush(heap, (fdistance[neighbor], neighbor))

    came_from2 = {}
    gdistance2 = {key: 0}
    fdistance2 = {key: heuristic(key, end)}
    came_from2[key] = None
    close_set2 = set()
    heap2 = []

    heappush(heap2, (fdistance2[key], key))

    while heap2:

        now = heappop(heap2)[1]
        time=time+1
        if now == end:
            now=came_from2[now]
            length=length+1
            maze[now[0]][now[1]]=5
            while came_from2[now]!=key:
                now=came_from2[now]
                maze[now[0]][now[1]]=5
                length=length+1
            maze [key[0]][key[1]]=5
            length=length+1
            break;

        close_set2.add(now)
        for i, j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance2[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
            if neighbor in close_set2 and new_distance >= gdistance2.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1]for i in heap2]:
                came_from2[neighbor] = now
                gdistance2[neighbor] = new_distance
                fdistance2[neighbor] = new_distance + heuristic(neighbor, key)
                heappush(heap2, (fdistance2[neighbor], neighbor))

    fw = open("second_floor_output.txt", 'w')
    for i in range(m) :
        for j in range(m):
            fw.write(str(maze[i][j])+" ")
        fw.write("\n")

    fw.write("---\n")
    fw.write("length = {0} \ntime = {1}".format(length,time))
    fw.close()



def third_floor(maze,start,key,end,m,n):
    length=0
    time=0
    can_go = [(0,1),(1,0),(-1,0),(0,-1)]
    came_from ={}
    gdistance = {start:0}
    fdistance = {start:heuristic(start,key)}
    came_from[start]=None
    close_set = set()
    heap = []

    heappush(heap, (heuristic(start,key)+0, start))

    while heap:

        now = heappop(heap)[1]
        time=time+1
        if now == key:
            maze[now[0]][now[1]]=5
            while came_from[now]!=start:
                now=came_from[now]
                maze[now[0]][now[1]]=5
                length=length+1
            length=length+1
            break;

        close_set.add(now)
        for i,j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and new_distance >= gdistance.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1] for i in heap]:
                gdistance[neighbor] = new_distance
                fdistance[neighbor] = new_distance + heuristic(neighbor,key)
                came_from[neighbor] = now
                heappush(heap, (fdistance[neighbor], neighbor))

    came_from2 = {}
    gdistance2 = {key: 0}
    fdistance2 = {key: heuristic(key, end)}
    came_from2[key] = None
    close_set2 = set()
    heap2 = []

    heappush(heap2, (fdistance2[key], key))

    while heap2:

        now = heappop(heap2)[1]
        time=time+1
        if now == end:
            now=came_from2[now]
            length=length+1
            maze[now[0]][now[1]]=5
            while came_from2[now]!=key:
                now=came_from2[now]
                maze[now[0]][now[1]]=5
                length=length+1
            maze [key[0]][key[1]]=5
            length=length+1
            break;

        close_set2.add(now)
        for i, j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance2[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
            if neighbor in close_set2 and new_distance >= gdistance2.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1]for i in heap2]:
                came_from2[neighbor] = now
                gdistance2[neighbor] = new_distance
                fdistance2[neighbor] = new_distance + heuristic(neighbor, key)
                heappush(heap2, (fdistance2[neighbor], neighbor))

    fw = open("third_floor_output.txt", 'w')
    for i in range(m) :
        for j in range(m):
            fw.write(str(maze[i][j])+" ")
        fw.write("\n")

    fw.write("---\n")
    fw.write("length = {0} \ntime = {1}".format(length,time))
    fw.close()


def fourth_floor(maze,start,key,end,m,n):
    length=0
    time=0
    can_go = [(0,1),(1,0),(-1,0),(0,-1)]
    came_from ={}
    gdistance = {start:0}
    fdistance = {start:heuristic(start,key)}
    came_from[start]=None
    close_set = set()
    heap = []

    heappush(heap, (heuristic(start,key)+0, start))

    while heap:

        now = heappop(heap)[1]
        time=time+1
        if now == key:
            maze[now[0]][now[1]]=5
            while came_from[now]!=start:
                now=came_from[now]
                maze[now[0]][now[1]]=5
                length=length+1
            length=length+1
            break;

        close_set.add(now)
        for i,j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and new_distance >= gdistance.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1] for i in heap]:
                gdistance[neighbor] = new_distance
                fdistance[neighbor] = new_distance + heuristic(neighbor,key)
                came_from[neighbor] = now
                heappush(heap, (fdistance[neighbor], neighbor))

    came_from2 = {}
    gdistance2 = {key: 0}
    fdistance2 = {key: heuristic(key, end)}
    came_from2[key] = None
    close_set2 = set()
    heap2 = []

    heappush(heap2, (fdistance2[key], key))

    while heap2:

        now = heappop(heap2)[1]
        time=time+1
        if now == end:
            now=came_from2[now]
            length=length+1
            maze[now[0]][now[1]]=5
            while came_from2[now]!=key:
                now=came_from2[now]
                maze[now[0]][now[1]]=5
                length=length+1
            maze [key[0]][key[1]]=5
            length=length+1
            break;

        close_set2.add(now)
        for i, j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance2[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
            if neighbor in close_set2 and new_distance >= gdistance2.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1]for i in heap2]:
                came_from2[neighbor] = now
                gdistance2[neighbor] = new_distance
                fdistance2[neighbor] = new_distance + heuristic(neighbor, key)
                heappush(heap2, (fdistance2[neighbor], neighbor))

    fw = open("fourth_floor_output.txt", 'w')
    for i in range(m) :
        for j in range(m):
            fw.write(str(maze[i][j])+" ")
        fw.write("\n")

    fw.write("---\n")
    fw.write("length = {0} \ntime = {1}".format(length,time))
    fw.close()


def fifth_floor(maze,start,key,end,m,n):
    length=0
    time=0
    can_go = [(0,1),(1,0),(-1,0),(0,-1)]
    came_from ={}
    gdistance = {start:0}
    fdistance = {start:heuristic(start,key)}
    came_from[start]=None
    close_set = set()
    heap = []

    heappush(heap, (heuristic(start,key)+0, start))

    while heap:

        now = heappop(heap)[1]
        time=time+1
        if now == key:
            maze[now[0]][now[1]]=5
            while came_from[now]!=start:
                now=came_from[now]
                maze[now[0]][now[1]]=5
                length=length+1
            length=length+1
            break;

        close_set.add(now)
        for i,j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and new_distance >= gdistance.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1] for i in heap]:
                gdistance[neighbor] = new_distance
                fdistance[neighbor] = new_distance + heuristic(neighbor,key)
                came_from[neighbor] = now
                heappush(heap, (fdistance[neighbor], neighbor))

    came_from2 = {}
    gdistance2 = {key: 0}
    fdistance2 = {key: heuristic(key, end)}
    came_from2[key] = None
    close_set2 = set()
    heap2 = []

    heappush(heap2, (fdistance2[key], key))

    while heap2:

        now = heappop(heap2)[1]
        time=time+1
        if now == end:
            now=came_from2[now]
            length=length+1
            maze[now[0]][now[1]]=5
            while came_from2[now]!=key:
                now=came_from2[now]
                maze[now[0]][now[1]]=5
                length=length+1
            maze [key[0]][key[1]]=5
            length=length+1
            break;

        close_set2.add(now)
        for i, j in can_go:
            neighbor = now[0] + i, now[1] + j
            new_distance = gdistance2[now] + 1

            if 0 <= neighbor[0] < m:
                if 0 <= neighbor[1] < n:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
            if neighbor in close_set2 and new_distance >= gdistance2.get(neighbor,0):
                continue

            if new_distance < gdistance.get(neighbor,0) or neighbor not in [i[1]for i in heap2]:
                came_from2[neighbor] = now
                gdistance2[neighbor] = new_distance
                fdistance2[neighbor] = new_distance + heuristic(neighbor, key)
                heappush(heap2, (fdistance2[neighbor], neighbor))

    fw = open("fifth_floor_output.txt", 'w')
    for i in range(m) :
        for j in range(m):
            fw.write(str(maze[i][j])+" ")
        fw.write("\n")

    fw.write("---\n")
    fw.write("length = {0} \ntime = {1}".format(length,time))
    fw.close()


for what_floor in range (5):
    file_list = ("first_floor.txt","second_floor.txt","third_floor.txt","fourth_floor.txt","fifth_floor.txt")
    fr=open(file_list[what_floor], "r")
    line = fr.readline()
    spline=line.split()
    floor=int(spline[0])
    m=int(spline[1])
    n=int(spline[2])
    splines=[]
    lines = fr.readlines()
    fr.close()
    for line in lines:
        splines = splines+line.split()
    maze = [[0]*n for i in range(m)]
    for i in range(m) :
        for j in range(m):
            maze[i][j] = int(splines[i*n+j])
            if (maze[i][j]==6):
                key=(i,j)

            if (maze[i][j]==4):
                end=(i,j)

            if (maze[i][j]==3):
                start=(i,j)
    if (what_floor==0):
        first_floor(maze,start,key,end,m,n)
    if (what_floor==1):
        second_floor(maze,start,key,end,m,n)
    if (what_floor==2):
        third_floor(maze,start,key,end,m,n)
    if (what_floor==3):
        fourth_floor(maze,start,key,end,m,n)
    if (what_floor==4):
        fifth_floor(maze,start,key,end,m,n)

