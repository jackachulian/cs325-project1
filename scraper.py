import requests
from bs4 import BeautifulSoup
import os
import re

game_ids_to_scrape = [
    "2864390", #Mana Cycle
    "413150", #Stardew Valley
    "1145360", #Hades
    "2344520", #Diablo 4
    "1623730"  #"Palworld"
]

class SteamReviewScraper:
    def __init__(self, url):
        self.url = url

    # Retrieves steam reviews for this scraper's url and saves them to a text file with the game's name in the steam_reviews subdir.
    def get_steam_reviews(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }

        # Fetch the Steam reviews page
        response = requests.get(self.url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page: {response.status_code}")
            return
        
        # Parse the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser') # <-- Use of classes (for OOP requirement)

        # Grab the app name which will be used for the file name instead of the id if a name is found
        app_name_div = soup.find(class_="apphub_AppName")
        app_name = app_name_div.get_text(strip=True) if app_name_div else game_id
        
        # Find all reviews by looking for the div with class 'apphub_CardTextContent'
        review_divs = soup.find_all('div', class_='apphub_CardTextContent')
        
        if not review_divs:
            print("No reviews found on the page.")
            return
        
        # This will remove the post date and early access review header, which is not needed for the AI.
        unwanted_text_pattern = re.compile(r'^Posted:\s+[A-Za-z]+\s+\d{1,2}(?:,\s+\d{4})?')
        
        # Create a directory for saving the review files
        os.makedirs("steam_reviews", exist_ok=True)

        # Save each review as a separate file
        filename = os.path.join("steam_reviews", f"{app_name}.txt")
        with open(filename, 'w', encoding='utf-8') as file:
            for idx, review_div in enumerate(review_divs):
                # Extract the review text
                review_text = review_div.get_text(strip=True)

                # Filter out unwanted text
                review_text = re.sub(unwanted_text_pattern, '', review_text).strip()
                review_text = review_text.replace("Early Access Review", "")
                
                # Skip empty reviews
                if len(review_text) > 0:
                    # Save the review to a text file
                    file.write(review_text+"\n")
                    print(f"Added review {idx + 1} to {filename}")



if __name__ == "__main__":
    for game_id in game_ids_to_scrape:
        game_reviews_url = 'https://steamcommunity.com/app/'+game_id+'/reviews/?browsefilter=toprated'
        scraper = SteamReviewScraper(game_reviews_url)
        scraper.get_steam_reviews()
