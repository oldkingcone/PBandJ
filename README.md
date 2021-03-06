# PBandJ :)
PasteBin Crawler, crawls this url [Pastebin Archive](https://www.pastebin.com/archive)
Presently crawls only that URL for all new pastes within that page, commits all found pastes into a database and trims out unwanted URL's, closes the connection and sleeps for 15 seconds to avoid overloading the server and being an pain in the rear, the repulls the page for new pastes, and repeats the process.

I will be expanding it to crawl all URL's found and store a summary of those contents into an SQLITE3 database. Presently, it parses the links and stores all inside an SQLITE database and then trims out the fat by pulling #MOST unwanted links out of the database.

Please note, upon loading and calling the Chrome driver(**_if it is indeed in your path_**) the script will appear to hang, it is not hanging or broken. The script is loading a bloated driver into memory and requesting the specified URL, or list of URL's. Please be patient as it is working.

# **Usage:**
- You will **need** to export into your path either the chrome driver(_Chromium_) or firefox(_Gecko_)
- Next, you need to change directory into the cloned directory.
- *Run, sudo pip install -r requirements.txt (Linux based systems)
* on BSD based systems: pip install -r requirements.txt --user
- Then enter the command as follows: python ./pbandj.py
- Crack open a cold one with the boys(or girls) and watch as the script does its magic.

This will work on BSD and Linux systems.

# **To do list:**

- **1.** _Windows Compatability._
- **2.** _Clean up DB so that only paste links are present within the DB._
- **3.** _Collect a summary of contents within each paste._
- **4.** _Filtering to search for specific strings contained within each paste.(DB functionality based on summary.)_
- **5.** _Add event trapping for assert failures before the user wants to stop crawling._
- **6.** _Figure out a more simple method to execute many SQL commands at once from the python script, **OR** set up triggers within the database **OR** have all deletion commands execute once the script is exited by the user on the clean up._

# **Future Implementation:**
- **1.** _Write Scrapy version of this, for a more dynamic crawler._


# **Scrapy spider usage:**
- On linux systems, use **apt install python-scrapy** to install the scrapy command line utilities, next you will want to **cd** into the freshly cloned directory, and use this command **scrapy crawl pb_main**, this command will start the spider.
- If you are having issues on running the spider, from within scrapy, please refer to the scrapy docs to get a better understanding on how to manage Scrapy spiders from the linux command like, with the scrapy utils. [Scrapy Docs](https://doc.scrapy.org/en/latest/intro/tutorial.html)
- Please make note, as this develops there will be more functionality added into it. Please be patient, more greatness is coming.

# **Closing:**

- Any of you looking to jump onto this project, feel free to reach out to me at [PBandJ Project Email](mailto:pbandjproject@protonmail.com) pbandjproject at protonmail dot com
- Dicord Server: [Discord invite Link](https://discord.gg/7Thyupp)
