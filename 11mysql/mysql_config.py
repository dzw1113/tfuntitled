from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

#https://www.cnblogs.com/kongqi816-boke/p/5752510.html
# create_engine("数据库类型+数据库驱动://数据库用户名:数据库密码@IP地址:端口/数据库"，其他参数)

engine = create_engine("mysql+pymysql://root:mysql123@120.55****:3306/bms", echo=True)

metadata = MetaData(engine)

#创建user表
# user = Table('user', metadata,
#              Column('id', Integer, primary_key=True),
#              Column('name', String(20)),
#              Column('fullname', String(40)),
#              )
# metadata.create_all()

# 执行SQL
cur = engine.execute('select * from km_bus_dict')
# 获取第一行数据
one = cur.fetchone()
print(one)
# 获取第n行数据
cur.fetchmany(3)
# 获取所有数据
cur.fetchall()