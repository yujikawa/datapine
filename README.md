# datapipe
# 0. Create project folder.
```
# mkdir ~/sample_pj
```

And you have to put SQL file and Data.

```
~/sample_pj
|__export
|__sqls: Transform data with SQL
|__source: csv or excel
```

# 1. Add DataSource(csv or excel) to source dir.
Create Data {table name}.csv

sample_pj/source/sample.csv
```
a,b,c
1,2,3
4,5,6
```

# 2. Add SQL to sqls dir.
Create SQL {SortNo}.{sql name}.sql
sample_pj/sqls/0.delete.sql
sample_pj/sqls/1.create.sql

0.delete.sql
```
drop table if exists a_sum;
```

1.create.sql
```
create table if not exists a_sum as 
select sum(a) as "合計" from sample;
```

# 3. Add SQL to export dir.
Create SQL {sql name}.sql
sample_pj/export/export.sql

export.sql
```
select * from a_test
```

# 4. Run command.
```
$ datapine etl --path ~/sample_pj
```
