# aliceCSV -- A concise and easy-to-use csv module   

**aliceCSV -- 一个简洁易用的csv模块**

==这是英文介绍，中文介绍请看[中文文档](https://github.com/Alicedrop/aliceCSV/blob/main/readme_zh-CN.md)==

This module can operate CSV file **as two-dimensional table** and be able to **convert them** into other forms easily.

<img src="iVBORw0KGgoAAAANSUhEUgAAAQ8AAABhCAIAAABHxLP3AAARuklEQVR4nO2dT4jjyL3Hf34Me13Y7GFDM7NNRvbB+DCPMMMiQ+8SAhm5IbiTRgT6BT94iXV4vJEHxk0IziXPhzBuWKvh8SKHJfGhL1on7YutXQbysk1shl5CmkXxwVIv3TOY7GH/XfYy7I7fQdZf60/JlmS3pj6HYVp/SlWq+ql+Va5v/VJffvklhMr5+fmrr74abprrwKeffnrz5s1V5yJ8vv7662vXrq06F+ETRbn+JdzkAOD58+ehp7kO4HJdLaIoVzjW8uzZM/3/+O1fLabT6aqzEAlRlCuErurZs2dfffXVSy+9pP4ZX6s6f+et3uO727/7RSz+USzlmhw/YI8u9D+39jv37kT8yNjqy1y2zT3uYGcj0setY9+imor5yDfffLNkmogM5ceZb11/Tz6L53GxlWtzj+t0Op1OZ3/r5OHhadSPi6VvOT3c3WUH+VnBOp378HbUJYuiXEtZy7ypQGzfqs/FP4zf+Hfqdmb8t2Ecz1uBJ7ZxfROeTCYRPyWGcp0ePjzZ2u+YepONnYOoO8316lscTQXialVPzz8cZ75LvnLre996fHIewwPjt5bJ6eBii47YX4mhb5kcCyebez+O2qO0s0bjFjdTgZha1T8H46d337gFAPnM9d8+FvduUtcjfmRs1nJxxO4eAQDA1n4n+jYWebkmTy/gBh210c+xLn2Lh6lAPK3q87M/f/bG1k0AgOs3b2c++3DweeTPjM1a9HELd13Y3Y184ILnxNAJ3Ld4mwrE0qqGp38aA/zy8LFx6PyfP3nl25E+dAXjlh1660iYTACi/DBHXq6N65swiLoU80RRrmDW4msqEMfc0dnJGCwTx+fvvPX47Ontb0fqjMU2JxYzkfctG3fym0eD08lO5EMwCyueE0MxFYjhW3X+t/dg5obNuPndu5/96SjisX78fcvkWDjZzN+JuI1FX66Nnft7cMSancrTw8hdzFX2LYimAtG//aH8GDL/SVqO3drKwC/ls1/cvBXdc1cwyoet/c7VnxMDgI2dg86d4wfs7u7sQAw/u0ZRrlToqyo/+OCDW7cibLWr4uzs7M0331x1LsLnk08+ee2111adi/CJolx4VSUqSS0XnhNDJ+Qlzf/63zQAwF/DTXVt+Ov//v1XwqozETJJ/QpEMm558uTJdDp9/vy5778ol4Wev3Xj0aNHq85C+IxGo1VnIRJCL9e1l19+Ocz0hjwAfHzwfphprgffefADANjVB6pJ4fLy8vXXX191LsIninKFP27BYJIKthYMBhVsLRgMKthaMBhUEK3l7DeH7ywguhKZVCrPKfNHGTF4YmuIc/muNorIMfmUSj7PiGrpklNny+BvLU8//PVbh//z3qIPIEEoJaw96YjdVrmcqzQS1IxEJl0QsjVZ/cWgXYNCmhEBgOKnPKVdkrQPBDI+1jJ87+c//eyHf/m3H2UWfUCuVssl1F7Ebqtc5IvlVjcp5iIyBakpD1iKUP8mKF5uSl3RXHvKWFpJ3tYBH2sh7/7uL3eXXPRF8R72oohGt8/o1yhcPs8pyswlUE/oV+bNLoHlfjFWmxS7rXKRAsrBXKylErm88TVeYYZ9Ebutco0lLMcIdsBThOaJiUwqXRkOK+lUKsWIc/6ZwuUT7a/FMsqn+FpOcPJXFLFRgFm3L9eyQtr0roVGI1MdTKdTmZYqDY5rjNW/+jmpoF0mMqV61ri/XoqvrhSu3ioXKYB5cxGZtF6qabs4KlSGxqmVZdgfZSyR2bTnJRQ/lZsk2ZSn0ylPAVUsS6aiiw0hV6SizuYKiWlOjOJrUJhvGQTFT/lZt09Q2zQpjbWv7RCyVfUMwdbKLQGq6kePoKr6ZWJXotusfj9by8XmFCk9YVietQybuYjdVrnPm5yZftk4tbIMRwNVpQ1zEbutZBtLfDPIFN93shdFZPKaZ5KumKbdSHrb7BLkMoT9VlDGkuoTaBRaYJhbpCg9AZpVrWVYzGX+C53OkivPcFQQ27RU5xQAULi6ZLySZBLj7y1UtSnVrfYiMukC0O2Z0yI3Sbd73VB9AhMDdt6qwkfpCUNzuy+0oFVHmslYUYaRIDK5odALaLwEW8sJPQWUngDWD1wCifPXSYJt0xZ7UcYS2ayyxOwdy6NgP+kQmdxwJIeZQ0SUnjAs9y2Nvl/WGtp8rvRyrSzDiFDF8py5KJzfZARVzAk9rifk7BMEySPe3/JVe6lLRh8yHMlqVSgiU28FTI4qllsFvS4VkYlnRkZsVMDuc5gami1XHNMF0rhqFRlGhuL7uUo6z5lymK7kipTNCmwmTxVzQiXh43sVNGt5hWrd+4/AbpITBNumYTjU/2hCXXVoSt1iLbAnRvFyX0sgVepm23x0NfbxwfuqEkHstsh5n4OqNkEzF17Wi5VvZKrV7EoyvBAUL/fpkSmHfdmWRWKbJluFlHkRQzoLJJ3wIQsAAKQuLy9DTO6tw59D4vQtqrJFJ1jpFJErFUa16bqZhc7SOhCFy5dGtcG6FRDrW64G5nm+VLo+ou2f58SgcPlUKi3Qa9dFRkTqo48+ClFp/GDIr7pEIfPxwfu2vuX//ivo+AqTEK7duHEjzPQSZy3zJEyXi5XG6IS858vffyU8evQoeeJ1DAZCt5ZEog7rk/oNxqCDR/kYDCrYWjAYVPysZXL8YFfjwfGiMRAdFbm6OAKrWEPE0M+Y9ELqVK8Jl/cdgzJcZOaeoJj1PygEviEsvK1lcvz2U3oWhpbbgyN2sTACPopck4oVsxwik67PpDVyLSukTY3KsrDN/X1HrQynqk2waJ0UrnRllph5W4s59OzGDr0FJ48XMJfkKXLXFbHbKtdm0hqCYmtlbUUX+oLVyJXh6lpB/QFio5KrXZWPZYBxy2TyBDavBw8n4qHInV1g6ukVzsGRWGd17lrh0Uv7qSLNiXjZi0NdWLa1sHpajjteEKwupbWLYozqt1S16nqJTN7RoY/PLUO3ltM/Hl0sEKnKQ5E7j8iktQ1H5BpU1Cpba3XuOiN2pbKxMHjUM75DPi/QVRnuXBdUMaev8xe7Egn6EmWxKzlqXii+BnVOUcSG2QlTuHza2G9G1vebUREa3WLbrgdSuHw9245NI4RmLaeHu7sPn+xxB4EjVXkocudRd1HQHAlefTOJU+fGg9qOZj2NMpaG0qjYVpshLRX8vsYuynCXukhnteXXyliia7r4WOxKTppXAACqSgulUh1MTpjYqOT6lv1m+mVDY2coz81FLEF8pgIo1qJZSie4qXgqch0udtpFIYHq3OixtyOCHUwH+gYIbFsXF7jjpAx3qwtim1b7E6Un5DLU9sxclLHkLnoh2FpuaD7tUPtUUR942ZXnMOox6dhnB3ys5fRwcUuBZRS5ZtZZnbuG+H9yiUwOIR0HZbhbXRCZnNQVQekJuSIFhGous7+iYdgaFfvm2YJY8LSWybFwsrl3f+FAoZ6K3Hkchbjrrs5dM5xNxSbSRNxAb04Z7l4XVDEnjUXNPIhtWhqL8giQZxacExe7LbfJCbJZpSi2TQuxjmJ9PbGLI3bXTIBfXHwUufNQxXKrPpO5Ktrkyrqrc9cJhSsJdHu+V6GKOdOL5UoVRBfGrgx3rwuqmBPqel9CZHJCve48wneFqjalgkXlXJjfDNApf/G1B89VlRs7B52dhZMWuy2Slh0UufVST2Ed3wLF97v5QroCAECW+2q9U7zcZ0rpVEE92nxRpEfBUXrCcDhMpyrGIbIpD1gCKF4ea++QLDfR5WkE26aFtJ6ge12kszCEojFCzRWkbDuYw0ywAxmM1MlmX2b98kmwbTqfZsR4ft8OPwJ4UlfsJ3UNMi4XOnhVJQaDSuqLL76YhspoNLp9+/aqy4XBhM81dWo3xBRHoxHu2a8QSS1XFGBPDINBBVsLBoMKthYMBhVsLRgMKr7WYpIaBxdOioyxAs8sfPW+Bf9WvwSOAiFwUyDP3e0Y2HApzG0glYouBnQcDcd3VeXbcF9VGu9vnTxcQJmvrROzC18xEaBw+ZK+ML8GFV0fonClgkmB7LK4SuFKBaCdAxsug2WtYFRLYuPQq/tYy517+urjO29sLfMgi/AVEwlKTwC6qstPqk095GCjkuubFMguEiF5NCwXWV290raHM37hQR63TI6FkwWkk664aEpnILkNGBsEO3D8ctulIwgq1llymibGNfQ0I4IRaxq5quaUw4HTn3c4dU/M7HOatMrOW+F4NcJ5fK3l9FAdtLBP6UVVLjArgyHB9taUSnVmrLsT4fkDLximvVTk0dCqYdQjYVpRVwEznL3ZeIWe7jJdta5kWqoE2f3CpBwOnL6jIn2G2ChItHaq3hBdr/duhM58icg/fv+z73//Z7//h++F7777ru6jGtF8AchyXzYOz8leNJ2R8T/Xi1fDxcXFqrOAxix8J1luur5vuUnqB+zlkvvNMkkCkOVm36b80m+e1ZDcJE0JW//SMbcBmMnJ5CY5rytDT9+xSWgHHU56Xm854popFWRPbGPn/t7mxeA06DBfz1G7OC6pcggfTaktfjFVLGNlcRAIdqC+bygtIgUiKJYfDKbTdhGMDUPcQ08bFemuyDS3Ss1VtCqHA6XvqEjXoapNqZDKM0YX6aZg92yEjsT3ewtBWTeSwkSL6X2ns6T1g4MiazTNBiwdetqHcNMn2MF0OqgWoVvKh6wc9LaW00NjznjBHZIc8NOUWmtW7LbcNg7BWHH7ycH+wl1eqdvtS4ae9iVo+kjic4Ji+YFq7qgKdg9h8wxva7lzj36qCY0fwv6Sw3yuVFFDqvtoSoeVknZOEZm6eVMsjBf2aMolLYQ9VW1K2glFZLQd3rxvF5mCft1SoacRCJa+oyJ9hsjok16K1vydFezBhc3oo3xk3Eb5tmGj3CxrHS5JGifkJkmWm6ZzZeehZvxcjVG+3De9OvOQ1Thhe6WWcpluN99vVBZZ7vfNo3DzsNh5PsbpqO3GBdLvz7UQ/azjG5i/3vpcSyN0BSuNUUmqDiSp5YoCvKoSg0Hlml/nExgAuLy8XHW5IgGX6wUHK41RSarHktRyRQH2xDAYVLC1YDCoYGvBYFDB1oLBoIJqLZPjBwsGNVZEQ0SQ10UES4alxfGQ3XBTFCMpjaMJFuwcKTnU9GNqA4jWcvrHo4uF0heZdMEQEbSRRARBwPGQLbjFNPaIdRx9nrwjWl8lkKzl9PDhyebmZvDURaYgNWVLdDQZy1ejwy2msWus45jylJSI1gjWMjkWTrb27+eDJ67GkbSuUzPJV8FRROoqOnWMamuJh/zChz5262mX7YHdQg07aXptuEW09lIRW1qAaPYOfavY8QKUfCKBsEPS20c39u/dWSBtb9WOrjW1iEi9RKeOUW11cOhjO9aYxv7HXXBV5Dppeufu9Ypo7aYi1lvAtF0cFQxxmG8VO1+AkE9EfHdIYhe1FV+GuaLmHGzT5Mw3ICh+qocTpbZpk4zJIaqtCRz62IolpjHCcVc8Qw3PZDIExQ+ckvSOaN0ChwYgdlvlPm95mp4Tvyp2v8Ann6h4Wsvp4cMne1w0tuIqUnUXnXoFZsOhj824BWpdIGa2hyJ3XtNrv9c7ojWailjfccO3it0u8M0nMh7WMjkWToywk+zRhfoH+o6VRCbnHmPShSVEpzj0sUqIpuKDj6Y3nIjWZnyr2CXkcljaYw9r2dg56Bhwe5uwucd1OgG6GqeQrArnNdJaWNSKQx+rhG4q/opck6bX+shgEa3dHqe3Ad8q9rnALZ8BiPa3fIrv5yppi5wzXckV3UcfsLCoFYc+BveYxm7HUXBV5Dppek0EjmitX2JRSzNd8I+o7HmBTz6DEGCHpINFZPkUL/fpUX3WHZe62b5nPF2CbTdhdnWpW6wF8MQoXu6D6UEvYOhju+uTmk23ux13wnIdI4IaathUhXWtCim+BoJ6NF2Hps0YxW7LYaBJVZvgZy68rDeBfCNTrWbNp7yr2PEC73wGAiuNUUmqDmSty6WIXKkwqq3Leg28qhKzXpjnRFPp+oj2dEbiBcc0xmBQwUpjVNbaY1kCXC50sCeGwaCCrQWDQQVbCwaDyv8DpZjbukaaoSwAAAAASUVORK5CYII=" />

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

![image](https://github.com/Alicedrop/aliceCSV/assets/128953967/73dad0cb-cc60-4636-808f-0142e2765384)




### 5.Others 



## License

aliceCSV's code in this repo uses the MIT license, see our `LICENSE` file.
