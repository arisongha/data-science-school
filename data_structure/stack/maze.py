from stack_linked_list import LStack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        if not self.head:
            return True
        return False

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next =self.head
        self.head = new_node
    
    def traverse(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next


class Position:
    def __init__(self, row, col, dir):
        self.row = row
        self.col = col
        self.dir = dir


class MazeSolver:
    direction=((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    def __init__(self, maze):
        self.maze=maze
        self.EXIT_ROW = len(maze)
        self.EXIT_COL = len(maze[0])
        
        # colomn 맨앞, 맨뒤에 벽(1) 추가 
        for row in maze:
            row.insert(0, 1)
            row.append(1)
        
        # row 맨위, 맨아래에 벽(1) 추가
        added_row = [1 for _ in range(self.EXIT_COL+2)]
        maze.insert(0, added_row)
        maze.append(added_row)

        self.path = LinkedList()

    def get_path(self):
        #임시적으로 경로를 담을 스택
        stack = LStack()
        #방문 여부를 판단하기 위한 행렬
        mark=[]
        for _ in range(self.EXIT_ROW+2):
            mark.append([0 for _ in range(self.EXIT_COL+2)])
        
        #row, col : 현재 행과 열
        #dir : 다음에 이동할 방향
        #next_row, next_col : 다음에 이동할 위치
        #found 최종 목적지 도착 여부
        row=None; col=None; dir=None; next_row=None; next_col=None; found=False
    
        #출발점을 mark에 표시함
        #to do
        mark[1][1]=1
        #현재 position을 스택에 push
        #방향은 direction[2] 즉 동쪽
        #to do
        stack.push(Position(1,1,2))
        
        #스택이 비어있지 않고 도착지를 찾지 못했다면
        while not stack.empty() and not found: #to do
            #스택에서 Position 하나를 꺼내온다
            #row, col, dir을 Position 값에서 읽어온다.
            #to do
            pos = stack.pop()
            row = pos.row
            col = pos.col
            dir = pos.dir

            #모든 방향을 탐색하지 않았고 
            #아직 도착지를 찾지 못했다면
            while dir < 8 and not found:
                #next_row와 next_col을 구한다
                #to do
                next_row = row + self.direction[dir][0]
                next_col = col + self.direction[dir][1]

                #next_row와 next_col이 도착지에 도달했다면
                if next_row == self.EXIT_ROW and next_col == self.EXIT_COL:#to do
                    #found를 True로 바꾼다
                    #to do
                    found = True
                    #스택에 현재 위치와 도착지 위치를 push
                    #to do
                    stack.push(Position(row,col,dir))
                    stack.push(Position(self.EXIT_ROW, self.EXIT_COL, 0))
                    
                
                #다음 위치(next_row, next_col)가 미로의 벽이 아니고 도착 전이라면
                elif self.maze[next_row][next_col] == 0 and mark[next_row][next_col] == 0:#to do
                    #다음 위치를 mark에 방문했다고 체크.
                    #to do
                    mark[next_row][next_col] = 1
                    
                    #현재 위치를 스택에 push
                    #to do
                    pos.row = row
                    pos.col = col
                    pos.dir = dir
                    stack.push(Position(row, col, dir))
                    #다음 위치로 이동
                    #to do
                    row = next_row
                    col = next_col
                    dir = 0
                    
                else:
                    #방향을 하나 늘려준다.
                    #to do
                    dir += 1
        
        #목적지를 찾았으면
        if found:
            #stack에서 꺼내 링크드 리스트에 저장한다. 
            while not stack.empty():
                self.path.add(stack.pop())
        else:
            print('There is no path in this maze!')

    def print_path(self):
        g = self.path.traverse()
        for node in g:
            print("({}, {})".format(node.data.row, node.data.col))

    def show_maze(self):
        print('   ', end='')
        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')
        print()

        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')

            for j in range(self.EXIT_COL+2):
                if self.maze[i][j] == 0:
                    print(' O ', end='')
                else:
                    print(' # ', end='')
            print()
        print()

    def show_path(self):
        path_set = set()
        g=self.path.traverse()
        for node in g:
            path_set.add((node.data.row, node.data.col))
        
        print('   ', end='')
        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')
        print()

        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')

            for j in range(self.EXIT_COL+2):
                if (i, j) in path_set:
                    print(' P ', end='')
                elif self.maze[i][j] == 0:
                    print(' O ', end='')
                else:
                    print(' # ', end='')
            print()
        print()


maze = [
		[0, 1, 1, 0, 0],
		[1, 0, 0, 1, 1],
		[0, 1, 1, 0, 1],
		[0, 1, 0, 1, 1],
		[1, 1, 0, 0, 0],
    ]

maze_solver = MazeSolver(maze)
maze_solver.show_maze()
maze_solver.get_path()
maze_solver.print_path()
maze_solver.show_path()
