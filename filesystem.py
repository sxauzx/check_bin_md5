#!/usr/bin/python
import hashlib
import os
import os.path
import sqlite3

dirpath=["/root/","/bin/","/boot/","/dev/","/etc/","/home/","/lib/","/lib64/","/srv/","/sys/","/usr/"]
urls=[]
for direct in dirpath:
    for parent,dirnames,filenames in os.walk(direct):
        for file_name in filenames:
            file_path=os.path.join(parent,file_name)
#            print file_path
            urls.append(file_path)

#def file(pathdir):
#    all_pro = os.listdir(pathdir)
#    childgroup = []
#    for pro in all_pro:
#        child = os.path.join('%s%s' % (pathdir, pro))
#        childgroup.append(child)
#    return childgroup

def check(url):
    check_path = os.getcwd()
    check=hashlib.md5()
    check.update(url)
    result = check.hexdigest()
#        print progress, result
    conn = sqlite3.connect('%s/bin.md5' % (check_path))
    conn.execute("create table if not exists checksum(id integer primary key autoincrement, url text,md5 text);")
    conn.execute("insert into checksum(url, md5) values ('%s', '%s')" % (url, result))
    conn.commit()


if __name__=='__main__':
    for url in urls:
        check(url)
