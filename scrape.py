from instream import InStream 
import pandas as pd 

def get_url(start_index, page):
    end_index = page.find(' class="p24_content "', start_index) - 1 
    start_index = page.find('href=', (end_index-100)) + len('href=') + 1  
    link = page[start_index:end_index]
    url = 'https://www.property24.com' + link
    return url, end_index 

def get_price(start_index, page):
    start_index = page.find('itemprop="price" content="', start_index) + len('itemprop="price" content="')
    if (start_index == 25): 
        return "end of page", 0 
    end_index = page.find('"', start_index) 
    price = page[start_index:end_index]
    return price, end_index 

def get_type(start_index, page):
    start_index = page.find('itemprop="name">', start_index) + len('itemprop="name">') 
    end_index = page.find('<', start_index)  
    type = page[start_index:end_index]
    return type, start_index 

def get_location(start_index, page):
    start_index = page.find('<span class="p24_location ">', start_index) + len('<span class="p24_location ">') 
    end_index = page.find('<', start_index) 
    location = page[start_index:end_index]
    return location, start_index

def get_bedrooms(start_index, page):
    pass

def get_bathrooms(start_index, page):
    pass

def get_garage(start_index, page):
    pass
    
def get_erf(start_index, page):
    pass

def get_num_pages(first_page):
    index_six = first_page.find('data-pagenumber="6"') + len('data-pagenumber="6"')
    start_last_page = first_page.find('data-pagenumber="', index_six) + len('data-pagenumber="')
    end_last_page = first_page.find('"', start_last_page) 
    last_page = first_page[start_last_page:end_last_page]
    return int(last_page)

def get_next_page(next_page_num, current_page):
    end_index = current_page.find(f' data-pagenumber="{next_page_num}"') - 1
    start_index = current_page.find('href=', (end_index-100)) + len('href=') + 1  
    url = current_page[start_index:end_index]
    instream_url = InStream(url) 
    next_page = instream_url.readAll() 
    return next_page 
    
def collect_data(first_page, num_pages):
    page = first_page
    next_page = 2
    # Initialise lists 
    prices = []; urls = []; types = []; locations = []; bedrooms = []; bathrooms = []; garage = []; erf_size = [] 
    while (next_page <= num_pages):
        i = 0 
        start_index = 0 
        while i < 25: 
            url, start_index = get_url(start_index, page) 
            price, start_index = get_price(start_index, page)
            type, start_index = get_type(start_index, page) 
            location, start_index = get_location(start_index, page) 
            if (price == "end of page"): 
                # Last unit is always an auction, which is not considered in this model 
                urls.pop() 
                prices.pop() 
                types.pop()
                locations.pop() 
                break 
            urls += [url] 
            prices += [price]
            types += [type] 
            locations += [location] 
            i += 1
        page = get_next_page(next_page, page) 
        next_page += 1 
 
def main():
    # URL of first search page for properties in Cape Town 
    url = "https://www.property24.com/for-sale/cape-town/western-cape/432?sp=pt%3d1500000"
    instream_url = InStream(url)
    # String of first page 
    first_page = instream_url.readAll()
    num_pages = get_num_pages(first_page)
    # csv of scraped data 
    collect_data(first_page, num_pages) 

if __name__ == "__main__": main() 
