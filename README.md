# PBandJ
PasteBin Crawler, crawls the url [Pastebin Archive](https://www.pastebin.com/archive)
Presently crawls only that URL for all new pastes within that page, commits all found pastes into a database and trims out unwanted URL's, closes the connection and sleeps for 15 seconds to avoid overloading the server and being an pain in the rear, the repulls the page for new pastes, and repeats the process.

I will be expanding it to crawl all URL's found and store a summary of those contents into an SQLITE3 database. Presently, it parses the links and stores all inside an SQLITE database and then trims out the fat by pulling #MOST unwanted links out of the database. Need to find a more simple way to execute all the delete commands at once.

This will work on BSD and Linux systems.

**To do list:**

**1.** _Windows Compatability._
**2.** _Clean up DB so that only paste links are present within the DB._
**3.** _Collect a summary of contents within each paste._
**4.** _Filtering to search for specific strings contained within each paste.(DB functionality based on summary.)_
**5.** _Add event trapping for assert failures._
