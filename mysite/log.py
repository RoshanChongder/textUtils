import os
def writeLog(path, content, m ):
    print(os.getcwd() )

    file = open(path, m)
    try :
        file.write(content)
    except Exception:
        print('Some error while writing log')
    finally:
        file.close()
