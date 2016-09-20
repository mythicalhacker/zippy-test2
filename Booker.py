import MySQLdb
import datetime
import time
import zipytest


conn=MySQLdb.connect('localhost','root' ,'','test')
co=conn.cursor()


############# TO BE REMOVED
def insertbook(book_id,model,date,pick_time,duration,timestamp,mobile):
    co.execute("TRUNCATE book")
    sql='''INSERT INTO book (book_id , model , date , pick_time , duration , timestamp , mobile ) VALUES (%d , '%s', '%s' , '%s' , '%s' , '%s' , %d )'''%(book_id,model,date,pick_time,duration,timestamp,mobile)
    co.execute(sql)

    
insertbook(100001 , 'Pulsar 150', '2016-08-17' , '23:00:00' , '05:00:00' , 'yes' , 9176047028)
#############
co.execute("SELECT * FROM book")
dual = co.fetchall()
dual=dual[0]
print dual

        

conn.commit()
co.close()
conn.close()

if 'day' in str(dual[3]+dual[4]):
    conn=MySQLdb.connect('localhost','root' ,'','test')
    co=conn.cursor()
    number=int(str(dual[3]+dual[4])[0])
    sql="UPDATE book SET duration='%s'"%(str(datetime.timedelta(days=1) - dual[3] - datetime.timedelta(minutes=1)))
    co.execute(sql)
    conn.commit()
    co.close()
    conn.close()
    vehicle1=zipytest.checker()
    if vehicle1==1:
        print 'not availabe0'            ##TO BE CHANGED
    else:
        conn=MySQLdb.connect('localhost','root' ,'','test')
        co=conn.cursor()
        sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(vehicle1[0] , (vehicle1[1]) , (vehicle1[2]) , (vehicle1[3]) , (vehicle1[4]) , vehicle1[5] , vehicle1[6] , (vehicle1[7]) , vehicle1[8])
        co.execute(sql)
        conn.commit()
        co.close()
        conn.close()
        
        for n in range(number):
            print n
            if n!=(number-1):
                conn=MySQLdb.connect('localhost','root' ,'','test')
                co=conn.cursor()
                
                sql="UPDATE book SET date='%s',pick_time='%s',duration='%s' WHERE book_id=%d"%(str(dual[2]+datetime.timedelta(days=1+n)),'00:00:00','23:59:00' ,dual[0])
                co.execute(sql)
                conn.commit()
                co.close()
                conn.close()
                vehicle1=zipytest.checker()
                if vehicle1==1:
                    print 'not availabe1'            ##TO BE CHANGED
                else:
                    conn=MySQLdb.connect('localhost','root' ,'','test')
                    co=conn.cursor()
                    sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(vehicle1[0] , (vehicle1[1]) , str(vehicle1[2]) , '00:00:00' , '23:59:00' , vehicle1[5] , vehicle1[6] , (vehicle1[7]) , vehicle1[8])
                    co.execute(sql)
                    conn.commit()
                    co.close()
                    conn.close()
            if n==(number-1):
                conn=MySQLdb.connect('localhost','root' ,'','test')
                co=conn.cursor()
                co.execute("SELECT * FROM book")
                test=co.fetchall()
                print test
    
                sql="UPDATE book SET date='%s',pick_time='%s',duration='%s' WHERE book_id=%d"%(str(dual[2]+datetime.timedelta(days=1+n)),'00:00:00' , str(dual[4]+dual[3]-datetime.timedelta(days=number)) , dual[0])
                co.execute(sql)
                co.execute("SELECT * FROM book")
                test=co.fetchall()
                print test
                conn.commit()
                co.close()
                conn.close()
                vehicle1=zipytest.checker()
                if vehicle1==1:
                    print 'not availabe2'            ##TO BE CHANGED
                else:
                    conn=MySQLdb.connect('localhost','root' ,'','test')
                    co=conn.cursor()
                    sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(vehicle1[0] , (vehicle1[1]) , str(vehicle1[2]), '00:00:00' , str(dual[4]+dual[3]-datetime.timedelta(days=1+n)) , vehicle1[5] , vehicle1[6] , (vehicle1[7]) , vehicle1[8])
                    co.execute(sql)
                    conn.commit()
                    co.close()
                    conn.close()
            
else:
    vehicle1=zipytest.checker()
    if vehicle1==1:
        print 'not available'            ##TO BE CHANGED
    else:
        conn=MySQLdb.connect('localhost','root' ,'','test')
        co=conn.cursor()
        sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(vehicle1[0] , (vehicle1[1]) , (vehicle1[2]) , (vehicle1[3]) , (vehicle1[4]) , vehicle1[5] , vehicle1[6] , (vehicle1[7]) , vehicle1[8])
        co.execute(sql)
        conn.commit()
        co.close()
        conn.close()

##FINISHED
##    
##
##
##
##
##         
##
##
