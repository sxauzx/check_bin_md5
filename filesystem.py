#!/usr/bin/python
import hashlib
import os
import sqlite3

urls=['/usr/bin/','/usr/local/bin/','/usr/sbin/','/usr/local/sbin/','/bin/','/sbin/']

def file(pathdir):
    all_pro = os.listdir(pathdir)
    childgroup = []
    for pro in all_pro:
        child = os.path.join('%s%s' % (pathdir, pro))
        childgroup.append(child)
    return childgroup

def check(childgroup):
    check_path = os.getcwd()
    for progress in childgroup:
        check=hashlib.md5()
        check.update(progress)
        result = check.hexdigest()
#        print progress, result
        conn = sqlite3.connect('%s/bin.md5' % (check_path))
        conn.execute("create table if not exists checksum(id integer primary key autoincrement, url text,md5 text);")
        conn.execute("insert into checksum(url, md5) values ('%s', '%s')" % (progress, result))
        conn.commit()


if __name__=='__main__':
    for url in urls:
        sum=file(url)
        check(sum)
