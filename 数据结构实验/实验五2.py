class StringList:
    def __init__(self):
        self.MaxStringSize = 256
        self.chars = ""
        self.length = 0

    # 判断是否为空的函数
    def IsEmptyString(self):
        if self.length == 0:
            IsEmpty = True
        else:
            IsEmpty = False
        return IsEmpty

    # 创建一个串的函数
    def CreateStringList(self):
        string = input('请输入字符串，按回车键结束：')
        if len(string) > self.MaxStringSize:
            print("输入的字符串的超过分配的内存，超过的部分无法存入。")
            self.chars = string[:self.MaxStringSize]
            self.length = self.MaxStringSize
        else:
            self.chars = string[:]
            self.length = len(self.chars)

    # 输出一个串的字符序列函数
    def StringTraverse(self):
        print(self.chars)

    # 获取串长度的函数
    def GetStringLength(self):
        return self.length

    # 获取串字符序列的函数
    def GetString(self):
        return self.chars

    # 获取模式串ListNext值的函数
    def GetListNextValue(self):
        ListNextVal = [None for x in range(0, 100)]
        ListNextVal[0]=-1
        k=-1
        j=0
        while j<len(self.chars)-1:
            if k==-1 or self.chars[j]==self.chars[k]:
                k+=1
                j+=1
                if self.chars[j]!=self.chars[k]:
                    ListNextVal[j]=k
                else:
                    ListNextVal[j]=ListNextVal[k]
            else:
                k=ListNextVal[k]
        return ListNextVal
    #KMP算法
    def IndexKMP(self,pos,T,ListNext):
        i=pos
        j=0
        length=T.GetStringLength()
        string=T.GetString()
        while i<len(self.chars)and j<length:
            if j==-1 or self.chars[i]==string[j]:
                i+=1
                j+=1
            else:
                j=ListNext[j]
        if j==length:
            print("匹配成功！模式串在主串中首次出现的位置为：",i-length)
        else:
            print("匹配失败！")
class TestIndex:
    def TestIndexKMP(self):
        S=StringList()
        S.CreateStringList()
        print("主串为：",end='')
        S.StringTraverse()
        T=StringList()
        T.CreateStringList()
        print("模式串为：",end='')
        T.StringTraverse()
        pos=int(input('请输入从主串的那一位置开始串的模式匹配：'))
        print("匹配结果：",end='')
        S.IndexKMP(pos,T,T.GetListNextValue())
if __name__=='__main__':
    TI=TestIndex()
    TI.TestIndexKMP()







