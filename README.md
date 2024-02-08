# aliceCSV -- A concise and easy-to-use csv module   

**aliceCSV -- 一个简洁易用的csv模块**

==这是英文介绍，中文介绍请看[中文文档](https://github.com/Alicedrop/aliceCSV/blob/main/readme_zh-CN.md)==

This module can operate CSV file **as two-dimensional table** and be able to **convert them** into other forms easily.



aliceCSV has **strong compatibility** with CSVs that does not comply with RFC 4180 or be in incorrect formats.

For example, if there is a file named "sheet.csv" and the following is its content.

```
avc,"She said,"I like orange juice.""
```

That is wrong.

According to RFC 4180 Definition 7, it's incorrect because the double-quote inside the second field must be escaped by preceding it with another double quote.

So the correct version is as following.

```
avc,"She said,""I like orange juice."""
```



If you try to open the wrong one in Excel, it will be interpreted into that one.

> | avc  | She said,I like orange juice."" |
> | ---- | ------------------------------- |



However, aliceCSV can correctly identify the author's true intention for both of them.

```python
from aliceCSV import *
myFile = open("sheet.csv", encoding="utf-8")
print(csvTo2dTable(myFile))
```

It will output  the following result.

> [['avc', 'She said,"I like orange juice."']]

And don't worry this will misunderstand you meaning —— 

## Install

You can use pip to install it.

pip install aliceCSV

or clone this 

## How to use

### 1.Create a two-dimonsion table basing on a csv file

```
csvTo2dTable(file, [optional]delimiter)
```

`file：an _io.BufferedReader of the targeted csv file, which is created by open() a csv file`

`delimiter : The delimiter used in the CSV file. This parameter can be omitted, with the default value being “,”.`



For example, there is a file named "sheet.csv".

```plain text
Name,Age,City
Alice,25,New York
Bob,30,San Francisco
Charlie,22,Los Angeles
```

To open a CSV file as a two-dimensional list using the `csvTo2dTable()` function, you can follow this format:

```python
from aliceCSV import csvTo2dTable

file_path = "sheet.csv"

# Using default delimiter (`,`), you can omit the delimiter parameter
table = csvTo2dTable(open(file_path))

print(table)
```

Replace `"sheet.csv"` with the actual path to your CSV file. This code snippet demonstrates how to use `csvTo2dTable()` to open a CSV file and display its content as a two-dimensional list.



**WARNING:** 

1.If you are having trouble with CSV files like this, it may be because they have a space after the delimiter "," . So the actual delimiter is ",  ".

```
name, gender, height, address
John, male, 175cm, "123 Main Street, New York, USA"
Emily, female, 160cm, "45 Oxford Road, London, UK"
Michael, male, 180cm, "10 Rue de la Paix, Paris, France"
Sophia, female, 165cm, "25 Alexanderplatz, Berlin, Germany"
```

If you fix it or learn more about it , you can go to  [**4.Convert CSV files into other formats**](https://github.com/Alicedrop/aliceCSV#4.Convert CSV files into other formats) .

### 2.Converte two-dimensional table into CSV file：

```
TableToCsv(sheet, [optional]output_path, [optional]sheet_encoding, [optional]delimiter, [optional]line_break)
```

`sheet: a two-dimensional table`

`output_path: The location for the output result. It can be omitted, with the default value being “output.csv”.`

`sheet_encoding:  The encoding format used in the output file. It can be omitted, with the default value being “utf-8”.`

```delimiter: The delimiter used in the CSV file. It can be omitted,  with the default value being “,”.```

`line_break: The line break used in the output file. It can be omitted, with the default value being "\n".`



To save a two-dimensional list as a CSV file using the `sheetToCsv()` function, you can use the following example:

```python
from aliceCSV import tableToCsv

# Example two-dimensional list
table = [['Name', 'Age', 'City'],
         ['Alice', 25, 'New York'],
         ['Bob', 30, 'San Francisco'],
         ['Charlie', 22, 'Los Angeles']]

tableToCsv(table)
```

Then it will output the "output.csv"

![image-20240208212308629](D:\2024工程\aliceCSV\assets\image-20240208212308629.png) 



### 3.Fix the length of a CSV file or a table

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

替换`"path/to/sheet.csv"`为实际的CSV文件路径。

| name    | gender | height | address            |          |          |
| ------- | ------ | ------ | ------------------ | -------- | -------- |
| John    | male   | 175cm  | “123 Main Street   | New York | USA”     |
| Emily   | female | 160cm  | “45 Oxford Road    | London   | UK”      |
| Michael | male   | 180cm  | “10 Rue de la Paix | Paris    | France”  |
| Sophia  | female | 165cm  | “25 Alexanderplatz | Berlin   | Germany” |





### 4.Convert CSV files into other formats

Many csv files use other delimiters, not commas. 

The following CSV file named "space.csv", which has a space between every two fields, which means it's delimiter is ", " , a comma with a space following.

```
name, gender, height, address
John, male, 175cm, "123 Main Street, New York, USA"
Emily, female, 160cm, "45 Oxford Road, London, UK"
Michael, male, 180cm, "10 Rue de la Paix, Paris, France"
Sophia, female, 165cm, "25 Alexanderplatz, Berlin, Germany"
```

aliceCSV can convert them easily.

```
fixCSV(path, [optional]output_path, [optional]origin_delimiter,                  [optional]target_delimiter, [optional]origin_encoding)
```

`path: The path of the origin CSV file.`

`output_path: The location for the output result. It can be omitted, with the default value being “output.csv”.`



You can use the function `fixCSV()` to convert CSV files with different formats, as shown in the example below. 

```python
from aliceCSV import fixCSV
fixCSV("space.csv", origin_delimiter=", ", target_delimiter=",")
```

This example demonstrates the conversion of the “space.csv” file into the resulting “output.csv” as follows.

![image-20240208223737057](D:\2024工程\aliceCSV\assets\image-20240208223737057.png) 



### 5.Others 



## License

aliceCSV's code in this repo uses the MIT license, see our `LICENSE` file.
