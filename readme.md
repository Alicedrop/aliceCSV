# aliceCSV -- A concise and easy-to-use csv module   
**aliceCSV -- 一个简洁易用的csv模块**
这是英文版介绍，中文版介绍请看[中文文档](https://github.com/Alicedrop/aliceCSV/blob/main/readme_zh-CN.md)

这个模块可以把csv文档作为二维列表进行操作，也可以用作开发的参考

例如下面的例子

This moudle can manipulate CSV documents as two-dimensional lists, as shown in the following example

## 使用方法

### 读取csv文件为二维列表：
```
csvTo2dSheet(file, mode)
```
file：一个使用open()打开的csv文件

mode: 选填，默认为standard，自动对csv文件中不符合规范的部分进行纠正，origin为保留原格式不进行自动修复




### 把二维表存储为csv文件：
```
sheetToCsv(sheet,output_path)
```
把
