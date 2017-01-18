import  connetmysql

class sql():
    def create_user(self,handle):
        handle.execute("DROP TABLE IF EXISTS `user`")
        handle.execute("create table user("
                       "id int not null auto_increment,"
                        "mobile VARCHAR (11),"
                       "name VARCHAR (20),"
                       "password VARCHAR (20),"
                       "primary key(id,mobile),"
                        "UNIQUE (mobile)"
                       ")"
                       "")
        handle.close()

    def create_need(self,handle):
        handle.execute("DROP TABLE IF EXISTS `need`")
        handle.execute("create table need("
                       "id int not null auto_increment,"
                       "need_id int (5),"
                       "need_name VARCHAR (100),"
                       "need_status VARCHAR (20),"
                       "finish_test VARCHAR (10),"
                       "need_tester VARCHAR (20),"
                       "need_day VARCHAR (15),"
                       "need_url VARCHAR (150),"
                       "primary key(id)"
                       ")"
                       "")

    def create_number(self,handle):
        handle.execute("DROP TABLE IF EXISTS `worknumber`")
        handle.execute("create table worknumber ("
                       "id int not null auto_increment,"
                       "casenum int (5) DEFAULT 0,"
                       "bugnum int (5) DEFAULT 0,"
                       "gubnum int (5) DEFAULT 0,"
                       "mobile VARCHAR (11),"
                       "day VARCHAR (8),"
                       "score int (2) DEFAULT 0,"
                       "score_reason VARCHAR(50),"
                       "primary key(id)"
                       ")"
                       "")
        handle.close()

    def create_plan(self,handle):
        handle.execute("DROP TABLE IF EXISTS `plan`")
        handle.execute("create table plan("
                       "id int not null auto_increment,"
                       "content VARCHAR (500),"
                       "mobile VARCHAR (11),"
                       "primary key(id)"
                       ")"
                       "")
    def create_info(self,handle):
        handle.execute("DROP TABLE IF EXISTS `info`")
        handle.execute("create table info("
                       "id int not null auto_increment,"
                       "mobile VARCHAR (11),"
                       "worktime VARCHAR (15),"
                       "avgtime VARCHAR (15,"
                       "txtime VARCHAR (15),"
                       "csxl VARCHAR (15,"
                       "primary key(id)"
                       ")"
                       "")
if __name__=="__main__":
    handle,conn=connetmysql.Mysql.connet()
    connect=sql()

    # connect.create_need(handle)

    # connect.create_plan(handle)
    # connect.create_number(handle)
    connect.create_info(handle)
    # connect.create_user(handle)

    connetmysql.Mysql.close(handle,conn)