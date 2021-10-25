

class SequenceStack:
    # 初始化栈函数
    def __init__(self, Max):
        self.MaxStackSize = Max
        self.s = [None for x in range(0, self.MaxStackSize)]
        self.top = -1
     # 访问某一元素的函数

    def StackVisit(self, element):
        print(element, end='')
    # 判断栈是否为空的函数

    def IsEmptyStack(self):
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        return iTop
    # 元素进栈的函数

    def PushStack(self, x):
        if self.top < self.MaxStackSize-1:
            self.top += 1
            self.s[self.top] = x
        else:
            print("栈满")
            return
    # 元素出栈的函数

    def PopStack(self):
        if self.IsEmptyStack():
            print("栈为空")
            return
        else:
            iTop = self.top
            self.top -= 1
            return self.s[iTop]
    # 遍历栈中元素的函数

    def StackTraverse(self):
        if self.IsEmptyStack():
            print("栈为空")
            return
        else:
            for i in range(0, self.top+1):
                self.StackVisit(self.s[i])
# 二、定义一个处理英文文章的类


class DealArticle:
    def ReadFile(self, strFileName):
        f = open(strFileName)
        str = f.read()
        f.close()
        print("英文文章内容如下：")
        print(str)
        return str
    # 处理文件的内容的函数

    def Deal(self, str):
        i = 0
        while i < len(str):
            if str[i] >= 'a' and str[i] <= 'z':
                i += 1
            elif str[i] >= 'A' and str[i] <= 'Z':
                i += 1
            elif str[i] == ' ':
                i += 1
            else:
                str = str[0:i]+str[i+1:len(str)]
                i += 1
        print("\n文章处理后的内容为：", str)
        return str

# 定义一个找出所有回文单词的类


class TestPD:
    # 默认的初始化测试回文单词类的函数
    def __init__(self):
        self.count = 0
        self.Table = []
    # 提取英文文章中的单词

    def Words(self, str):
        i = 0
        Totalwords = 0
        word = ''
        tag = True
        while i < len(str):
            if (str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z'):
                word = word+str[i]
                i = i+1
                tag = True
            else:
                if tag == True:
                    word = word.lower()
                    self.Plalindrome(word)
                    Totalwords = Totalwords+1
                    word = ""
                tag = False
                i = i+1
        print("该文章的单词总数为:", Totalwords)
        print("该文章中的回文单词总数为:", self.count)
        print("回文单词分别为(若在文章中有大写字母，则此时已转换为小写):", self.Table)
        rate = self.count/Totalwords
        rate = rate*100
        print("该文章的回文率为:", rate, "%")
    # 判断某单词是否为回文单词的函数

    def Plalindrome(self, str):
        st1 = SequenceStack(20)
        st2 = SequenceStack(20)
        i = 0
        while i < (len(str)):
            st1.PushStack(str[i])
            i = i+1
        i = i-1
        while i < (len(str)) and i >= 0:
            st2.PushStack(str[i])
            i = i-1
        tag = 0
        while st1.IsEmptyStack() != True:
            if (st1.PopStack() != st2.PopStack()):
                tag = 1
                return
        if st1.IsEmptyStack() == True and tag == 0:
            self.Table.append(str)
            self.count = self.count+1


if __name__ == '__main__':
    DA = DealArticle()
    str = DA.Deal(DA.ReadFile("./数据结构试验/text.txt"))
    TPD = TestPD()
    TPD.Words(str)
