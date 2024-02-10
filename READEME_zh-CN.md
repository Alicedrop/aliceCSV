
# aliceCSV -- 一个简洁易用的csv模块

aliceCSV`是一个用于操作CSV文件的Python模块，基于RFC 4180标准，将CSV文件作为一个二维列表进行操作。它易于使用，没有任何依赖库。

这个模块可以把CSV文件转化二维列表进行操作，并且可以轻易地把它们转换成其他形式。



aliceCSV对于不完全兼容RFC 4180或格式错误的csv文件有着强大的兼容能力。

例如，如果有这样一个名称为“sheet.csv”的CSV文件：

```
avc,"She said,"I like orange juice.""
```

根据RFC 4180中对CSV的定义7，这种表达是错误的，因为在这个被双引号括起来的字段中，双引号必须要用另一个双引号转义。

实际上，这个csv文件这样表达才是正确的。

```
avc,"She said,""I like orange juice."""
```

如果你用Excel打开这个错误的csv文件，它会被识别为

> | avc  | She said,I like orange juice."" |
> | ---- | ------------------------------- |

然而，aliceCSV对这两个文件都能识别出CSV文件作者的实际要表达的意思：

```python
from aliceCSV import *
myFile = open("sheet.csv", encoding="utf-8")
print(csvTo2dTable(myFile))
```

这将会输出以下结果：

> [['avc', 'She said,"I like orange juice."']]

不必担心这种兼容会影响正常的读取——举个例子，如果要表达上面Excel读取出的错误的结果，也不应该是那种错误的写法，这种什么都不是的写法只能通过解读程序猜测来读取，至于猜成什么，因文本、解读程序的不同，也是不确定的。aliceCSV只是根据常见错误，选择猜成比较可能是作者真实意图的结果进行输出罢了。

# 如何安装

pip

```
pip install aliceCSV
```

即可成功安装。

或者，你可以从源代码安装.



## 功能

- `indexOfStr(target: str, string: str)`: 获取字符串在容器字符串中出现的索引。
- `csvLineToList(line: str, delimiter=",")`: 将CSV文件的一行拆分为列表。
- `csvTo2dTable(file, delimiter=",")`: 将CSV文件转换为二维列表。
- `fixLineLength(csv_sheet)`: 根据RFC 4180标准修复CSV文件中行的长度。
- `tableToCSV(sheet, output_path, sheet_encoding="utf-8", delimiter=",", line_break="\n")`: 将二维列表输出为CSV文件。



## 使用示例

### 1.基于一个csv文件创建二维表

```
csvTo2dTable(file, [optional]delimiter)
```

`file：目标CSV文件的_io.BufferedReader 对象，通过open()创建。`

`delimiter : CSV文件的分隔符，可以不给，默认为","。`



例如，有这样一个文件"sheet.csv"。

```plain text
Name,Age,City
Alice,25,New York
Bob,30,San Francisco
Charlie,22,Los Angeles
```

使用 `csvTo2dTable()` 把这个CSV打开为二维列表进行操作：

```python
from aliceCSV import csvTo2dTable

file_path = "sheet.csv"

# Using default delimiter (`,`), you can omit the delimiter parameter
table = csvTo2dTable(open(file_path))

print(table)
```



**注意**

1.如果你发现无法正确处理像这样的CSV文件，这可能是因为在分隔符","后面多了一个空格，所以实际上分隔符是", "。

```
name, gender, height, address
John, male, 175cm, "123 Main Street, New York, USA"
Emily, female, 160cm, "45 Oxford Road, London, UK"
Michael, male, 180cm, "10 Rue de la Paix, Paris, France"
Sophia, female, 165cm, "25 Alexanderplatz, Berlin, Germany"
```

如果希望修复这种CSV文件或了解更多，你可以看第四点  [**4.Convert CSV files into other formats**](https://github.com/Alicedrop/aliceCSV#4.Convert CSV files into other formats) .

### 2.把二维列表转换为CSV文件

```
TableToCsv(sheet, [optional]output_path, [optional]sheet_encoding, [optional]delimiter, [optional]line_break)
```

`sheet: 一个二维列表。`

`output_path: 输出路径。可以不填，默认为在当前目录下创建"output.csv"。`

`sheet_encoding:  输出文件的编码格式。可以不填，默认为“utf-8"。`

