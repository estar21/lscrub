from helpers import DFHelper

df_helper = DFHelper("Starhub", "./")

df_helper.log({"file_name": "something.txt", "line_number": 5, "line_content": "x,y,z"})

checksum = df_helper.md5("./Logging.py")