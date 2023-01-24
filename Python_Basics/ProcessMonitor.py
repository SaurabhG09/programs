import psutil

def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("Marvellous Infosystems : Python Automation and Machine Learning")
    
    print("Process Monitor")
    
    listprocess = ProcessDisplay()
    
    for elements in listprocess:
        print(elements)
        
if __name__ == "__main__":
    main()