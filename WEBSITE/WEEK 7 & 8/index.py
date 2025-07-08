from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.airbnb.co.za/")

        select_place = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div/div[2]/div[3]/main/div/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/a"))
        )
        select_place.click()

        print("Current URL:", driver.current_url)
        assert "https://www.airbnb.co.za/rooms/" in driver.current_url, "URL does not contain expected path"

    finally:
        # Close the driver
        driver.quit()
        
        main()
        