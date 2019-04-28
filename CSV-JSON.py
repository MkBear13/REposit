from context_manager import ContextManager

class Convector():

def __init__(self):
        self.csv_file = None
        self.json_file = None

with ContextManager(self.csv_file, 'r') as open_file:
          csvfile = str(open_file.read()) 

def process(self.csv_file, self.json_file):
  arr=[]
  headers = []
  for header in csvfile.readline().split(','):
    headers.append(header)
  for line in csvfile.readlines():  
  lineStr = ''
  for i,item in enumerate(line.split(',')):
    if i < len(csvfile): 
        lineStr+='"'+headers[i] +'" : "' + item + '",\n'
  arr.append(lineStr)
  jsn = '{\n "entries":['
  jsnEnd = ']\n}'
    for i in range(len(arr)-1):
    if i == len(arr)-2:
        jsn+="{"+str(arr[i])[:-2]+"}\n" 
    else:
        jsn+="{"+str(arr[i])[:-2]+"},\n" 
      jsn+=jsnEnd
  with ContextManager(self.json_file, 'a') as open_file:
     open_file.write( str(leap(jsn))

if __name__ == "__main__":
    convert = Convector()
    convert.filename = input("enter name of .csv file ")
    convert.jsonfile = input("enter name of .json file ")
    arr = convert.reader()
    convert.write_to_json(arr)