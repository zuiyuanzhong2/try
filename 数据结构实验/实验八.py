class CircularSequenceQueue:
    # 初始化循环顺序队列的函数
    def __init__(self):
        self.MaxQueueSize = 10
        self.s = [None for x in range(0, self.MaxQueueSize)]
        self.front = 0
        self.rear = 0
    def InitQueue(self,Max):
        self.MaxQueueSize=Max
        self.s=[None for x in range(0,self.MaxQueueSize)] 
        self.front=0
        self.rear=0
    #访问某一元素的函数
    def QueueVisit(self, element):
        print(element, end=' ')
    #判断循环队列是否为空的函数
    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue
    #元素入队的函数
    def EnQueue(self, x):
        if(self.rear+1) % self.MaxQueueSize != self.front:
            self.rear = (self.rear+1) % self.MaxQueueSize
            self.s[self.rear] = x
        else:
            print("队列已满，无法进队")
            return
    #元素出队的函数
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空，无法出队")
            return
        else:
            self.front = (self.front+1) % self.MaxQueueSize
            return self.s[self.front]
    #依次访问队列中元素的函数
    def QueueTraverse(self):
        if self.IsEmptyQueue():
            print("队列为空，无元素可以访问")
            return
        else:
            if self.front < self.rear:
                i = self.front+1
                while i < self.rear:
                    self.QueueVisit(self.s[i])
                    i += 1
                self.QueueVisit(self.s[self.rear])
            else:
                i = self.front+1
                while i < self.MaxQueueSize:
                    self.QueueVisit(self.s[i])
                    i += 1
                i = 0
                while i <= self.rear:
                    self.QueueVisit(self.s[i])
                    i += 1

    #获取队头元素的函数
    def GetHead(self):
        if self.IsEmptyQueue():
            print("队列为空，无法输出队头元素")
            return
        else:
            return self.s[(self.front + 1) % self.MaxQueueSize]


    #输出当前队列中元素个数的函数
    def GetQueueLength(self):
        if self.IsEmptyQueue():
            print("队列为空，队列长度为零")

            return
        else:
            return (self.rear - self.front + self.MaxQueueSize) % self.MaxQueueSize

class Vertex(object):
    def __init__(self, data):
        self.data = data
        self.info = None


