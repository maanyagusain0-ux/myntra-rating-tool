from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_rating(driver):

    try:

        wait = WebDriverWait(driver, 1.5)
 
        rating_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "index-overallRating")
            )
        )

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

    except:

        # Product has no rating
        return "No Rating", "No Rating"