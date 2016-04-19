import sys
import datetime
import photonz_toolkit as ptk


def add():
  pass


def status():
   pass


def info():
   print("Version: " + ptk.get_version())
   print("Content Home: " + ptk.get_content_home())
   print("Manifest file: " + ptk.__manifest_file_name__)
   print("Install date: " + str(datetime.datetime.now())) 

def main():
   arg = sys.argv[1]
   print(arg)
   if arg == 'info':
      info()
   else:
      pass   

if __name__ == '__main__':
   main()




