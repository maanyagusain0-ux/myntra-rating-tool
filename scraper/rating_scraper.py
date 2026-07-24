from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def extract_rating(driver):
    try:
        # Extended wait time from 1.5s to 5s to allow slow rendering elements to appear
        wait = WebDriverWait(driver, 5)

        rating_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "index-overallRating")
            )
        )

        print("FOUND RATING TEXT:")
        print(rating_element.text)

        text = rating_element.text
        lines = text.split("\n")

        rating = lines[0].replace("|", "").strip()
        rating_count = "NA"

        if len(lines) >= 3:
            rating_count = (
                lines[2]
                .replace("Ratings", "")
                .replace(",", "")
                .strip()
            )

        return rating, rating_count

    except Exception as e:
        print("RATING EXTRACTION FAILED")
        print(e)

        # Product has no rating or class was not found in DOM
        return "No Rating", "No Rating"