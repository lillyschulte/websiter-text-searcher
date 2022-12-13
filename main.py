from urllib.parse import urlparse

def search_keyword(url, keyword):
  import requests
  import re

  # Use the requests module to fetch the HTML of the website
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Get the HTML of the website as a string
    html = response.text

    # Use a regular expression to find all URLs in the HTML
    url_regex = r'https?://\S+'
    urls = re.findall(url_regex, html)

    # Parse the original URL to extract its domain
    original_domain = urlparse(url).netloc

    # Search for the keyword in the HTML
    occurrences = []
    index = 0
    line_number = 1
    while True:
      # Find the next occurrence of the keyword in the HTML
      index = html.find(keyword, index)
      if index == -1:
        # Keyword not found, exit the loop
        break
      else:
        # Keyword found, add the line number and index to the list of occurrences
        occurrences.append((line_number, index))

        # Increment the line number if a newline character is found
        if html[index] == "\n":
          line_number += 1

        # Increment the index to search for the next occurrence
        index += len(keyword)

    # Recursively search the HTML of any underlying web pages
    visited_urls = []
    for url in urls:
      # Skip URLs that have already been visited
      if url in visited_urls:
        continue

      # Add the URL to the list of visited URLs
      visited_urls.append(url)

      # Search the HTML of the underlying web page
      subpage_occurrences = search_keyword(url, keyword)

      # Add the occurrences found in the underlying web page to the list of occurrences
      occurrences.extend(subpage_occurrences)

    # Return the list of occurrences
    return occurrences
  else:
    print(f"Failed to fetch HTML for {url}")

#url = input("URL:")
#keyword = input("Keyword:")
url = "http://thiccbois.nl"
keyword = "worst"
search_keyword(url, keyword)

