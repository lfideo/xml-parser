# xml-parser
This script makes it possible to parse xml feeds and return a dataframe - it includes the following steps:
1) with the help of the `requests library`, I'm able to connect to a web page
2) then I use `json` and `xmltodict` libraries to transform `collections.OrderedDict` object into a dictionary
3) after that I construct a list by looping through dictionary keys to get the information I need
4) when the list is ready, I use `pd.sjon_normalize` to create a dataframe
5) then the dataframe is sent to Google Spreadsheets via the `df2gspread` library
