import pymysql
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)
cursor = conexao.cursor()
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)
    
    
    #output
#('information_schema',)
#('mysql',)
#('performance_schema',)
#('phpmyadmin',)
#('test',)
