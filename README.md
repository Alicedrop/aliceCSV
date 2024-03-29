# aliceCSV -- A concise and easy-to-use csv module   

**aliceCSV -- 一个简洁易用的csv模块**

==这是英文介绍，中文介绍请看[中文文档](https://github.com/Alicedrop/aliceCSV/blob/main/READEME_zh-CN.md)==

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

And don't worry about this kind of compatibility affecting normal reading. For example, even if you want to express the wrong sheet Excel reads out, it shouldn't be done in that erroneous manner. Such writing is merely guesswork for the interpreter to decipher. The interpretation may vary due to text and interpretation program differences, making it uncertain what it's interpreted as. aliceCSV simply outputs results based on commonly made errors, opting for those that likely reflect the author's true intent.

## Install

You can use pip to install it.
```bash
pip install aliceCSV
```
or install from this repo.

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

If you fix it or learn more about it , you can go to the forth part [**4.Convert CSV files into other formats**](https://github.com/Alicedrop/aliceCSV/blob/main/README.md#4convert-csv-files-into-other-formats) .

### 2.Converte two-dimensional table into CSV file：

```
TableToCsv(sheet, [optional]output_path, [optional]sheet_encoding, [optional]delimiter, [optional]line_break)
```

`sheet: a two-dimensional table`

`output_path: The location for the output result. It can be omitted, with the default value being “output.csv”.`

`sheet_encoding:  The encoding format used in the output file. It can be omitted, with the default value being “utf-8”.`

```delimiter: The delimiter used in the CSV file. It can be omitted,  with the default value being “,”.```

`line_break: The line break used in the output file. It can be omitted, with the default value being "\n".`



To save a two-dimensional list as a CSV file using the `tableToCsv()` function, you can use the following example:

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

![image](https://github.com/Alicedrop/aliceCSV/assets/128953967/fd302b28-7619-4e49-a0e8-6b26989346fa)




### 3.Fix the length of a CSV file or a table

The  function `fixLineLength()` can be used to fix the length of lines in CSV files according to the RFC 4180 standard. 

It checks the number of fields in each row. If the number of fields in a row is less than the maximum number of fields, an empty field will be added at the end of the row to ensure that the number of fields in each row is the same.

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

Replace 'sheet.csv' with the actual CSV file path.






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
fixCSV(path, [optional]output_path, [optional]origin_delimiter,[optional]target_delimiter, [optional]origin_encoding)
```

`path: The path of the origin CSV file.`

`output_path: The location for the output result. It can be omitted, with the default value being “output.csv”.`

`origin_delimiter: The delimiter of the origin CSV file.It can be omitted, with the default value being “,”.`

`target_delimiter: The delimiter used in the output file.It can be omitted, with the default value being “,”.`

`origin_encoding: The encoding of the the origin file.It can be omitted, with the default value being “utf-8”.`

`target_encoding: The encoding used in the output file.It can be omitted, with the default value being “utf-8”.`

`target_line_break: The line break of the output file.It can be omitted, with the default value being “\n”.`


You can use the function `fixCSV()` to convert CSV files with different formats, as shown in the example below. 

```python
from aliceCSV import fixCSV
fixCSV("space.csv", origin_delimiter=", ", target_delimiter=",")
```

This example demonstrates the conversion of the “space.csv” file into the resulting “output.csv” as follows.

![image](https://github.com/Alicedrop/aliceCSV/assets/128953967/73dad0cb-cc60-4636-808f-0142e2765384)




### 5.Others 



## License

aliceCSV's code in this repo uses the MIT license, see our `LICENSE` file.
