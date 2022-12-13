import requests

def search_keyword():
  # Ask the user for the URL to search
  url = input("Enter the URL to search: ")

  # Ask the user for the keyword to search for
  keyword = input("Enter the keyword to search for: ")

  # Use the requests module to fetch the HTML of the website
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Get the HTML of the website as a string
    html = response.text

    # Search for the keyword in the HTML
    occurrences = []
    index = 0
    while True:
      # Find the next occurrence of the keyword in the HTML
      index = html.find(keyword, index)
      if index == -1:
        # Keyword not found, exit the loop
        break
      else:
        # Keyword found, add the index to the list of occurrences
        occurrences.append(index)

        # Increment the index to search for the next occurrence
        index += len(keyword)

    # Return the list of occurrences
    return occurrences
  else:
    print(f"Failed to fetch HTML for {url}")

# Test the search_keyword function
occurrences = search_keyword()
print(occurrences)