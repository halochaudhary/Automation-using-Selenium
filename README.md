# Automation-using-Selenium

## Selenium Getting Data

This repository contains a Python script that uses Selenium WebDriver to automate a search on Amazon.in and retrieve product names from the search results. It's a basic example of web scraping with Selenium and can be extended for more complex tasks.

### Features

- **Browser Automation:** Automates a web browser using Selenium WebDriver.
- **Amazon Search:** Opens Amazon.in and performs a search for a specified product (iPhones in this example).
- **Data Retrieval:** Collects and prints the names of the search results.
- **Result Display:** Displays the number of products found and their names.

### Prerequisites

- **Selenium WebDriver:** Ensure you have Selenium WebDriver installed. You can install it using pip:
  ```sh
  pip3 install selenium
  ```
  or
  ```sh
  sudo apt install python3-selenium
  ```
- **WebDriver Executable:** Download the appropriate WebDriver executable for your browser (e.g., ChromeDriver for Google Chrome) and ensure it's in your system PATH or specify the path explicitly in the script.

### Usage

1. **Setup WebDriver:**
   Ensure that the WebDriver executable (e.g., `chromedriver` for Chrome) is available in your system PATH or specify its path in the script.

2. **Run the Script:**
   Execute the script using Python:
   ```sh
   python3 selenium_getting_data.py
   ```

### Example Code

```python
from selenium import webdriver
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Amazon.in
driver.get('http://www.amazon.in')

# Maximize the browser window
driver.maximize_window()

# Perform a search for 'iphones'
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('iphones')
driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()

# Retrieve the list of product names
list = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")

# Print the number of products found and their names
print(str(len(list)) + ' products found')
for i in list:
    print(i.text)

# Pause to allow manual inspection
time.sleep(30)

# Quit the WebDriver
driver.quit()
```

### Notes

- **Deprecation Warning:** The methods `find_element_by_xpath` and `find_elements_by_xpath` are deprecated in recent versions of Selenium. Consider using `find_element` and `find_elements` with appropriate `By` imports.
- **Delay for Manual Inspection:** The `time.sleep(30)` is included to allow manual inspection of the browser window before it closes. Adjust or remove as needed.

### Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
