What this program covers:
-------------------------

- The main purpose of this project is to understand the basics of how to quickly extract data from websites and use it for our own purposes.
- Import the necessary modules.
- Select any URL for scraping. Here, I used the CDKeys website to scrap their product prices.
- We need to then make a request and parse the response as HTML. This can be done using the Requests library and BeautifulSoup.
- In this example, I selected the original prices fields and each product on the page.
- Use the json module to convert the data in the HTML attributes to JSON.
- In this example, there was literally an HTML attribute that had a JSON string of all the product information on the CDKeys site. Usually, you’re not so lucky and will have to select the inner text or HTML of specific tags.
