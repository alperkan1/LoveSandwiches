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
    print("please enter the sales figures from the last maket day")
    print("Data should have 6 numbers , seperated with commas.")
    print("example: 10, 12, 30, 40, 50, 60\n")
    data_str = input("Enter your data here: ")
    print(f"The data provided is{data_str}")
get_sales_data() 