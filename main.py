import os, platform
from utils import get_links_to_scrape, start_scrape, trip_advisor_scrape


def main ():
    main_url = 'https://www.tripadvisor.com/Airlines'
        
    prompt = "Add number of Trip Advisor pages of companies to scrape: (default = 10 @ 5 companies per page - 50 companies): "
    page_input = input(prompt)
    if page_input == '':
        page_input = 10
    else:
        page_input = int(page_input)
    
    prompt = "Add start page (default = 0): "
    start_input = input (prompt)
    if start_input == '':
        start_input = 0
    else:
        start_input = int(start_input)
        
    prompt = "Enter number of reviews per company: "
    num_reviews_input = input (prompt)
    
    prompt = "At what point do you wish to start your scrape (page_num - if you have scraped before enter last page, otherwise enter 0): "
    start = input(prompt)
        
    urls = get_links_to_scrape(main_url, start=start_input, num_pages=page_input)

    
    for url in urls:
        driver = start_scrape(url, start=int(start_input))
        trip_advisor_scrape(driver, url, start=int(start), num_reviews=int(num_reviews_input))
        driver.quit()
        
if __name__ == "__main__":
    
    if platform.system() == "linux" or platform.system() == "linux2":
        prompt = "Enter path to geckodriver (default is current working directory): "
        path_input = input(prompt)
        if path_input == '':
            path = os.getcwd()
            print('\n', 'Gecko driver is expected to be at: ', path, '\n')
        else:
            path = path_input
        os.environ["PATH"] += os.pathsep + path
    if not os.path.exists('./airline_pickles'):
        os.mkdir('airline_pickles')
    main()