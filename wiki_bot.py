import wikipediaapi
import requests

# Define the user agent
user_agent = 'WikiBot/1.0 (liomad999@gmail.com)'

# Function to fetch Wikipedia summary
def fetch_wikipedia_summary(topic):
    # Define the URL for Wikipedia API
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + topic
    
    # Set up headers including the user agent
    headers = {'User-Agent': user_agent}
    
    # Send a GET request to the Wikipedia API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data.get('extract', 'No summary available for this topic.')
    else:
        return "The page does not exist on Wikipedia or there was an error retrieving it."

if __name__ == "__main__":
    topic = input("Enter the topic you want to search on Wikipedia: ")
    summary = fetch_wikipedia_summary(topic)
    print(f"\nSummary of {topic}:\n{summary}")
