import MySQLdb
import datetime
import time


conn=MySQLdb.connect('localhost','root' ,'','test')
co=conn.cursor()

def insertextension(book_id,model,date,pick_time,duration,timestamp,mobile):   
    sql='''INSERT INTO extension (book_id , model , date , pick_time , duration , timestamp , mobile ) VALUES (%d , '%s', '%s' , '%s' , '%s' , '%s' , %d )'''%(book_id,model,date,pick_time,duration,timestamp,mobile)
    co.execute(sql)

insertextension(100001,'Pulsar 150','2016-08-18','04:00:00','03:00:00','yes',9176047028)
    
conn.commit()
co.close()
conn.close()
