# import requests


# from bs4 import BeautifulSoup


# class BlogPostGenerator:
#     def __init__(self):
#         self.base_url = "https://www.google.com/search?q="
#         self.search_result_limit = 5  # Limit the number of search results to fetch

#     def search_and_generate(self, topic):
#         # Step 1: Perform a Google search for the given topic
#         search_query = "+".join(topic.split())  # Format topic for the URL
#         search_url = self.base_url + search_query
#         search_results = self.fetch_search_results(search_url)
#         # print('df',search_results)
        
#         # Step 2: Extract information from search results and generate the blog post
#         blog_post = self.generate_blog_post(search_results)
#         # print(blog_post)
#         return blog_post

#     def fetch_search_results(self, search_url):
#         # Fetch search results from Google
#         response = requests.get(search_url)
#         # print(response.text)
#         # exit()
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             # search_results = soup.find_all('div', class_='tF2Cxc')
#             search_results = soup.find_all('div')
#             # print('er',search_results)
#             # search_results = soup.prettify()
#             return search_results[:self.search_result_limit]
#         else:
#             print("Failed to fetch search results.")
#             return []

#     def generate_blog_post(self, search_results):
#         # Generate a blog post by extracting text from search results
#         blog_post = ""
       
#         for result in search_results:
#             # snippet = result.find_all('div', class_='BNeawe iBp4i AP7Wnd')
#             snippet = result.find('div')
#             blog_post += snippet + "\n\n"

#         return blog_post

# if __name__ == "__main__":
#     agent = BlogPostGenerator()
#     # print(agent)
#     # Input: Topic for the blog post
#     topic = "Benefits of Artificial Intelligence in Healthcare"

#     # Generate the blog post
#     blog_post = agent.search_and_generate(topic)

#     # Print the generated blog post
#     print(blog_post.capitalize())



# import requests
# from bs4 import BeautifulSoup

# class BlogPostGenerator:
#     def __init__(self):
#         self.base_url = "https://www.google.com/search?q="
#         self.search_result_limit = 5  # Limit the number of search results to fetch

#     def search_and_generate(self, topic):
#         # Step 1: Perform a Google search for the given topic
#         search_query = "+".join(topic.split())  # Format topic for the URL
#         search_url = self.base_url + search_query
#         search_results = self.fetch_search_results(search_url)

#         # Step 2: Extract information from search results and generate the blog post
#         links = self.extract_links(search_results)
#         print('edf',links)
#         blog_post = self.generate_blog_post(links)
#         return blog_post

#     def fetch_search_results(self, search_url):
#         # Fetch search results from Google
#         response = requests.get(search_url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             search_results = soup.find_all('div', class_='tF2Cxc')
#             return search_results[:self.search_result_limit]
#         else:
#             print("Failed to fetch search results.")
#             return []

#     def extract_links(self, search_results):
#         # Extract links from search results
#         links = []
#         for result in search_results:
#             link = result.find('a')['href']
#             links.append(link)
#         return links

#     def generate_blog_post(self, links):
#         # Generate a blog post by including the extracted links
#         blog_post = "Here are some useful links related to the topic:\n\n"
#         print('er',links)
#         for i, link in enumerate(links, start=1):
#             blog_post += f"{i}. {link}\n"
#         return blog_post

# if __name__ == "__main__":
#     agent = BlogPostGenerator()

#     # Input: Topic for the blog post
#     topic = "Benefits of Artificial Intelligence in Healthcare"

#     # Generate the blog post
#     blog_post = agent.search_and_generate(topic)

#     # Print the generated blog post
#     print(blog_post)



# from googlesearch import search

# class BlogPostGenerator:
#     def __init__(self):
#         self.search_result_limit = 5  # Limit the number of search results to fetch

#     def search_and_generate(self, topic):
#         # Step 1: Perform a Google search for the given topic
#         search_results = self.fetch_search_results(topic)

#         # Step 2: Extract information from search results and generate the blog post
#         blog_post = self.generate_blog_post(search_results)
#         return blog_post

#     def fetch_search_results(self, topic):
#         # Perform a Google search and retrieve search results
#         search_results = []
#         for result in search(topic, num_results=self.search_result_limit):
#             search_results.append(result)
#         return search_results

#     def generate_blog_post(self, links):
#         # Generate a blog post by including the extracted links
#         blog_post = "Here are some useful links related to the topic:\n\n"
#         for i, link in enumerate(links, start=1):
#             blog_post += f"{i}. {link}\n"
#         return blog_post

# if __name__ == "__main__":
#     agent = BlogPostGenerator()

#     # Input: Topic for the blog post
#     topic = "Benefits of Artificial Intelligence in Healthcare"

#     # Generate the blog post
#     blog_post = agent.search_and_generate(topic)

#     # Print the generated blog post
#     print(blog_post)




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
