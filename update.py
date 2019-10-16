import time,threading,json,sqlite3
from insert import Insert as ins 
from mail import Mail


class UpdateDBS:
    def __init__(self):
        self.con=sqlite3.connect('amazon.db')
        self.q=self.con.cursor()
    def browser(self,index,url):
        print('{}...on process'.format(index))
        obj=ins(url)
        js=obj.browser()
        data=json.loads(js)
        self.q.execute('SELECT price FROM links WHERE url=:url',{'url':url})
        rs=self.q.fetchone()
        self.con.commit()
        if rs[0]==data['price']:
            print('Done..{}'.format(index))
        else:
            print('Generating email.{}'.format(index))
            m=Mail()
            m.SentMail(data)
            self.q.execute('DELETE FROM links WHERE product_name=:pr',{'pr':data['product_name']})
            self.con.commit()
            i=ins(data['url'])
            i.controller()

    def update(self):
        self.q.execute('SELECT count(*) FROM links')
        r=self.q.fetchone()
        self.con.commit()
        if r[0]>0:
            self.q.execute('SELECT url FROM links')
            ln=self.q.fetchall()
            self.con.commit()
            for index,i in enumerate(ln):
               self.browser(index+1,i[0])

    def get_tables(self):
        with self.con:
            self.q.execute("SELECT * FROM links")
            r=self.q.fetchall()
            for index,i in enumerate(r):
                print('ROW{}:\nPRODUCT: {}\nPRICE: {}\nLINKS: {}\nSCREENSHORT: {}'.format(index+1,i[0],i[1],i[2],i[3]))