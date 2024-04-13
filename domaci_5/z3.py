import json
from datetime import datetime
import csv

# Load JSON data
with open("data.json", "r") as file:
    json_data = json.load(file)

# Function to search for an article by title
def search_article_by_title(title):
    for article in json_data["data"]["articles"]:
        if article["title"] == title:
            return article
    return None

# Function to add a comment to an article
def add_comment_to_article(title, comment_title, comment_author, comment_description):
    for article in json_data["data"]["articles"]:
        if article["title"] == title:
            if not any(comment["title"] == comment_title for comment in article["comments"]):
                article["comments"].append({
                    "title": comment_title,
                    "author": comment_author if comment_author else "anonim",
                    "description": comment_description
                })
                # Write the updated JSON data back to the file
                with open("data.json", "w") as file:
                    json.dump(json_data, file, indent=4)
                return True
            else:
                print("Comment with the same title already exists.")
                return False
    print("Article not found.")
    return False

# Function to delete an article based on comment title
def delete_article_by_comment_title(comment_title):
    for article in json_data["data"]["articles"]:
        for comment in article["comments"]:
            if comment["title"] == comment_title:
                json_data["data"]["articles"].remove(article)
                # Write the updated JSON data back to the file
                with open("data.json", "w") as file:
                    json.dump(json_data, file, indent=4)
                return True
    print("Article with the specified comment title not found.")
    return False

# Function to get a comment by title
def get_comment_by_title(article_title, comment_title):
    article = search_article_by_title(article_title)
    if article:
        for comment in article["comments"]:
            if comment["title"] == comment_title:
                return comment
    return None

# Function to get comments by author
def get_comments_by_author(author):
    comments = []
    for article in json_data["data"]["articles"]:
        for comment in article["comments"]:
            if comment["author"] == author:
                comments.append(comment)
    return comments

# Function to get articles by author and write them to a CSV file sorted by number of comments
def write_articles_to_csv_by_author(author):
    print("Writing articles to CSV...")
    articles = []
    for article in json_data["data"]["articles"]:
        if article["author"] == author or not article["comments"]:
            articles.append(article)
    articles.sort(key=lambda x: len(x["comments"]), reverse=True)
    
    print(f"Number of articles found: {len(articles)}")
    
    for article in articles:
        print(article)  # Print article before writing to CSV
    
    with open(f"{author}_articles.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "author", "description", "category", "views", "comments"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            article_data = {
                "title": article["title"],
                "author": article["author"],
                "description": article["description"],
                "category": article["category"],
                "views": article["views"],
                "comments": len(article["comments"])  # Count of comments
            }
            writer.writerow(article_data)

# Function to get articles by author and write them to a JSON file sorted by number of views
def write_articles_to_json_by_author(author):
    print("Writing articles to JSON...")
    articles = []
    for article in json_data["data"]["articles"]:
        if article["author"] == author or not article["comments"]:
            articles.append(article)
    articles.sort(key=lambda x: x["views"], reverse=True)
    
    print(f"Number of articles found: {len(articles)}")
    
    for article in articles:
        print(article)  # Print article before writing to JSON
    
    with open(f"{author}_articles.json", "w", encoding="utf-8") as jsonfile:
        json.dump(articles, jsonfile, indent=4)


# Test functions
print(search_article_by_title("Apple is Listening"))
print(add_comment_to_article("Apple is Listening", "Great article", "John Doe", "Awesome insights!"))
# print(delete_article_by_comment_title("Great article"))
print(get_comment_by_title("Apple is Listening 2", "Nice"))
print(get_comments_by_author("SolarFan"))
write_articles_to_csv_by_author("Marco Arment")
write_articles_to_json_by_author("Marco Arment")
