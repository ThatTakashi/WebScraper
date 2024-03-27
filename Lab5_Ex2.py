# Python web scraper for blog posts
# By: Takashi
# Date: 28th March 2024

# Import requests to fetch HTML data from a given website
import requests
from bs4 import BeautifulSoup
import json

# Ask the user for input about the target website and target elements
file_name_input = input("Enter a file name to store results: ")
URL = input("Enter the url you would like to scrape (Beginning with https://): ")

print("------------")

title_elements = input("Enter the HTML element of the post title: ")
date_elements = input("Enter the HTML element of the post date: ")
desc_elements = input("Enter the HTML element of the post description: ")

print("------------")

title_class = input("Enter the class name of the post title element")
date_class = input("Enter the class name of the post date element")
desc_class = input("Enter the class name of the post desc element")

page = requests.get(URL)
file_name = file_name_input + ".txt"

data_n = {}

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="wp-block-query-is-layout-flow")

job_elements = results.find_all("li", class_="wp-block-post")

print(f"Blog Posts from {URL}")
print("------------")

for job_element in job_elements:
    post = "Post"
    title_element = job_element.find(title_elements, class_=title_class)
    date_element = job_element.find(date_elements, class_=date_class)
    description_element = job_element.find(desc_elements, class_=desc_class)

    temp = {}
    f = "Title"
    temp[f] = title_element.text.strip()
    print(f"Post title: {title_element.text.strip()}")
    g = "Date Posted"
    temp[g] = date_element.text.strip()
    print(f"Date posted: {date_element.text.strip()}")
    h = "Description"
    temp[h] = description_element.text.strip()
    print(f"Post description: {description_element.text.strip()}")
    print("*------------*")
    data_n[post] = temp

    file = open(file_name, 'a+')
    data = data_n
    json.dump(data, file, indent=4)
