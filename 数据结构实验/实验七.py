from typing import NoReturn
#定义一个二叉树的结点的类

class BinaryTreeNode(object):
    def __init__(self) :
        self.data='#'
        self.LeftChild=None
        self.RightChild=None

class TreeState():
    def __init__(self,Node,a) :
        self.BinaryTreeNode=Node
        self.VisitedFlag=a
        

#定义一个循环队列
class CircularSequenceQueue:
    def __init__(self) :
        self.MaxQueueSize=4
        self.s=[None for x in range(0,self.MaxQueueSize)]
        self.front=0
        self.rear=0
    #初始化循环队列函数
    def InitQueue(self,MaxQueueSize):
        self.MaxQueueSize=MaxQueueSize
        self.s=[None for x in range(0,self.MaxQueueSize)]
        self.front=0
        self.rear=0

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

#二叉树
class BinaryTree(object):
    #用递归创建二叉树
    def CreateBinaryTree(self,Root):
        data=input('->')
        if data =='#':
            Root = None
        else:
            Root.data=data
            Root.LeftChild=BinaryTreeNode()
            self.CreateBinaryTree(Root.LeftChild)
            Root.RightChild=BinaryTreeNode()
            self.CreateBinaryTree(Root.RightChild)
    #遍历二叉树一个结点函数
    def VisitBinaryNode(self,BinaryTreeNode):
        if BinaryTreeNode.data !='#':
            print(BinaryTreeNode.data,end='')

    #先序遍历非递归算法
    def PreOrder(self,Root):
        StackTreeNode=[]
        tTreeNode=Root
        while len(StackTreeNode)>0 or tTreeNode is not None:
            while tTreeNode is  not None:
                self.VisitBinaryNode(tTreeNode)
                StackTreeNode.append(tTreeNode)
                tTreeNode=tTreeNode.LeftChild
            if len(StackTreeNode)>0:
                tTreeNode=StackTreeNode.pop()
                tTreeNode=tTreeNode.RightChild
    #中序遍历二叉树非递归算法
    def InOrder(self,Root):
        StackTreeNode=[]
        tTreeNode=Root
        while len(StackTreeNode)>0 or tTreeNode is not None:
            while tTreeNode is  not None:
                StackTreeNode.append(tTreeNode)
                tTreeNode=tTreeNode.LeftChild
            if len(StackTreeNode)>0:
                tTreeNode=StackTreeNode.pop()
                self.VisitBinaryNode(tTreeNode)
                tTreeNode=tTreeNode.RightChild
    #后序遍历非递归算法（课本）
    def PostOrder(self,Root):
        StackTreeNode=[]
        tBinaryTreeNode=Root
        tTree=None
        while tBinaryTreeNode is not None:
            tTree=TreeState(tBinaryTreeNode,0)
            StackTreeNode.append(tTree)
            tBinaryTreeNode=tBinaryTreeNode.LeftChild
        while len(StackTreeNode)>0:
            tTree=StackTreeNode.pop()
            if tTree.BinaryTreeNode.RightChild is None or tTree.VisitedFlag==1:
                self.VisitBinaryNode(tTree.BinaryTreeNode)
            else:
                StackTreeNode.append(tTree)
                tTree.VisitedFlag=1
                tBinaryTreeNode=tTree.BinaryTreeNode.RightChild
                while tBinaryTreeNode is not None:
                    tTree=TreeState(tBinaryTreeNode,0)
                    StackTreeNode.append(tTree)
                    tBinaryTreeNode=tBinaryTreeNode.LeftChild
    #后序遍历非递归算法（使用两个栈）
    def PostOrder2(self,Root):
        StackTreeNode=[]
        StackTreeNode2=[]
        StackTreeNode.append(Root)
        while len(StackTreeNode)>0:
            tTreeNode=StackTreeNode.pop()
            StackTreeNode2.append(tTreeNode)
            if tTreeNode.LeftChild is not None:
                StackTreeNode.append(tTreeNode.LeftChild)
            if tTreeNode.RightChild is not None:
                StackTreeNode.append(tTreeNode.RightChild) 
        while len(StackTreeNode2)>0:
            if StackTreeNode2[-1].data=='#':
                StackTreeNode2.pop()
            else:
                print(StackTreeNode2.pop().data,end='')
    #层次遍历二叉树的函数
    def LevelOrder(self,Root):
        tSequenceQueue=CircularSequenceQueue()
        tSequenceQueue.InitQueue(100)
        tSequenceQueue.EnQueue(Root)
        tTreeNode=None
        while tSequenceQueue.IsEmptyQueue()==False:
            tTreeNode=tSequenceQueue.DeQueue()
            self.VisitBinaryNode(tTreeNode)
            if tTreeNode.LeftChild is not None:
                tSequenceQueue.EnQueue(tTreeNode.LeftChild)
            if tTreeNode.RightChild is not None:
                tSequenceQueue.EnQueue(tTreeNode.RightChild)
    #修改指定节点值算法
    def ModifyNode(self,Root):
        if Root is not None:
            self.FindNodeF(Root)
            self.ModifyNode(Root.LeftChild)
            self.ModifyNode(Root.RightChild)
    #查找结点F算法
    def FindNodeF(self,BinaryTreeNode):
        if BinaryTreeNode.data=='F':
            BinaryTreeNode.data='Z'

    #插入指定节点值算法
    def InsertNode(self,Root):
        if Root is not None:
            self.FindNodeG(Root)
            self.InsertNode(Root.LeftChild)
            self.InsertNode(Root.RightChild)
    #查找结点G的算法
    def FindNodeG(self,Node):
        if Node.data=='G':
            Node.RightChild=BinaryTreeNode()        
            Node.RightChild.data='K'

    #输出函数
    def PrintOut(self):
        print("*****************************")
        print("****实现二叉树的各种操作******")
        print("\n(1)初始化根结点:", end="")
        try:
            self.__init__()
            print("树初始化成功!")
        except:
            print("树初始化失败!")
        print("\n(2)递归算法创建一棵树。")
        print('创建一棵二叉树\n')
        print(' A')
        print(' / \\')
        print(' B C')
        print(' / \\ / \\')
        print(' D E F G')
        print(' / \\/')
        print('H IJ')
        print('A B D H # # # E # I # # C F J # # # G # # ')
        # 创建一棵二叉树
        print('请仿照上述序列，输入某一二叉树中各结点的值(#表示空结点)，\
        每输入一个值按回车换行:')
        try:
            self.CreateBinaryTree(bTN)
            print("二叉树创建完成!") 
        except ValueError:
            print("输入有误，请重新输入!")
            self.CreateBinaryTree(bTN)
        print("\n(3)对二叉树进行前序遍历:")
        try:
            self.PreOrder(bTN)
        except ValueError:
            print("遍历出错!")
        print("\n\n(4)对二叉树进行中序遍历:") 
        try:
            self.InOrder(bTN)
        except ValueError:
            print("遍历出错!")
        print("\n\n(5)对二叉树进行后序遍历(课本):")
        try:
            self.PostOrder(bTN)
        except ValueError:
            print("遍历出错!")
        print("\n\n(5.2)对二叉树进行后序遍历(用两个栈):")
        try:
            self.PostOrder2(bTN)
        except ValueError:
            print("遍历出错!")
        print("\n\n(6)对二叉树进行层次遍历:")
        try:
            self.LevelOrder(bTN) 
        except ValueError:
            print("遍历出错!")
        print("\n\n(7)获取值为 F 的结点，并将其值修改为 Z。")
        try:
            self.ModifyNode(bTN) 
        except ValueError:
            print("修改出错!")
        print("修改 F 后的二叉树前序遍历结果为:") 
        self.PreOrder(bTN)
        print("\n\n(8)为值为 G 的结点添加右孩子，令其值为 K。")
        try:
            self.InsertNode(bTN)
        except ValueError:
            print("插入出错!")
        print("插入后的二叉树前序遍历结果为:")
        self.PreOrder(bTN)
                
if __name__ == '__main__': 
    bTN = BinaryTreeNode() 
    bT = BinaryTree()
    bT.PrintOut()
