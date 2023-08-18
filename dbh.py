import sqlite_utils

def insert_data_from_file(db_path, table_name, file_path):
	# 连接到数据库
	db = sqlite_utils.Database(db_path)
	
	# 创建表格
	table = db[table_name]

	# 读取文件内容并插入数据
	with open(file_path, 'r') as file:
		for line in file:
			# 解析每行数据为Python列表
			row_data = eval(line.strip())

			# 转换列表为字典
			column_names = ['0','1','2','3','4','5','6','7','8','f',]
			row_data_dict = dict(zip(column_names, row_data))

			# 插入数据到表格
			table.insert(row_data_dict)

import sqlite3 as sqlite

def get_data_num(filename,tablename,condition):
	# read database file
	conn = sqlite.connect(filename)
	# create cursor
	c = conn.cursor()
	# create a query
	# SELECT COUNT(*) FROM pgs WHERE `1` = 'X' AND `5` = 'O' AND `f` = 'T';
	q = 'SELECT COUNT(*) FROM '+tablename+' WHERE '
	for key,value in condition.items():
		q += f"`{key}` = '{value}' AND "
	q = q[:-5]
	q += ';'
	#print(q)
	# execute the query
	c.execute(q)
	# get the result
	result = c.fetchone()
	# close the connection
	conn.close()
	# return the result
	return result[0]