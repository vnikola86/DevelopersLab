import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all sibling div elements containing property information
    thumb_div_elements = soup.find_all("div", class_="thumb_div")
    property_div_elements = [div.find_next_sibling("div") for div in thumb_div_elements]
    
    # Print the href links for individual ads
    print("Href links for individual ads:")
    for div_element in property_div_elements:
        a_tag = div_element.find("a", href=True)
        if a_tag:
            href = a_tag["href"]
            print(href)

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
    city_name = input("Enter the city name: ").strip().lower()
    city_area_links = get_city_area_links(city_name)
    
    print("City Area Links:")
    for city_area, link in city_area_links.items():
        print(f"{city_area}: {link}")

    # Scrape the first link
    if city_area_links:
        first_link = list(city_area_links.values())[0]
        scrape_webpage(first_link)

if __name__ == "__main__":
    main()