class Graph(object):
    def __init__(self, kind):
        self.kind = kind
        self.Vertices = []
        self.Arcs = []
        self.ArcNum = 0
        self.VertexNum = 0

    # 以邻接矩阵为存储结构创建无向网的方法
    def CreateGraph(self):
        print('请依次输入图中各项点的值，每个顶点以回车间隔：')
        print('并以#作为输入结束符：')
        data = input('->')
        while data is not "#":
            vertex = Vertex(data)
            self.Vertices.append(vertex)
            self.VertexNum += 1
            data = input('->')
        self.Arcs = [[0 for i in range(self.VertexNum)]
                     for i in range(self.VertexNum)]
        Horizontal = 0
        while Horizontal < self.VertexNum:
            Vertical = 0
            while Vertical < self.VertexNum:
                if Vertical is Horizontal:
                    self.Arcs[Horizontal][Vertical] = 0
                else:
                    self.Arcs[Horizontal][Vertical] = float("inf")
                Vertical += 1
            Horizontal += 1
        # 依次输入边或弧的两个顶点，并进行定位
        print('请依次输入图中每条边的两个顶点值和权值，以空格作为间隔，')
        print('例如：\'A B 2\',每输入一组后进行换行，最终以#结束输入：')
        arc = input('->')
        while arc is not '#':
            VertexOne = arc.split()[0]
            VertexTwo = arc.split()[1]
            VertexOneIndex = self.LocateVertex(VertexOne)
            VertexTwoIndex = self.LocateVertex(VertexTwo)
            weight = float(arc.split()[2])
            if self.kind is 1:
                self.Arcs[VertexOneIndex][VertexTwoIndex] = weight
                self.Arcs[VertexTwoIndex][VertexOneIndex] = weight
            self.ArcsNum = self.ArcNum+1
            arc = input('->')
        print('创建成功')
    # 定位顶点在邻接表中的位置方法

    def LocateVertex(self, Vertex):
        index = 0
        while self.Vertices[index].data != Vertex and index < len(self.Vertices):
            index += 1
        return index


    def BFSTraverse(self):
        visited=[]
        h=0
        BFENum=1
        Queue=CircularSequenceQueue()
        Queue.InitQueue(10)
        while h<self.VertexNum:
            visited.append('False')
            h+=1
        h=0
        Queue.EnQueue(0)
        print(self.Vertices[0].data)
        visited[0]='True'
        while Queue.IsEmptyQueue() is False:
            tVertex=Queue.DeQueue()
            v = tVertex+1
            while v < self.VertexNum:
                if self.Arcs[tVertex][v]!=float("inf") and visited[v]=='False':
                    print(self.Vertices[v].data)
                    visited[v]='True'
                    BFENum+=1
                    Queue.EnQueue(v)
                v+=1
        if BFENum==self.VertexNum:
            print('该网是连通网')


    # Prim算法
    def MiniSpanTreePrim(self, Vertex):
        # arc 存储最小生成树的边，以顶点值对的形式存储
        arc = []
        closedge = [[]for i in range(self.VertexNum)]
        # 以self.Vertices中的第0个顶点作为根节点，创建最小生成树
        MinEdge = 0
        # closedge[i]包含两个部分，第二部分是与下标i表示的顶点相关联的边的最小权值，第二部分是该边依附于的另一个顶点
        # 0表示该顶点已经包含在最小生成树
        index = 0
        # 初始化 closedge
        while index < self.VertexNum:
            closedge[index] = [Vertex, self.Arcs[Vertex][index]]
            index += 1
        # 寻找最小生成树的n-1条边
        index = 1
        while index < self.VertexNum:
            # 获取符合条件下权值最小的边，并将其存入arc
            MinEdge = self.GetMin(closedge)
            arc.append([self.Vertices[closedge[MinEdge][0]].data,
                       self.Vertices[MinEdge].data])
            closedge[MinEdge][1] = 0
            i = 0
            # 更新closedge
            while i < self.VertexNum:
                if self.Arcs[MinEdge][i] < closedge[i][1]:
                    closedge[i] = [MinEdge, self.Arcs[MinEdge][i]]
                i += 1
            index += 1
        print('使用Prim算法构造的最小生成树的边如下：')
        for item in arc:
            print(item)

    # 获取权值最小的边的方法
    def GetMin(self, closedge):
        index = 0
        MinWeight = float("inf")
        vertex = 0
        while index < self.VertexNum:
            if closedge[index][1] is not 0 and closedge[index][1] < MinWeight:
                # 当该边（index）存在时，比较其权值是否更小
                MinWeight = closedge[index][1]
                vertex = index
            index += 1
        return vertex

    # 定位顶点在邻接表中的位置方法
    def LocateVertex(self, Vertex):
        index = 0
        while self.Vertices[index].data != Vertex and index < len(self.Vertices):
            index = index + 1
        return index

    # 将图中的边按权值的升序排列并存储在一个列表中的方法
    def GetEdges(self, Edges):
        Horizental = 0
        while Horizental < self.VertexNum:
            Vertical = Horizental
            while Vertical < self.VertexNum:
                if self.Arcs[Horizental][Vertical] > 0 and self.Arcs[Horizental][Vertical] < float("inf"):
                    index = 0
                    flag = True
                    while index < len(Edges) and flag:
                        if Edges[index][2] > self.Arcs[Horizental][Vertical]:
                            Edges.insert(index, [
                                         self.Vertices[Horizental].data, self.Vertices[Vertical].data, self.Arcs[Horizental][Vertical]])
                            flag = False
                        index += 1
                    if flag:
                        Edges.append(
                            [self.Vertices[Horizental].data, self.Vertices[Vertical].data, self.Arcs[Horizental][Vertical]])
                Vertical += 1
            Horizental += 1

    def MiniSpanTreeKruskal(self,Edges):
        flag=[[]for i in range(self.VertexNum)]
        index=0
        #初始化顶点标记，其用于判断顶点是否属于同一连接分量
        while index<self.VertexNum:
            flag[index]=index
            index+=1
        index=0
        #访问图中的每一条边
        while index<len(Edges):
            VertexOne=self.LocateVertex(Edges[index][0])
            VertexTwo=self.LocateVertex(Edges[index][1])
            #若边的两个顶点不属于同一连接分量。则该边被保留
            #并将两个顶点划分到同一连接分量
            if flag[VertexOne] is not flag [VertexTwo]:
                FlagOne=flag[VertexOne]
                FlagTwo=flag[VertexTwo]
                limit=0
                while limit<self.VertexNum:
                    if flag[limit] is FlagTwo: 
                        flag[limit] = FlagOne
                    limit = limit+1 
                index = index + 1 
            else:#否则将该边删除
                Edges.pop(index) 
        print('使用 Kruskal 算法构造的最小生成树的边如下:')
        for item in Edges:
            print(item)


# 主程序
if __name__ == '__main__':
    # 创建一个联通的无向网
    graph = Graph(1)
    graph.CreateGraph()
    #广度优先遍历以及判断是否是连通网
    graph.BFSTraverse()
    #以下标为 0 的顶点构造最小生成树(Prim 算法)
    graph.MiniSpanTreePrim(0)

    Edges=[]
    graph.GetEdges(Edges)
     #构造最小生成树(Kruskal 算法)
    graph.MiniSpanTreeKruskal(Edges)

