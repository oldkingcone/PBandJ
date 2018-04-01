# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


try:
    from datetime import datetime
    from scrapy.exceptions import DropItem
    import psycopg2
except (ImportError,ImportWarning) as e:
    import sys
    print("[***] Sorry, one of these packages did not import: %s [***]"% str(e))
    sys.exit(1)

class DuplicateCheckingPipeline(object):
    def __init__(self):
        # set up duplicate catching.
        self.id_seen = set()

    def process_item(self, item, spider):
        if item['li']:
            if item['a']:
                if item['href']:
                    if item['href'] not in self.id_seen:
                        self.id_seen.add(item['href'])
                        # since we are looking for URL's, this should blanket them into a net.
                        # Hopefully, this works fine.
                        try:
                            dt = datetime.now()
                            con = psycopg2.connect(
                            "host = 'localhost' dbname = 'crawls' user = 'YOURUNIQUEUSRNAME' password = 'YOURUNIQUEPASSWORD'")
                            cur = con.cursor()
                            cur.execute("CREATE TABLE IF NOT EXISTS crawls"
                                    "(Id INTEGER PRIMARY KEY, dates VARCHAR(255), link VARCHAR(255), summary VARCHAR(255))")
                            pgsql = "INSERT INTO crawls(dates, link) VALUES('%s','%s')"
                            cur.execute(pgsql % str(dt),str(item))
                            return item
                        except psycopg2.DatabaseError as e:
                            print("[***] Something went wrong with the DB: %s [***]" % str(e))
                    else:
                        self.id_seen.add(item['href'])
                        raise DropItem("[***] Duplicate found: %s [***]" % str(item))

