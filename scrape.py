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
    return type, end_index 

def get_location(start_index, page):
    start_index = page.find('<span class="p24_location ">', start_index) + len('<span class="p24_location ">') 
    end_index = page.find('<', start_index) 
    location = page[start_index:end_index]
    return location, end_index

def get_feature_details(start_index, page):
    start_index = page.find('<span class="p24_icons">', start_index) + len('<span class="p24_icons">')
    return_index = start_index  
    available_feautures = [False, False, False, False, False]
    i = 0 
    while i < 5:
        start_index = page.find('title="', start_index) + len('title="') 
        end_index = page.find('"', start_index) 
        item = page[start_index:end_index]
        if (item == "Bedrooms") and (i < 1):
            available_feautures[0] = True 
            i = 1 
        elif (item == "Bathrooms") and (i < 2): 
            available_feautures[1] = True  
            i = 2 
        elif (item == "Parking Spaces") and (i < 3): 
            available_feautures[2] = True 
            i = 3 
        elif (item == "Erf Size") and (i < 4):
            available_feautures[3] = True 
            i = 4 
        elif (item == "Floor Size") and (i < 5):
            available_feautures[4] = True 
            i = 5 
        # Once 'i' is greater than its corresponding feature, we are on a different property 
        else: 
            return available_feautures, return_index
        start_index = end_index  
    return available_feautures, return_index 

def get_bedrooms(start_index, page):
    start_index = page.find('"Bedrooms"', start_index) + len('"Bedrooms"')
    start_index = page.find('<span>', start_index) + len('<span>') 
    end_index = page.find('</span>', start_index)  
    bedrooms = page[start_index:end_index] 
    return bedrooms, end_index 

def get_bathrooms(start_index, page):
    start_index = page.find('"Bathrooms"', start_index) + len('"Bathrooms"')
    start_index = page.find('<span>', start_index) + len('<span>') 
    end_index = page.find('</span>', start_index)  
    bathrooms = page[start_index:end_index] 
    return bathrooms, end_index 

def get_parkings(start_index, page):
    start_index = page.find('"Parking Spaces"', start_index) + len('"Parking Spaces"')
    start_index = page.find('<span>', start_index) + len('<span>') 
    end_index = page.find('</span>', start_index) 
    parkings = page[start_index:end_index] 
    return parkings, end_index 

def get_erf(start_index, page):
    start_index = page.find('"Erf Size"', start_index) + len('"Erf Size"')
    start_index = page.find('<span>', start_index) + len('<span>') 
    end_index = page.find(' ', start_index) 
    erf = page[start_index:end_index] 
    return erf, end_index 

def get_floor(start_index, page):
    start_index = page.find('"Floor Size"', start_index) + len('"Floor Size"')
    start_index = page.find('<span>', start_index) + len('<span>') 
    end_index = page.find(' ', start_index) 
    floor = page[start_index:end_index] 
    return floor, end_index

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
    prices = []; urls = []; types = []; locations = []; num_bedrooms = []; num_bathrooms = []; parking_spaces = []; erf_size = []; floor_size = []  
    while (next_page <= num_pages):
        i = 0 
        start_index = 0 
        # Scrape content from one page
        while i < 25: 
            url, start_index = get_url(start_index, page) 
            price, start_index = get_price(start_index, page)
            type, start_index = get_type(start_index, page) 
            location, start_index = get_location(start_index, page) 
            # Check which features are available, returns a boolean array 
            available_features, start_index = get_feature_details(start_index, page) 
            # Available features are stored, missing values are represented by 'None'
            if available_features[0] is True:
                bedrooms, start_index = get_bedrooms(start_index, page) 
            else: 
                bedrooms = None 
            if available_features[1] is True: 
                bathrooms, start_index = get_bathrooms(start_index, page) 
            else: 
                bathrooms = None 
            if available_features[2] is True: 
                parkings, start_index = get_parkings(start_index, page) 
            else: 
                parkings = None 
            if available_features[3] is True: 
                erf, start_index = get_erf(start_index, page) 
            else: 
                erf = None 
            if available_features[4] is True: 
                floor, start_index = get_floor(start_index, page) 
            else: 
                floor = None 
            if (price == "end of page"): 
                # Last unit is always an auction, which is not considered in this model 
                urls.pop(); prices.pop(); types.pop(); locations.pop(); num_bedrooms.pop(); num_bathrooms.pop(); parking_spaces.pop(); erf_size.pop(); floor_size.pop() 
                break 
            urls += [url] 
            prices += [price]
            types += [type] 
            locations += [location] 
            i += 1
            num_bedrooms += [bedrooms]
            num_bathrooms += [bathrooms] 
            parking_spaces += [parkings] 
            erf_size += [erf] 
            floor_size += [floor] 
        page = get_next_page(next_page, page) 
        next_page += 1 
    # Combine lists into a data frame, then a csv file
    create_csv(urls, prices, types, locations, num_bedrooms, num_bathrooms, parking_spaces, erf_size, floor_size)
    
def create_csv(urls, prices, types, locations, num_bedrooms, num_bathrooms, parking_spaces, erf_size, floor_size):
    data = {
        "Price": prices,
        "URL": urls,
        "Type": types, 
        "Location": locations,
        "Bedrooms": num_bedrooms,
        "Bathrooms": num_bathrooms, 
        "Parking Spaces": parking_spaces, 
        "Erf Size": erf_size, 
        "Floor Size": floor_size
    }
    df = pd.DataFrame(data)
    # The csv file is saved for further processing 
    df.to_csv('property_data.csv', index=False)
    print(df) 

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
