import random

#生成正序、逆序和随机序列，范围为 1 到 500

positiveseq=[i for i in range(1,501)]
invertedseq=[i for i in range(500,0,-1)]
randomseq=random.sample(positiveseq,500)
#设置三个数据文件的存储路径
#'.'为当前目录
directory='./'
#将正序序列数据存入文件 positivesequence.txt 中
r ="\n".join(str(i) for i in positiveseq)
with open(directory+'positivesequence.txt','a') as wr: 
    wr.write(r) 
#将逆序序列数据存入文件 invertedsequence.txt 中 
r ="\n".join(str(i) for i in invertedseq)
with open(directory+'invertedsequence.txt','a') as wr:
    wr.write(r)
#将随机序列数据存入文件 randomsequence.txt 中
r ="\n".join(str(i) for i in randomseq)
with open(directory+'randomsequence.txt','a') as wr: 
    wr.write(r)


#导入模块 time，用来获取当前时间
import time
#类名称:ListItem
#类说明:定义顺序表中的一个节点
#类释义:定义顺序表中的一个节点
class ListItem(object):
    def __init__(self ,key,value):
        self.key = key
        self.value = value 
#类名称:SSequenceList
#类说明:定义一个顺序表 Array
#类释义:创建一个顺序表 Array，并对其执行相关操作
class SSequenceList(object):
#初始化顺序表函数
    def __init__(self):
        self.SeqList=[] 
    #创建链表函数
    def CreateSequenceListByInput_Seq(self,seq):
        self.SeqList.append(ListItem(int(0), 0))
        with open('./'+seq+'.txt', 'r') as f:
            data = f.readlines()
        i=1
        for line in data:
            self.SeqList.append(ListItem(int(line),i))
            i=i+1

    #冒泡排序
    def BubbleSort(self):
        SeqListLen = len(self.SeqList)
        for i in range(1,SeqListLen-1):
            for j in range(1,SeqListLen-i):
                if self.SeqList[j+1].key < self.SeqList[j].key:  #空⑤（如果当前记录大于下一个纪录）
                    self.SeqList[0].key = self.SeqList[j].key    #使用第一个位置作为中转，完成两者的交换
                    self.SeqList[j].key = self.SeqList[j+1].key  #空⑥（就交换两者的顺序）
                    self.SeqList[j+1].key = self.SeqList[0].key
    
    #快速排序的一趟分区

    def AdjustPartition(self,low,high):
        left=low
        right=high
        self.SeqList[0].key = self.SeqList[left].key
        while left < right:
            while left < right and  self.SeqList[right].key >= self.SeqList[0].key:  #空⑦ 当left<right并且枢轴记录不大于下标为right的记录时
                right = right-1
            self.SeqList[left].key = self.SeqList[right].key
            while left < right and self.SeqList[left].key <= self.SeqList[0].key:    #空⑧ 当left<right并且枢轴记录大于等于下标为left的记录时
                left = left+1
            self.SeqList[right].key = self.SeqList[left].key
        self.SeqList[left].key= self.SeqList[0].key      #空⑨  将枢轴记录的关键字存入下标为left的记录中
        return left
    #快速排序
    def QuickSort(self,low,high):
        if low<high:
            pivot = self.AdjustPartition(low,high)   #空⑩  先进行一次分区
            self.QuickSort(low,pivot-1)               #空⑪  分别对其分成的两个分区再进行分区
            self.QuickSort(pivot+1,high)              #空⑫
    #输出函数
    def PrintOut(self):
        print("***************************************************")
        print("\n(1)对正序序列进行冒泡排序和快速排序所花的时间:")
        try:
            self.__init__() 
        except:
            print("顺序表 Array 初始化失败") 
        self.CreateSequenceListByInput_Seq('positivesequence') 
        t1=time.time()
        self.BubbleSort() #调用冒泡排序算法
        t2=time.time()
        tm=t2-t1 
        print(' 冒泡排序所花的时间为:',tm)
        try:
            self.__init__()
        except:
            print("顺序表 Array 初始化失败")
        self.CreateSequenceListByInput_Seq('positivesequence')
        Len=len(self.SeqList)
        t1=time.time()
        self.QuickSort(0,len(self.SeqList)-1) #调用快速排序算法
        t2=time.time() 
        tk=t2-t1
        print(' 快速排序所花的时间为:',tk) 
        if tm > tk:
            print(' 结论:快速排序所花时间更短')
        else:
            print(' 结论:冒泡排序所花时间更短')
        print("\n(2)对逆序序列进行冒泡排序和快速排序所花的时间:")
        try:
            self.__init__() 
        except:
            print("顺序表 Array 初始化失败")
        self.CreateSequenceListByInput_Seq('invertedsequence')
        t1=time.time()
        self.BubbleSort() #调用冒泡排序算法
        t2=time.time()
        tm=t2-t1
        print(' 冒泡排序所花的时间为:',tm)
        try:
            self.__init__()
        except:
            print("顺序表 Array 初始化失败")
        self.CreateSequenceListByInput_Seq('invertedsequence')
        Len=len(self.SeqList)
        t1=time.time()
        self.QuickSort(0,499) #调用快速排序算法
        t2=time.time()
        tk=t2-t1

        print(' 快速排序所花的时间为:',tk)
        if tm > tk:
            print(' 结论:快速排序所花时间更短') 
        else:
            print(' 结论:冒泡排序所花时间更短')
        print("\n(3)对随机序列进行冒泡排序和快速排序所花的时间:")
        try:
            self.__init__()
        except:
            print("顺序表 Array 初始化失败")
        self.CreateSequenceListByInput_Seq('randomsequence')
        t1=time.time()
        self.BubbleSort() #调用冒泡排序算法
        t2=time.time()
        tm=t2-t1
        print(' 冒泡排序所花的时间为:',tm)
        try:
            self.__init__()
        except:
            print("顺序表 Array 初始化失败")
        self.CreateSequenceListByInput_Seq('randomsequence')
        Len=len(self.SeqList)
        t1=time.time()
        self.QuickSort(0,499) #调用快速排序算法
        t2=time.time()
        tk=t2-t1
        print(' 快速排序所花的时间为:',tk)
        if tm > tk:
            print(' 结论:快速排序所花时间更短')
        else:
            print(' 结论:冒泡排序所花时间更短') 
if __name__ =='__main__':
    Array=SSequenceList()
    Array.PrintOut()