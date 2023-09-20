import openai
import requests
from bs4 import BeautifulSoup

class BlogPostGenerator:
    def __init__(self, gpt3_api_key):
        self.api_key = gpt3_api_key
        self.base_url = "https://www.google.com/search?q="
        self.search_result_limit = 5

    def search_and_generate(self, topic):
        # Step 1: Perform a Google search for the given topic
        search_query = "+".join(topic.split())
        search_url = self.base_url + search_query
        search_results = self.fetch_search_results(search_url)

        # Step 2: Extract information from search results
        content = self.extract_content(search_results)

        # Step 3: Generate the blog post content
        blog_post = self.generate_blog_post(topic, content)
        return blog_post

    def fetch_search_results(self, search_url):
        # Fetch search results from Google
        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('div', class_='tF2Cxc')
            return search_results[:self.search_result_limit]
        else:
            print("Failed to fetch search results.")
            return []

    def extract_content(self, search_results):
        # Extract text content from search results
        content = ""
        for result in search_results:
            # Extract text from the "r" class instead of "BNeawe iBp4i AP7Wnd"
            snippet = result.find('div', class_='r').get_text()
            content += snippet + "\n\n"
        return content

    def generate_blog_post(self, topic, content):
        # Generate a blog post using GPT-3
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Write a blog post on the topic: {topic}\n\n{content}\n\n",
            max_tokens=1097,  # Adjust the length as needed
            stop=None,
            temperature=1.3,  # Adjust the temperature for creativity
        )
        return response.choices[0].text.strip()

if __name__ == "__main__":
    gpt3_api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your GPT-3 API key
    agent = BlogPostGenerator(gpt3_api_key)

    # Input: Topic for the blog post
    topic = "Benefits of Artificial Intelligence in Healthcare"

    # Generate the blog post
    blog_post = agent.search_and_generate(topic)

    # Print the generated blog post
    with open('blog.txt','w') as file:
        file.write(blog_post)
    # print(blog_post)
