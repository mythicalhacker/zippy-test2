import MySQLdb
import datetime
import time
import specifictest


conn=MySQLdb.connect('localhost','root' ,'','test')
co=conn.cursor()

##TO BE LINKED PROPERLY
sql="SELECT * FROM confirmed WHERE book_id=%d"%(100001)      #connecting to confirmed.sql
co.execute(sql)
p3=co.fetchall()
sql="SELECT * FROM extension"     #connecting to confirmed.sql
co.execute(sql)
p4=co.fetchall()
s=p4[0]##s is extension time



def insertbook(book_id,model,date,pick_time,duration,timestamp,mobile):   
    sql='''INSERT INTO book (book_id , model , date , pick_time , duration , timestamp , mobile ) VALUES (%d , '%s', '%s' , '%s' , '%s' , '%s' , %d )'''%(book_id,model,date,pick_time,duration,timestamp,mobile)
    co.execute(sql)
r=[]
##FOR DUAL DAY RIDES
for q in p3:
    x=[]
    x.append(q[2])
    if len(x)>1:
        y=max(x)
    else:
        y = x[0]        ## y is confirmed date to extend

for q in p3:
    if q[2]==y:
        r=q             ##r is confirmed booking to extend

## For extension before ride begins
if r!=[]:
    if r[8]==0:
        if 'day' not in str(r[4]+s[4]):
            co.execute("TRUNCATE book")
            insertbook(s[0],str(s[1]),str(s[2]),str(r[4]),str(s[4]),str(s[5]),s[6])
            conn.commit()
            co.close()
            conn.close()
            vehicle1=specifictest.checker()
            if vehicle1==1:
                print 'not available'            ##TO BE CHANGED
            else:
                conn=MySQLdb.connect('localhost','root' ,'','test')
                co=conn.cursor()
                if vehicle1[3][1]==':':
                    x=len(vehicle1[3])
                    vehicle1[3]=list(vehicle1[3])
                    while x>-1:
                        if x==len(vehicle1[3]):
                            vehicle1[3].append(vehicle1[3][6])
                        
                        if x>0 and x<len(vehicle1[3]):
                            vehicle1[3][x]=vehicle1[3][x-1]
                        if x==0:
                            vehicle1[3][0]='0'
                        x=x-1
                vehicle1[3]=''.join(vehicle1[3])
                sql="UPDATE confirmed SET drop_time='%s' WHERE book_id=%d AND date='%s'"%(datetime.timedelta(hours=int(vehicle1[3][0:2]) , minutes=int(vehicle1[3][3:5]) , seconds=int(vehicle1[3][6:8]))+s[4] , vehicle1[5] , s[2])
                co.execute(sql)
                conn.commit()
                co.close()
                conn.close()
        else:
            conn=MySQLdb.connect('localhost','root' ,'','test')
            co=conn.cursor()
            co.execute("TRUNCATE book")
            print s
            insertbook(s[0],str(s[1]),str(s[2]),str(r[4]),str(datetime.timedelta(days=1) - r[4] - datetime.timedelta(minutes=1)),str(s[5]),s[6])
            conn.commit()
            co.close()
            conn.close()
            vehicle1=specifictest.checker()
            if vehicle1==1:
                print 'not available'            ##TO BE CHANGED
            else:
                conn=MySQLdb.connect('localhost','root' ,'','test')
                co=conn.cursor()
                sql="UPDATE confirmed SET drop_time='23:59:00' WHERE book_id=%d"%(vehicle1[5])
                co.execute(sql)
                conn.commit()
                co.close()
                conn.close()
            conn=MySQLdb.connect('localhost','root' ,'','test')
            co=conn.cursor()
            
            co.execute("TRUNCATE book")
            insertbook(s[0],str(s[1]),str(s[2]+datetime.timedelta(days=1)),datetime.timedelta(hours=0),str(r[4]+s[4] - datetime.timedelta(days=1)),str(s[5]),s[6])
            print s
            conn.commit()
            co.close()
            conn.close()
            vehicle1=specifictest.checker()
            if vehicle1==1:
                print 'not available'            ##TO BE CHANGED
            else:
                conn=MySQLdb.connect('localhost','root' ,'','test')
                co=conn.cursor()
                sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(vehicle1[0] , (vehicle1[1]) , str(s[2]+datetime.timedelta(days=1)) , '00:00:00' , str(r[4]+s[4] - datetime.timedelta(days=1)) , vehicle1[5] , vehicle1[6] , (vehicle1[7]) , vehicle1[8])
                co.execute(sql)
                conn.commit()
                co.close()
                conn.close()
            
            

##FOR REAL TIME EXTENSION (FORCE EXTENSION)
    elif r[8]==1:
        conn=MySQLdb.connect('localhost','root' ,'','test')
        co=conn.cursor()
        
        print str(r[4]+s[4])
        ##MULTI DAY EXTENSIONS
        if 'day' in str(r[4]+s[4]):
            print 'yes3'
            sql="UPDATE confirmed SET drop_time='%s' WHERE book_id=%d"%('00:00:00', r[5])
            co.execute(sql)
            sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(r[0],str(r[1]),str(r[2]+datetime.timedelta(days=1)),'00:00:00',str(s[4]-(datetime.timedelta(days=1)-r[4])),r[5],r[6],str(r[7]),r[8])
            co.execute(sql)
            sql="SELECT * FROM confirmed where vehicle_id=%d AND date='%s' ORDER BY pick_time ASC"%(r[0],datetime.timedelta(days=1)+r[2])
            co.execute(sql) 
            t=co.fetchall()
        else:
            sql="UPDATE confirmed SET drop_time='%s' WHERE book_id=%d"%(str(r[4]+s[4]), r[5])
            co.execute(sql)
            placeholder=r[4]+s[4]
            sql="SELECT * FROM confirmed where vehicle_id=%d AND date='%s' ORDER BY pick_time ASC"%(r[0],r[2])
            co.execute(sql) 
            t=co.fetchall()
            
        
        for x in t:    
            if x[3]>r[3]:
                if x[5]!=r[5]:
                    if placeholder>x[3]:
                        if 'day' in str(placeholder-x[3]+x[4]):
                            sql="UPDATE confirmed set drop_time='%s' WHERE book_id=%d"%('23:59:00' , x[5])
                            co.execute(sql)
                            sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(x[0],str(x[1]),str(x[2]+datetime.timedelta(days=1)),'00:00:00',str((x[4]-x[3])-(datetime.timedelta(days=1)-placeholder)),x[5],x[6],str(x[7]),x[8])
                            co.execute(sql)
                            sql="SELECT * FROM confirmed where vehicle_id=%d AND date='%s' ORDER BY pick_time ASC"%(r[0],r[2]+datetime.timedetla(days=1))
                            co.execute(sql)
                            z=co.fetchall()
                            x.append(z)
                        else:    
                            sql="UPDATE confirmed set drop_time='%s' WHERE book_id=%d"%(str((placeholder-x[3])+x[4]) , x[5])
                            co.execute(sql)
                            sql="UPDATE confirmed set pick_time='%s',state=%d WHERE book_id=%d"%(str(placeholder) , x[5] , 2)
                            co.execute(sql)
                            sql="SELECT * FROM confirmed where book_id=%d"%(x[5])
                            co.execute(sql)
                            y=co.fetchall()
                            y=y[0]
                            placeholder=y[4]
                            print placeholder
                        
                        
        conn.commit()
        co.close()
        conn.close()
                        
                




         

