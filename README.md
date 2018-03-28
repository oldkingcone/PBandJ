# PBandJ
PasteBin Crawler, crawls the url https://pastebin.com/archive
Presently crawls only that URL for all new pastes within that page, commits all found pastes into a database and trims out unwanted URL's, closes the connection and sleeps for 15 seconds to avoid overloading the server and being an pain in the rear, the repulls the page for new pastes, and repeats the process.

I will be expanding it to crawl all URL's found and store a summary of those contents into an SQLITE3 database. Presently, it parses the links and stores all inside an SQLITE database and then trims out the fat by pulling #MOST unwanted links out of the database. Need to find a more simple way to execute all the delete commands at once.
