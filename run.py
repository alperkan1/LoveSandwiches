import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CRED = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CRED.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')
def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:

        print("please enter the sales figures from the last maket day")
        print("Data should have 6 numbers , seperated with commas.")
        print("example: 10, 12, 30, 40, 50, 60\n")
        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")
        validate_data(sales_data)

        if validate_data(sales_data):
            print("data is valid")
            break

def validate_data(values):
    """
    inside the try converts all strins values into intergers .
    Raise the Value error if the strings cannot be converted into a int or if there isnt 6 values.
    """
    try: 
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"expected 6 values required , you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again/n")
        return False
    return True
data = get_sales_data() 
