########################################################
########        Duplicate File Remover             ########
########        Author : Saurabh Y Girme         ########
########        Date : November 12 2022         ########
######################################################## 

from sys import *
import os
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    
    iCnt = 0
    
    if len(results) > 0:
        for result in results:
            for subresult in result:
                iCnt += 1
                
                if iCnt >= 2:
                    os.remove(subresult)
            iCnt = 0

    else:
        print("No duplicate files found")

def hashfile(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)
    
    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()
    
    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    dups = {}
    
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is :" +dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
                    
        return dups

    else:
        print("Invalid Path")

def PrintResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    
    if len(results) > 0:
        print("Duplicates found : ")
        print("The following files are duplicate")
                
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)

    else:
        print("No duplicate files found")

def main():
    print("---------Marvelllous Infosystems by Piyush Khairnar---------")

    print("Application Name : " +argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and print duplicate files' name")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = FindDuplicate(argv[1])
        PrintResults(arr)
        DeleteFiles(arr)
        endTime = time.time()
        
        print("Took %s seconds to evaluate "% (endTime - startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input ",E)

if __name__ == "__main__":
	main()