"""
1. 每一行记录位于一个单独的行上，用回车换行符CRLF(也就是\r\n)分割。

2. 文件中的最后一行记录可以有结尾回车换行符，也可以没有。

aaa,bbb,ccc CRLF
zzz,yyy,xxx

4. 在标题头行和普通行每行记录中，会存在一个或多个由半角逗号(,)分隔的字段。整个文件中每行应包含相同数量的字段，空格也是字段的一部分，不应被忽略。每一行记录最后一个字段后不能跟逗号。（通常用逗号分隔，也有其他字符分隔的CSV，需事先约定）

5. 每个字段可用也可不用半角双引号(“)括起来（不过有些程序，如Microsoft的Excel就根本不用双引号）。如果字段没有用引号括起来，那么该字段内部不能出现双引号字符。
"aaa","bbb","ccc" CRLF
zzz,yyy,xxx
6. 字段中若包含回车换行符、双引号或者逗号，该字段需要用双引号括起来。

Fields containing line breaks (CRLF), double quotes, and commas should be enclosed in double-quotes. For example:（下面原文的例子可能有些问题）

"aaa","b CRLF
bb","ccc" CRLF
zzz,yyy,xxx

7. 如果用双引号括字段，那么出现在字段内的双引号前必须加一个双引号进行转义。





"""


def indexOfStr(string: str, container: str):
    """
    用于获取字符串string在容器字符串container出现的索引，以一个列表的形式返回所有出现位置。
    python内置了四个寻找的函数，find()返回首次出现的索引，没有则返回-1；index返回首次出现的索引，没有则会报错ValueError: substring not found
    rfind和rindex是反过来从末尾开始查找。
    count是计算出现的次数
    这些都不完全符合要求。因此写一个函数来实现。

    :type string: str
    :param string:要查找的字符串
    :param container:被查找的字符串
    :return:list
    """
    result = []
    if string in container:
        index_to_start = 0  # 一开始从索引0开始，当找到一个
        while 1:
            index = container[index_to_start:].find(string)  # 索引是在要找
            if index == -1:
                break
            else:
                result.append(index + index_to_start)
                index_to_start = index + index_to_start + 1
    return result  # 如果容器中不存在要寻找的字符串，没有进入if，则返回空列表


def csvTo2dSheet(file, mode: str = "standard") -> list:
    """
    将使用open打开的csv文件转为二维列表
    先进行一次遍历，把每一行转换为
    :param file: 使用open()打开的csv文件
    :param mode: standard表示按照标准，origin为保留原格式不进行自动修复
    :return: 二维列
    """
    data: list = file.readlines()
    for i in range(len(data)):
        item = data[i]
        if item[len(item) - 2:len(item)] == "\r\n":  # 注意！！！！！！！！最后两项是len()-2:len()!!!!!!
            '''
            因为是【a,b】取的是索引a:b-1,而长度恰好是因为没有0所以比最大索引多1，所以要取最后一位，b必须得是len（），然后实际就是取最大索引len-1。
            而前一位就是len-2了
            '''
            item = data[:len(item) - 2]  # 因为后两位索引是len-2,len-1，这两个都舍弃，所以就是最大渠道len-3，也就是[:len-2]
        elif item[-1] == "\n":
            item = item[:len(item) - 1]  # [0:len]就是从头到尾，那么[0:len-1]就是从头到倒数第二项
        # 至此去掉了末尾的换行符。
        # 之后就可以丢给分割函数了。

        data[i] = item
        data[i] = csvLineToList(data[i])

    return data


def csvLineToList(line: str) -> list:
    """
    输入一行csv的内容，识别每一列，拆分成列表
    :param line: 准备拆分成列表的csv文件的某一行，是字符串形式
    :return: 返回按列拆分成的列表
    """
    global converted_count
    if not '"' in line:
        converted_count += 1
        print("no \" inside", converted_count)
        return line.split(',')
    else:
        # Plan A
        # 如果是"xxx","abc"之类的，4种：
        # "abc"    像这样只有一项，没有逗号，那就不管它
        # abc",def"      有引号，但是不是表示这个意思的，虽然违反了规则，但是不管它，
        # “abc",def      只有第一项是有引号的，那么就没有 ,"
        # abc,"def"      只有最后一项是有引号的，那么没有 ,"
        # 如果只有一项， 例如 "55"，没有逗号，那就不用分了
        # 只要不是只有一项，那么必有,"  或者 ",的结构其中之一，
        #
        #
        # 但是也要注意不是"",(第七条)，因此通过看"前一个是否是"来判断有效性。直接以有效的位置进行分割。
        # 先找 ,“ 的结构 ，在这引文段应该在
        # 例如 未知用户,太好了！真的有人啊！,"左,分支7"
        # 先以

        pass

        # Plan B
        # 也可以通过左括号右括号的方式来检测。连续的两个"会被视作无效。，那么
        # 从左往右读，读到第一个"，正常来说这个肯定是外引号，因为双双引号只出现在引文内部。
        # (对于不是的异常情况，测试一下excel和pycharm是怎么搞的)
        # 那么从这里开始一个引文段，记下这个索引;往下找下一个引号，找到后看看是不是两个连在一起的转义，是则则是文本，继续，不是则是引文结束，记下索引。
        # 判断下一位是不是,，正常来说应该是(除非是结尾)，如果不是则是原文出错了，也看看别人怎么做。

        # 具体实现的话，可以先用,"


def sheetToCsv(sheet, output_path):
    result = 0

    return result


if __name__ == "__main__":
    converted_count = 0
    print("45")
    myFile = open("第一章_new.csv", encoding="utf-8")
    csvList = csvTo2dSheet(myFile)
    print(csvList)

'''
示例 
hello,w,"125,5",999

而hello",w,"125,5",999
结果是hello"   w   125,5     999

hello"",w,"125,5",999
结果是hello""   w   125,5     999

hello"",w,55"125,5",999
hello""     w    55"125    5"     999

hello"",w,55"125,5"6,999
hello""     w    55"125    5"6     999

hello"123",w,55"125,5"6,999
hello"123"  w   55"125  5"6     999
对于

'''

'''
因此，需要一下几个：
1.删除每行末尾的换行符（根据1.2条）：读取末尾两个，如果是\r\n就舍弃，否则就舍弃最后一个\n或\r。
2.第四条规定每行列数都一样，所以对于不够的会自动补全，除非在origin模式
3.五六七都是说双引号的问题，所以分割为列表先看有没有双引号，没有就直接用逗号分割；


'''
