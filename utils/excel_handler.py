import os
import pandas as pd


def read_input_excel(file_path):

    try:
        df = pd.read_excel(file_path)

        print("Excel file loaded successfully!")

        return df

    except Exception as e:

        print(f"Error reading Excel: {e}")

        return None


def save_output_excel(results):

    output_df = pd.DataFrame(results)

    os.makedirs("output", exist_ok=True)

    output_file = "output/ProductRatings.xlsx"

    output_df.to_excel(output_file, index=False)

    print("\nReport generated successfully!")
    print(f"Saved at: {output_file}")

    return output_file