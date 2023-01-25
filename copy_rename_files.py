#A Python script to rename and copy files to another folder. Script will read a CSV file called file_list.csv and it will batch process.
#In file_list.csv list all new file names in the first column, and old file names in the second column.
#Indicate below your files source folder and files target folder paths.

#Import libraries
import shutil
import csv

title_lst=[]
guid_lst=[]

try:
    #Define here your source and target folders paths
    source = "C:\\Doc\\img_folder1\\"  #Replace here - Your source folder path where files will be copied and renamed from
    target = "C:\\Doc\\img_folder2\\"  #Replace here - Your target folder path where files will be copied and renamed to
    input_csv_file = "file_list.csv"
        
    # read input data
    file_in = open(input_csv_file, encoding="utf8")
    with file_in as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            #remove illigal char from file names
            for row in csvReader:
                uTitle=''
                for x in row[0]:
                    if ord(x)<128:
                        uTitle= uTitle + x
                uTitle=uTitle.replace(":","-") 
                uTitle=uTitle.replace(".","-")
                uTitle=uTitle.replace("#","")
                uTitle=uTitle.replace("$","")
                title_lst.append(uTitle)
                guid_lst.append(row[1]) 
                
                
    file_in.close()

    # start copying and renaming files

    for i in range(len(title_lst)):
        uTitle = ""
        guID = ""
        uTitle = title_lst[i].lower().replace(" ","-") + ".jpg" #replace "jpg" with any other extension or remove it and scpecify extensions in file_list.csv
        guID = guid_lst[i].replace("'","") + ".jpg" #replace "jpg" with any other extension or remove it and scpecify extensions in file_list.csv

        print(uTitle)
        print(guID)
        source_temp=""
        target_temp=""
        source_temp = source + guID
        target_temp = target + uTitle

        #print(source_temp)
        #print(target_temp)
        shutil.copy(source_temp, target_temp)

except:
    print(source)
    print(target)
    print("\n error at row: ", i)    
