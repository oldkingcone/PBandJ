try:
    import socket
    import os
    from selenium import webdriver
    from time import sleep
    import sqlite3
except (ImportError, ImportWarning) as e:
    print('[!] Sorry... One of the packages didnt import: \n%s [!]' % str(e))

os.system('clear')
print('''
____________                   _     ___ 
| ___ \ ___ \                 | |   |_  |
| |_/ / |_/ /   __ _ _ __   __| |     | |
|  __/| ___ \  / _` | '_ \ / _` |     | |
| |   | |_/ / | (_| | | | | (_| | /\__/ /
\_|   \____/   \__,_|_| |_|\__,_| \____/
by [**] @old_king_cone [**]\n''')
print('[***] Please crawl responsibily, maintain about a 15 second wait time before each pull \n'
      'That way you avoid getting thrown in jail for doing a DDOS and get referred to as an asshole. [***]\n')
sleep(5)
loop = 1
print('[**] Please wait... [**]\n')
print('[**] Opening drivers with headless option, you wont see anything until it starts pulling links. [**]\n')
print('[*] Retriving https://www.pastebin.com/archive [*]\n')
sleep(5)
while loop == 1:
    try:
        os.system('clear')
        driver = webdriver.ChromeOptions()
        driver.add_argument('headless')
        browse = webdriver.Chrome(chrome_options=driver)
        browse.get("https://www.pastebin.com/archive")
        print('[**] Pulling data [**]\n')
        assert "Pastes Archive" in browse.title
        element = browse.find_elements_by_xpath("//a[@href]")
        database = sqlite3.connect('crawls.sqlite')
        c = database.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS pastebin(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         date_group TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, link TEXT, summary TEXT)''')
        loop = 1
        wait_time = 15
        sql_stmt = "INSERT INTO pastebin(link) VALUES('%s')"
        sql_stmt = str(sql_stmt)

        ignore_urls = '''"%pro%" OR "%tools#%" OR "%facebook%" OR 
                        "%twitter%" OR "%steadfast%" OR "%tribalfusion%" OR "%trends%" OR "%api%" OR "%faq%" OR 
                        "%languages%" OR "%tools%" OR "%privacy%" OR "%cookies_policy%" OR "&contact%" OR "%dmca%"
                        OR "%scraping%" OR "%creativecommons%" OR "%login%" OR "%messages%" OR "%alerts%" 
                        OR "%settings%" '''
        for elem in element:
            hrefs = elem.get_attribute("href")
            print("[!] Item found: %s [!]" % hrefs)
            c.execute(sql_stmt % str(hrefs))
            database.commit()
            loop = 0
        if loop == 0:
            print('[!] While Sleeping, purging DB of garbage URL\'s: %s [!]' % ignore_urls)
            c.execute('DELETE FROM pastebin WHERE link LIKE "%pro%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%language%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%steadfast%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%deal_%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%api%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%login%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%cookies%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%faq%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%dmca%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%scraping%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%messages%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%creativecommons%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%facebook%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%twitter%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%settings%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%privacy%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%tribalfusion%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%tools%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%trends%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%contact%"')
            c.execute('DELETE FROM pastebin WHERE link LIKE "%alert%"')
            database.commit()
            browse.quit()
            sleep(wait_time)
            loop += 1
        continue
    except(KeyboardInterrupt, socket.error) as e:
        database = sqlite3.connect('crawls.sqlite')
        c = database.cursor()
        ignore_urls = '''"%pro%" OR "%tools#%" OR "%facebook%" OR 
                "%twitter%" OR "%steadfast%" OR "%tribalfusion%" OR "%trends%" OR "%api%" OR "%faq%" OR 
                "%languages%" OR "%tools%" OR "%privacy%" OR "%cookies_policy%" OR "&contact%" OR "%dmca%"
                OR "%scraping%" OR "%creativecommons%" OR "%login%" OR "%messages%" OR "%alerts%" OR "%settings%" '''
        import sys
        browse.quit()
        print('[!] Sanitizing and Exiting due to: %s[!]'% str(e))
        print('[!] Deleting: %s [!]' % str(ignore_urls))
        c.execute('DELETE FROM pastebin WHERE link LIKE "%alert%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%contact%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%pro%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%language%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%steadfast%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%deal_%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%api%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%login%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%cookies%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%faq%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%dmca%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%scraping%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%messages%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%creativecommons%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%facebook%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%twitter%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%settings%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%privacy%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%tribalfusion%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%tools%"')
        c.execute('DELETE FROM pastebin WHERE link LIKE "%trends%"')
        database.commit()
        print('[!] Database sanitized! [!]')
        database.close()
        print('[!] ChromeDriver exited! Good-bye [!]')
        sys.exit(1)