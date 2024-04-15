import csv
import re
import requests
from bs4 import BeautifulSoup

def get_country_url(country_name):
    if country_name.lower() == "deutschland":
        return "https://www.realitica.com/immobilien/Deutschland/"
    else:
        return f"https://www.realitica.com/nekretnine/{country_name}/"

def get_city_url(city_name, country_name):
    if country_name.lower() == "crna-gora":
        return f"https://www.realitica.com/nekretnine/{city_name}/Crna-Gora/"
    elif country_name.lower() == "deutschland":
        return f"https://www.realitica.com/immobilien/{city_name}/"
    else:
        return f"https://www.realitica.com/nekretnine/{city_name}/"

def scrape_webpage(url, csvfile):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all sibling div elements containing property information
    thumb_div_elements = soup.find_all("div", class_="thumb_div")
    property_div_elements = [div.find_next_sibling("div") for div in thumb_div_elements]
    
    # List to store the extracted information of all property ads
    property_ads_info = []

    # Extract data from each property ad
    for div_element in property_div_elements:
        a_tag = div_element.find("a", href=True)
        if a_tag:
            ad_info = {}
            href = a_tag["href"]
            ad_response = requests.get(href)
            ad_soup = BeautifulSoup(ad_response.content, 'html.parser')

            # Extract relevant information from the ad webpage
            ad_info["Vrsta"] = ad_soup.find(string="Vrsta").next_element.strip().lstrip(': ') if ad_soup.find(string="Vrsta") and ad_soup.find(string="Vrsta").next_element else None
            ad_info["Područje"] = ad_soup.find(string="Područje").next_element.strip().lstrip(': ') if ad_soup.find(string="Područje") and ad_soup.find(string="Područje").next_element else None
            ad_info["Lokacija"] = ad_soup.find(string="Lokacija").next_element.strip().lstrip(': ') if ad_soup.find(string="Lokacija") and ad_soup.find(string="Lokacija").next_element else None
            ad_info["Cijena"] = ad_soup.find(string="Cijena").next_element.strip().lstrip(': ') if ad_soup.find(string="Cijena") and ad_soup.find(string="Cijena").next_element else None
            ad_info["Spavaćih Soba"] = ad_soup.find(string="Spavaćih Soba").next_element.strip().lstrip(': ') if ad_soup.find(string="Spavaćih Soba") and ad_soup.find(string="Spavaćih Soba").next_element else None
            ad_info["Kupatila"] = ad_soup.find(string="Kupatila").next_element.strip().lstrip(': ') if ad_soup.find(string="Kupatila") and ad_soup.find(string="Kupatila").next_element else None
            ad_info["Stambena Površina"] = ad_soup.find(string="Stambena Površina").next_element.strip().lstrip(': ') if ad_soup.find(string="Stambena Površina") and ad_soup.find(string="Stambena Površina").next_element else None
            ad_info["Klima Uređaj"] = "Klima Uređaj" in ad_soup.text

            # Append the extracted information to the list
            property_ads_info.append(ad_info)

    # Write extracted information to a CSV file with UTF-8 encoding
    with open(csvfile, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Vrsta', 'Područje', 'Lokacija', 'Cijena', 'Spavaćih Soba', 'Kupatila', 'Stambena Površina', 'Klima Uređaj']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for ad_info in property_ads_info:
            writer.writerow(ad_info)

def get_country():
    countries = ["Hrvatska", "Crna-Gora", "Srbija", "Bosna-i-Hercegovina", "Makedonija", "Deutschland", "svijet"]
    print("Select a country:")
    for idx, country in enumerate(countries, start=1):
        print(f"{idx}. {country}")
    country_idx = int(input("Enter the number of the country: ")) - 1
    return countries[country_idx]

def get_city(country_name):
    country_url = get_country_url(country_name)
    response = requests.get(country_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the form element containing city links
    city_form = soup.find("form")
    if city_form:
        # Find all links within the form element and filter out those not matching the city format
        city_links = city_form.find_all("a", href=True)
        city_links = [link for link in city_links if f"/nekretnine/" or f"/immobilien/" in link.get("href")]
    else:
        # If no form element is found, search for city links in the entire page
        if country_name == 'Crna-Gora':
            city_links = soup.find_all("a", {"href": re.compile(f"/nekretnine/.*/{country_name}/$")})
        elif country_name == 'Deutschland':
            city_links = soup.find_all("a", {"href": re.compile(f"/immobilien/.*/$")})
        else:
            city_links = soup.find_all("a", {"href": re.compile(f"/nekretnine/.*/$")})
    
    cities = [link.get_text() for link in city_links]
    print("Select a city:")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city}")
    city_idx = int(input("Enter the number of the city: ")) - 1
    return cities[city_idx]

def get_city_area_links(city_name):
    base_url = "https://www.realitica.com/nekretnine/"
    url = base_url + city_name + "/Crna-Gora/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    city_area_links = {}
    
    # Find all links containing the city name in their href attribute
    links = soup.find_all("a", href=lambda href: href and city_name in href)
    for link in links:
        href = link.get("href")
        city_area = link.text.strip()
        
        # Find the grand-grand-parent element
        grand_grand_parent = link.find_parent("div").find_parent("div")
        
        # Check if the grand-grand-parent element exists before accessing it
        if grand_grand_parent:
            # Check if the link is for a city area by examining its grand-grand-parent input element
            if grand_grand_parent.find("input", {"type": "checkbox", "name": "cty[]"}):
                city_area_links[city_area] = href
    
    return city_area_links

def main():
    country_name = get_country()
    city_name = get_city(country_name).split(' (')[0].lower()

    city_area_links = get_city_area_links(city_name)
    
    print("City Area Links:")
    for city_area, link in city_area_links.items():
        print(f"{city_area}: {link}")

    # Define the CSV file to store the data
    csvfile = 'property_ads_info.csv'

    # Scrape all city area links
    for link in city_area_links.values():
        scrape_webpage(link, csvfile)


if __name__ == "__main__":
    main()
