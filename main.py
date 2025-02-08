import numpy as np
from tavily import TavilyClient
import pandas as pd
import os
import json

def identifyInstitution(institution: str, inst_dict: dict):
    """Assign to a institution (key) in the dictionary whether it is public or private (value).

    Args:
        institution (str): the name of the current institution
        inst_dict (dict): the dictionary containing the institutions' sector

    Returns:
        dict: the updated dict containing the institutions' sector
    """
    client = TavilyClient(api_key = "your TAVILY API key")
    
    # A Q&A need only to know one word of the answer, so this is teh appropiate request to make.
    result = client.qna_search(
        query=f"Is {institution} public or private?"
    )
    
    # If the word public is in the answer, then the institution is public (though exceptions might pop up)
    if "public" in result:
        inst_dict[institution] = "public"
    # If the word private is in the answer, then the institution must be private
    elif "private" in result:
        inst_dict[institution] = "private"
    # If neither word comes out, then the institution is unidentified
    else:
        inst_dict[institution] = "N/A"
    
    # Returned the updated dictionary
    return inst_dict
    
def main():
    # Create a Pandas DF to store the Nature Index's share for each kind of institutions
    columns = ["private", "public"]
    index = [i for i in range(2015, 2024)]
    ret_df = pd.DataFrame(columns=columns, index=index)
    ret_df.fillna(0, inplace=True)      # This is needed to do += below
    
    if os.path.exists("inst_dict.json"):
        # If an institution dictionary already exists, load it
        with open("inst_dict.json", "r") as infile:
            main_dict = json.load(infile)
    else:
        # Else, create  dictionary to store whether each institution is public or private
        main_dict = {}
    
    try:
        year = 2015         # the Dataset begins at this year
        # Process all the file in the directory. Sorted the list in order to process chronologically.
        #  Each iteration of the loop accounts for a year
        for name in sorted(os.listdir("CSV_Academia")):
            current_df = pd.read_csv(f"CSV_Academia/{name}")
            current_df = current_df.set_index("Institution")    # Easier to process with institution as index.
            for institution in current_df.index:
                if institution == "Tecnológico de Monterrey, Mexico":       # My Alma Mater :)
                    print(":)")
                # The program takes long to finish, needed a way to see everything is going smooth
                print(f"{year}: Checking {institution}")
                if institution not in main_dict:        # Self-explinatory
                    main_dict = identifyInstitution(institution, main_dict)
                status = main_dict[institution]     # status: whether it is private, public or unidentified
                if status != "N/A":     # If it is not unidentified
                    # Add the institution share to its corresponding kind and year
                    ret_df.loc[year, status] += current_df.loc[institution, f"Share {year}"]
            year += 1   # increase a year once a CSV file is processed

        print(ret_df)                       # Print the Dataframe
        ret_df.to_csv("Ret_df.csv")         # Save the Dataframe to a CSV
        
        # Save institutions dictionary into a JSON file
        with open("inst_dict.json", "w") as outfile:
            outfile.write(main_dict)
    
    # If anything bad happens (like running out of TAVILY credits all of the progress is printed & saved)
    except:
        print(ret_df)                       # Print the Dataframe
        ret_df.to_csv("Ret_df.csv")         # Save the Dataframe to a CSV
        
        # Save institutions dictionary into a JSON file
        with open("inst_dict.json", "w") as outfile:
            json.dump(main_dict, outfile)

# Run the program
if "__main__" == __name__:
    main()