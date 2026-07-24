from utils.excel_handler import read_input_excel, save_output_excel
from scraper.browser import open_browser
from scraper.rating_scraper import extract_rating


def main(input_file, progress_bar=None, status_text=None):

    df = read_input_excel(input_file)

    if df is None:
        return None

    driver = open_browser()

    results = []

    total_products = len(df)

    for index, row in df.iterrows():

        # Update Streamlit Progress Bar
        if progress_bar:
            progress = (index + 1) / total_products
            progress_bar.progress(progress)

        # Update Status Text
        if status_text:
            status_text.text(
                f"Processing Product {index + 1} of {total_products}\n"
                f"FG Code: {row['FG CODE']}"
            )

        fg_code = row["FG CODE"]
        myntra_id = row["Myntra ID"]
        link = row["Link"]

        print(f"\nProcessing {index + 1}/{total_products}")

        driver.get(link)

        rating, rating_count = extract_rating(driver, link)

        results.append({
            "FG CODE": fg_code,
            "Myntra ID": myntra_id,
            "Link": link,
            "Rating": rating,
            "Rating Count": rating_count
        })

        print(f"Rating : {rating}")
        print(f"Rating Count : {rating_count}")

    driver.quit()

    output_file = save_output_excel(results)

    return output_file


if __name__ == "__main__":
    input_file = "data/Set4.xlsx"
    main(input_file)