# scraping_watch

## Flipkart Watches Scraper

This project contains a Python script that scrapes the names, prices, and ratings of men's watches under ₹2000 from Flipkart.

### Features

- Uses `requests` and `BeautifulSoup` to fetch and parse product data from Flipkart.
- Extracts product names, prices, and ratings.
- Saves the data into an Excel file called `newflipkart_watches.xlsx` using `pandas`.

### How to Use

1. **Install Dependencies**  
   Make sure you have the required libraries installed:
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl
   ```

2. **Run the Script**  
   Execute the Python script:
   ```bash
   python <script_name>.py
   ```
   Replace `<script_name>.py` with the actual name of your script file.

3. **Output**  
   After running, you'll find a file named `newflipkart_watches.xlsx` in your working directory containing the scraped data.

### Note

- This script scrapes data from Flipkart's search results page for men's watches under ₹2000.
- The script is for educational purposes. Website structure may change, so selectors might need updates in the future.# scraping_watch
