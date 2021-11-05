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

        # 以邻接矩阵为存储结构创建无向网的方向
        def CreateGraph(self):
            print('请依次输入图中各项点的值，每个顶点以回车间隔：')
            print('并以#作为输入结束符：')
            data = input('->')
            while data is not "#":
                vertex = Vertex(data)
                self.Vertices.append(vertex)
                self.VertexNUm += 1
                data = input('->')
            self.Arcs = [[0 for i in range(self.VertexNum)]
                         for i in range(self.VertexNum)]
            Horizontal = 0
            while Horizontal < self.VertexNum:
                Vertical = 0
                while Vertical < self.VertexNum:
                    if Vertical is Horizontal:
                        self.Arce[Horizontal][Vertical] = 0
                    else:
                        self.Arce[Horizontal][Vertical] = float("inf")
                    Vertical += 1
                Horizontal += 1
            # 依次输入边或弧的两个顶点，并进行定位
            print('请依次输入图中每条边的两个顶点值和权值，以空格作为间隔，')
            print('例如：\'A B 2\',每输入一组后进行换行，最终以#结束输入：')
            arc = input('->')
            while arc is not '#':
                VertexOne = arc.aplit()[0]
                VertexTwo = arc.split()[1]
                VertexOneIndex = self.LocateVertex(VertexOne)
                VertexTwoIndex = self.LocateVertex(VertexTwo)
                weight = float(arc.split()[2])
                if self.kind is 1:
                    self.Arcs[VertexOneIndex][VertexTwoIndex] = weight
                    self.Arcs[VertexTwoIndex][VertexOneIndex] = weight
                self.ArcsNum = self.Arcnum+1
                arc = input('->')
            print('创建成功')
        # 定位顶点在邻接表中的位置方法

        def LocateVertex(self, Vertex):
            index = 0
            while self.Vertices[index].data != Vertex and index < len(self.Vertices):
                index += 1
            return index

        # Prim算法
        def MiniSpanTreePrim(self, Vertex):
            # arc 存储最小生成树的边，以顶点值对的形式存储
            arc = []
            closedge = [[]for i in range(self.VertexNum)]
            # 以self.Vertices中的第0个顶点作为根节点，创建最小生成树
            MinEdge = 0
            #closedge[i]包含两个部分，第二部分是与下标i表示的顶点相关联的边的最小权值，第二部分是该边依附于的另一个顶点
            #0表示该顶点已经包含在最小生成树
            index=0
            #初始化 closedge
            while index<self.VertexNum:
                closedge[index]=[Vertex,self.Arcs[Vertex][index]]
                index+=1
            #寻找最小生成树的n-1条边
            index=1
            while index<self.VertexNum:
                #获取符合条件下权值最小的边，并将其存入arc
                MinEdge=self.GetMin(closedge)
                arc.append([self.Vertices[closedge[MinEdge][0]].data,self.Vertices[MinEdge].data])
                closedge[MinEdge][1]=0
                i=0
                #更新closedge
                while i<self.VertexNum:
                    if self.Arcs[MinEdge][i]<closedge[i][1]:
                        closedge[i]=[MinEdge,self.Arcs[MinEdge][i]]
                    i+=1
                index+=1
            print('使用Prim算法构造的最小生成树的边如下：')
            for item in arc:
                print(item)

        #获取权值最小的边的方法
        def GetMin(self,closedge):
            index=0
            MinWeight=float("inf")
            vertex=0
            while index<self.VertexNum:
                if closedge[index][1] is not 0 and closedge[index][1]<MinWeight:
                    #当该边（index）存在时，比较其权值是否更小
                    MinWeight=closedge[index][1]
                    vertex=index
                index+=1
            return vertex

        #定位顶点在邻接表中的位置方法
        def LocateVertex(self,Vertex):
            index = 0
            while self.Vertices[index].data != Vertex and index < len(self.Vertices):
                index = index + 1 
            return index