from splinter import Browser

with Browser(driver_name="chrome") as browser:
    # Visit URL
    url = "https://www.google.com.tw"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnK')
    # Interact with elements
    #button.click()
    if browser.is_text_present('splinter.readthedocs.org'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
