# 数据文档模板

本项目的数据文档经历过两个版本，最初的版本是使用SQL建表语句表示的，在后期尝试过改为使用typescript表示，但这种表示方式不是很适合SQL数据库，更适合noSQL，故下面不赘述。

# XXXX数据文档

- [XXXX数据文档](#XXXX数据文档)
  - [一、概述](#一概述)
  - [二、具体字段](#二具体字段)
  - [三、具体模型](#三具体模型)
    - [XXXX](#XXXX)

## 一、概述

本文档是后端开发相关的数据文档，规定了表名，数据字段等，供数据库维护，后端开发以及参考使用。

## 二、具体字段

### XXXX

简介，表权限，（如果来自ETL）来源，外键说明

数据字段如下：

```pgsql
TYPE_ VARCHAR (36 char) 类型
LITISTATION VARCHAR (36 char) LITISTATION
XM VARCHAR (270 char) 姓名
SEX VARCHAR (36 char) SEX
METHOD_ VARCHAR (222 char) METHOD
SFZHM VARCHAR (60 char) 身份证号码
OTHERNO VARCHAR (90 char) OTHERNO
ORGANIZATIONNO VARCHAR (108 char) ORGANIZATIONNO
ADDRESS VARCHAR (294 char) ADDRESS
TELEPHONE VARCHAR (112 char) TELEPHONE
ID NUMERIC (18,0) ID
```