`delimiter:  CSV文件所使用的分隔符。可以不填，默认为","。`

`line_break: 输出文件使用的换行符。可以不填，默认为"\n"。`

通过以下代码可以用`tableToCSV()`函数把二维列表转换为二维列表。

```python
from aliceCSV import tableToCsv

# Example two-dimensional list

table = [['Name', 'Age', 'City'],
         ['Alice', 25, 'New York'],
         ['Bob', 30, 'San Francisco'],
         ['Charlie', 22, 'Los Angeles']]

tableToCSV(table)
```

运行后会在本地输出如图所示的"output.csv"

![image](https://github.com/Alicedrop/aliceCSV/assets/128953967/fd302b28-7619-4e49-a0e8-6b26989346fa)



### 3.修复CSV文件或二维列表的长度

```
fixLineLength(CSV_sheet)
```

`CSV_sheet: 一个打开为二维列表格式的CSV文件。`



使用`fixLineLength()`函数可以根据RFC 4180标准修复CSV文件中行的长度。该函数会检查每一行的字段数目，如果某行的字段数目少于最大字段数目，则会在该行的末尾添加空字段，以保证每一行的字段数目相同。

```python
from aliceCSV import fixLineLength, csvTo2dTable, tableToCSV

# Example CSV file: sheet.csv
file_path = "sheet.csv"

# Open the CSV file as a two-dimensional list
file = open(file_path)
table = csvTo2dTable(file)

# Fix the line lengths of the CSV file
fixed_table = fixLineLength(table)

# Output the result
output_file = tableToCSV(fixed_table)
```

替换`"sheet.csv"`为实际的CSV文件路径。



### 4.转换为其他格式的CSV文件

一些CSV文件使用逗号之外的符号为分隔符。

下面这个"space.csv"，在两个字段之间有一个空格，这意味着它的分隔符是", "，一个逗号加上一个空格。

```
name, gender, height, address
John, male, 175cm, "123 Main Street, New York, USA"
Emily, female, 160cm, "45 Oxford Road, London, UK"
Michael, male, 180cm, "10 Rue de la Paix, Paris, France"
Sophia, female, 165cm, "25 Alexanderplatz, Berlin, Germany"
```

aliceCSV 可以轻易地转换它们。

```
fixCSV(path, [optional]output_path, [optional]origin_delimiter,[optional]target_delimiter, [optional]origin_encoding)
```

`path: 输入的初始CSV文件路径.`

`output_path: 输出生成的CSV文件的路径。可以不填，默认为“output.csv”.`

`origin_delimiter：原始CSV文件的分隔符。它可以省略，默认值为“，”`

`target_delimiter：输出文件中使用的分隔符。它可以省略，默认值为“，”`

`origin_encoding：原始文件的编码。它可以省略，默认值为“utf-8”`

`target_encoding：输出文件中使用的编码。它可以省略，默认值为“utf-8”`

`target_line_break：输出文件的换行符。它可以省略，默认值为“\n”`



可以像这样使用 `fixCSV()` 把CSV文件转换为其他分隔格式的CSV文件

```python
from aliceCSV import fixCSV
fixCSV("space.csv", origin_delimiter=", ", target_delimiter=",")
```

上面的代码会生成内容如下的“output.csv"文件。

![image](https://github.com/Alicedrop/aliceCSV/assets/128953967/73dad0cb-cc60-4636-808f-0142e2765384)





## 许可证

本项目采用MIT许可证。详细信息请参阅 [LICENSE](http://geekaichat.site/LICENSE) 文件。
