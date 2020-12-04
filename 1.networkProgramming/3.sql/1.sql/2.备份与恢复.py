"""
备份数据
    mysqldump -u root -p  employees > PATH/xxx.sql
恢复数据
    source PATH/xxx.sql


备份数据库(重新创建的时候回顺便创建并use库)
    mysqldump -u root -p  --databases employees > PATH/xxx.sql
恢复数据库
    source PATH/xxx.sql
"""