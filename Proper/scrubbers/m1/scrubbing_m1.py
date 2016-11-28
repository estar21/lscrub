import os, string, datetime

def validateTelco2(telco, fn_input, fn_output):
    finput = open(fn_input,"rb")
    lines = finput.readlines()
    
    foutput = open(fn_output,"wb")
    foutput.write(lines[0]) ## copy column names to output file
    
    for line in lines[1:]:
        cols = line.replace("\r\n","").split("|")
        
        if len(cols) != telco["num_col"]: ## check expected no. of cols
            continue
        
        try:
            datetime.datetime.strptime(cols[0],telco["0"]["allowed"])
        except ValueError:
            continue
        
        if not set(cols[1]).issubset(telco["1"]["allowed"]) or len(cols[1]) > telco["1"]["maxlength"]:
            continue
        
        try:
            aa = float(cols[2])
            if aa not in telco["2"]["allowed"]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[4])
            if aa < telco["4"]["allowed"][0] or aa > telco["4"]["allowed"][1]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[5])
            if aa < telco["5"]["allowed"][0] or aa > telco["5"]["allowed"][1]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[6])
            if aa not in telco["6"]["allowed"]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[7])
            if aa not in telco["7"]["allowed"]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[8])
            if aa not in telco["8"]["allowed"]:
                continue
        except ValueError:
            continue
        
        if cols[9] not in telco["9"]["allowed"]:
            continue
        
        foutput.write(line) ## write row to output file if satisfied criteria

    finput.close()
    foutput.close()


def validateTelco2_2017(telco, fn_input, fn_output):
    finput = open(fn_input,"rb")
    lines = finput.readlines()
    
    foutput = open(fn_output,"wb")
    foutput.write(lines[0])
    
    for line in lines[1:]:
        cols = line.replace("\r\n","").split("|")
        
        if len(cols) != telco["num_col"]: ## check expected no. of cols
            continue
        
        try:
            datetime.datetime.strptime(cols[0],telco["0"]["allowed"])
        except ValueError:
            continue
        
        if not set(cols[1]).issubset(telco["1"]["allowed"]) or len(cols[1]) > telco["1"]["maxlength"]:
            continue
        
        try:
            aa = float(cols[2])
            if aa < telco["2"]["allowed"][0] or aa > telco["2"]["allowed"][1]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[3])
            if aa < telco["3"]["allowed"][0] or aa > telco["3"]["allowed"][1]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[4])
            if aa not in telco["4"]["allowed"]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[5])
            if aa not in telco["5"]["allowed"]:
                continue
        except ValueError:
            continue
        
        try:
            aa = float(cols[6])
            if aa not in telco["6"]["allowed"]:
                continue
        except ValueError:
            continue
        
        if cols[7] not in telco["7"]["allowed"]:
            continue
        
        foutput.write(line)

    finput.close()
    foutput.close()



if __name__ == "__main__":

    #Note: I skip CGI, not checking it
    Telco2 = {"num_col" : 10, 
              "0": {"allowed": "%Y-%m-%d %H:%M:%S.%f"}, #TIMESTAMP
              "1": {"allowed": set(string.ascii_uppercase + string.digits), "maxlength": 32}, #TOKEN
              "2": {"allowed": [2,3]}, #NETWORK
              "4": {"allowed": (-90.0,90.0)}, #LATITUDE
              "5": {"allowed": (-180.0,180.0)}, #LONGITUDE
              "6": {"allowed": range(0,100)}, #EVENT
              "7": {"allowed": range(100,1000)}, #MCC
              "8": {"allowed": range(10,1000)}, #MNC
              "9": {"allowed": ["INDOOR","OUTDOOR"]} #SITE_TYPE
              }
    
    Telco2_2017 = {"num_col" : 8, 
                   "0": {"allowed": "%Y-%m-%d %H:%M:%S"}, #TIMESTAMP
                   "1": {"allowed": set(string.ascii_uppercase + string.digits), "maxlength": 32}, #USERID
                   "2": {"allowed": (-90.0,90.0)}, #LATITUDE
                   "3": {"allowed": (-180.0,180.0)}, #LONGITUDE
                   "4": {"allowed": range(0,4)}, #TRAFFIC
                   "5": {"allowed": range(100,1000)}, #MCC
                   "6": {"allowed": range(10,1000)}, #MNC
                   "7": {"allowed": ["INDOOR","OUTDOOR"]} #SITE_TYPE
                   }
              
    folderpath = "/media/kokmeng/Backup Data/M1data/160630/"
    for filename in os.listdir(folderpath):
        fn_input = folderpath + filename
        n = os.path.splitext(filename)
        fn_output = folderpath + n[0] + '_a' + n[1] ## rename output file
        validateTelco2(Telco2, fn_input, fn_output)






#        # 1st col
#        if ((set(cols[0]).issubset(telco["0"]["allowed"])) and (len(cols[0]) == telco["0"]["length"])) == False:
#            lines.remove(line)
#        # 2nd col
#        if ((datetime.datetime.strptime(cols[0],telco["0"]["allowed"])) and (len(cols[1]) == telco["1"]["length"])) == False:
#            lines.remove(line)
#        # 3rd col
#        if ((set(cols[2]).issubset(string.digits)) and (int(cols[2]) in telco["2"]["allowed"]) and (len(cols[2]) in telco["2"]["length"])) == False:
#            lines.remove(line)
#        # 4th col
#        if ((set(cols[3]).issubset(string.digits)) and (int(cols[3]) in telco["3"]["allowed"]) and (len(cols[2]) in telco["3"]["length"])) == False:
#            lines.remove(line)
#

#def validateTelco2(telco): # returns only lines that are valid.
#    folderpath = telco["folderpath"]
#    for filename in os.listdir(folderpath):
#        fo = open(folderpath + "\\" + filename, "rb")
#        lines = fo.readlines()
#        for line in lines:
#            line_clean = line.replace("\n","")
#            cols = line_clean.split(",")
#            # check expected no. of cols
#            if len(cols) != telco["num_col"]:
#                lines.remove(line)
#            # 1st col
#            if ((set(cols[0]).issubset(telco["0"]["allowed"])) and (len(cols[0]) == telco["0"]["length"])) == False:
#                lines.remove(line)
#            # 2nd col
#            if ((datetime.datetime.strptime(cols[1],telco["1"]["allowed"])) and (len(cols[1]) == telco["1"]["length"])) == False:
#                lines.remove(line)
#            # 3rd col
#            if ((set(cols[2]).issubset(string.digits)) and (int(cols[2]) in telco["2"]["allowed"]) and (len(cols[2]) in telco["2"]["length"])) == False:
#                lines.remove(line)
#            # 4th col
#            if ((set(cols[3]).issubset(string.digits)) and (int(cols[3]) in telco["3"]["allowed"]) and (len(cols[2]) in telco["3"]["length"])) == False:
#                lines.remove(line)                
#    return lines
#
#
#valid_lines = validateTelco2(Telco_2)
#for line in valid_lines:
#    # write the line somewhere
#
#
#f = open('myfile','w')
#f.write('hi there\n') # python will convert \n to os.linesep
#f.close() # you can omit in most cases as the destructor will call it

