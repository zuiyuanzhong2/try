#类名称:BinaryTreeNode
#类说明:定义一个二叉树的结点
#类释义:分别有左孩子 LeftChild，右孩子 RightChild 和数据 data
class BinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.LeftChild = None 
        self.RightChild = None
class TreeState(object):
    def __init__(self,BinaryTreeNode,VisitedFlag):
        self.BinaryTreeNode = BinaryTreeNode
        self.VisitedFlag = VisitedFlag

# 类说明:定义一个二叉树
class BinaryTreeNonRecursive(BinaryTreeNode): 
# 创建二叉树的函数
    def CreateBinaryTree(self, Root):
        data = input('->')
        if data == '#':
            Root = None
        else:
            Root.data = data
            Root.LeftChild = BinaryTreeNode()
            self.CreateBinaryTree(Root.LeftChild)
            Root.RightChild = BinaryTreeNode() 
            self.CreateBinaryTree(Root.RightChild)

#先序遍历非递归算法一（按照实验要求里的另一种算法的思想写成）
    def PreOrderNonRecursive1(self, Root):
        StackTreeNode = []
        tTreeNode = Root
        StackTreeNode.append(tTreeNode)
        while len(StackTreeNode) >0:
            #将栈顶元素弹出并访问
            tTreeNode=StackTreeNode.pop() 
            self.VisitBinaryTreeNode(tTreeNode)
            #若tTreeNode有右孩子，就将其入栈
            if tTreeNode.RightChild != "#"and  tTreeNode.RightChild  is not None:
                StackTreeNode.append(tTreeNode.RightChild)
            #若tTreeNode有左孩子，也将其入栈
            if tTreeNode.LeftChild != "#"and tTreeNode.LeftChild != None:
                StackTreeNode.append(tTreeNode.LeftChild)


#先序遍历非递归算法二
    def PreOrderNonRecursive2(self,Root):
        StackTreeNode=[]
        tTreeNode=Root
        while len(StackTreeNode)>0 or tTreeNode is not None:   #空①
            while tTreeNode is  not None:
                self.VisitBinaryTreeNode(tTreeNode)
                StackTreeNode.append(tTreeNode)     #空②
                tTreeNode=tTreeNode.LeftChild        #空③
            if len(StackTreeNode)>0:
                tTreeNode=StackTreeNode.pop()        #空④
                tTreeNode=tTreeNode.RightChild

        

    def VisitBinaryTreeNode(self, BinaryTreeNode):
        # 值为#的结点代表空结点
        if BinaryTreeNode.data != '#':
            print(BinaryTreeNode.data, end="")

#非递归遍历二叉树
if __name__ =='__main__':
    btnrn = BinaryTreeNode()
    btrn = BinaryTreeNonRecursive()
    #创建一棵二叉树
    print("******************非递归先序遍历二叉树*****************")
    print('创建一棵二叉树\n')
    print(' A')
    print(' / \\')
    print(' B C')
    print(' / \\ / \\')
    print(' D E F G')
    print(' / \\/')
    print('H IJ')
    print('A B D H # # # E # I # # C F J # # # G # # ')
    print('请按上述序列输入二叉树中各结点的值(#表示空结点)，\
    每输入一个值按回车换行:')
    btrn.CreateBinaryTree(btnrn)
    print ('对二叉树进行非递归前序遍历:')
    #前序遍历二叉树
    print ('一、课本上的方式（实验指导书里代码部分）:')
    btrn.PreOrderNonRecursive2(btnrn)
    print ('\n二、另一种方法（按照实验要求里的另一种算法思想写的）:')
    btrn.PreOrderNonRecursive1(btnrn)