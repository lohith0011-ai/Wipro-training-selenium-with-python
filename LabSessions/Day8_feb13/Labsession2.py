from bs4 import BeautifulSoup

html = """
<html>
<head><title>Test Page</title></head>
<body>
<h1>Welcome</h1>
<p>This is a paragraph.</p>
<a href="https://example.com">Click Here</a>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print("HTML Parsed Successfully")

# Extract title text
print("Title :", soup.title.text)

# Extract h1 text
print("H1 :", soup.h1.text)

# Extract paragraph text
print("Paragraph :", soup.p.text)

link = soup.find("a")      # find first <a> tag
print("First Link:", link)
print("Href:", link["href"])

print(soup.prettify())

print(soup.find("p"))        # First paragraph
print(soup.find_all("p"))    # List of all paragraphs




from bs4 import BeautifulSoup

html = """
<html>
<body>

<div class="product">
    <h2 class="name">Laptop</h2>
    <p class="price">$800</p>
    <p class="rating">4.5</p>
    <p class="availability">In Stock</p>
    <img src="laptop.jpg">
</div>

</body>
</html>
"""

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Extract product details
product_name = soup.find("h2", class_="name").text
price = soup.find("p", class_="price").text
rating = soup.find("p", class_="rating").text
availability = soup.find("p", class_="availability").text

# Print output
print("Product Name:", product_name)
print("Price:", price)
print("Rating:", rating)
print("Availability:", availability)

# Find all image tags
images = soup.find_all("img")

# Print image URLs
for img in images:
    print(img["src"])