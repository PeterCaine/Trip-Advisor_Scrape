# Trip-Advisor_Scrape
Scraping Trip Advisor using Python and Selenium

- download and install selenium (https://selenium-python.readthedocs.io/installation.html or pip install selenium)
- download and install geckodriver (for Firefox): https://github.com/mozilla/geckodriver/releases (this can be placed directly into the folder where you run your .py files from (or ipynb notebook, or added to path))

Scraping Trip Advisor requires a few decisions to be made on the part of the user:
- How many airlines; 
- How many reviews per airline. 
It also takes a while, so if you want to do a little this time and wish to continue where you left off last time, that adds even more options.


At the beginning of the programme you are prompted to:
- enter the path to geckodriver (Linux - only - windows users should put driver in same directory as .py files otherwise add to PATH)
- add the number of Trip Advisor pages of companies to scrape (5 companies per page)
- add the start page (if you have previously scraped 10 pages, enter 11 to continue where you left off)
- enter number of reviews per company (experimentation showed that around 1500 was possible without connection issues - max values are prone to errors midway. The pickle files will still write out, but it's still annoying).
- At what point do you wish to start (the pickle files are written with the name of the airline and number of pages of reviews scraped - you can continue by entering the next number (if there are any more to scrape)).

- a pickle file is output containing a binary version of the raw html of each review. I'll set up another repo so to unpack it. 

- a txt file of the companies scraped is also output to the airline_pickles folder.