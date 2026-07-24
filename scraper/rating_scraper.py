import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def extract_rating(driver, url):
    driver.get(url)

    # ----------------------------------------------------
    # Step 1: Print basic page info and source snippet
    # ----------------------------------------------------
    print("=" * 80)
    print("CURRENT URL:", driver.current_url)
    print("PAGE TITLE:", driver.title)
    print("\n--- FIRST 5000 CHARS OF PAGE SOURCE ---")
    print(driver.page_source[:5000])
    print("=" * 80)

    # ----------------------------------------------------
    # Step 2: Check if rating keywords exist in HTML
    # ----------------------------------------------------
    print("Contains overallRating:", "index-overallRating" in driver.page_source)
    print("Contains Rating:", "Rating" in driver.page_source)

    # ----------------------------------------------------
    # Step 3: Save complete HTML to local file for inspection
    # ----------------------------------------------------
    try:
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Successfully saved page source to page.html")
    except Exception as e:
        print("Failed to save page.html:", e)

    # ----------------------------------------------------
    # Extraction Logic
    # ----------------------------------------------------
    try:
        wait = WebDriverWait(driver, 5)

        rating_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "index-overallRating")
            )
        )

        print("\nFOUND RATING TEXT:")
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
        print("\nRATING EXTRACTION FAILED:", e)
        return "No Rating", "No Rating"