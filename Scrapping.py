import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the number of pages to parse", type=int)
parser.add_argument("--dbname",help="Enter the database name", type=str)
args =parser.parse_args()

url = "https://www.oyorooms.com/hotels-in-mumbai//?page="


page_num_Max= args.page_num_max
scrap_info_list =[]
connect.connect(args.dbname)
for page_num in range(1,page_num_Max):
    Url = url + str(page_num)
    req = requests.get(Url)
    print("Get Request for: "+ Url )
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div", {"class":"hotelCardListing"})
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find_all("h3", {"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["address"]=hotel.find_all("span", {"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find_all("span", {"class":"listingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"] = hotel.find_all("span",{"class":"hotelRating__ratingSummart"}).text
        except AttributeError:
            hotel_dict["rating"] = None
        
        
        pae = hotel.find_all("div",{"class":"amenityWrapper"})
        
        am_list = []
        for am in pae.find_all("div",{"class":"amenityWrapper"}) :
            am_list.append(am.find("span", {"class":"d-body-sm"}).text.strip())
        hotel_dict["amenity"] = ', '.join(am_list[:-1])
        
        scrap_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))
#data for creating data at the end 
dataFrame = pandas.DataFrame(scrap_info_list)
print("Creating CSV File....")
dataFrame.to_csv("Mumbai-oyo.csv")
connect.get_hotel_info(args.dbname)