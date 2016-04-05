import json
import os
import sys
import hashlib
import datetime
# import search

__version__ = '0.1'
__config_file__  = 'config.json'
__manifest_file_name__ = 'manifiest.json'
__content_home__ =os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'content'))
__description__ = ''' This is the photonz api interface for working with a stucture indicated
                      in the config.json file '''

###############################################################################################
def get_version():
   ''' Return application version '''
   return __version__

###############################################################################################
def get_config_file_name():
   ''' Return the filename of the config file that is being used '''
   return __config_file__

###############################################################################################
def get_content_home():
   ''' Return the path to the root content location '''
   return __content_home__


###############################################################################################
def HashCalc(fpath):
   ''' Return the 32 character md5 hash of the object at fpath '''
   try:
      f = file(fpath,'rb')
      Data =f.read()
      MD5 = hashlib.md5(Data).hexdigest()
   except:
      sys.exit()
   f.close()
   return MD5

###############################################################################################
def generate_manifest(file_locations, manifest_path="."):
   ''' Create a manifest file that contains the dictionary of hashes and filenames
       that is currently being used by the application. If one already exists it
       is backed up prior to a new manifest being created. ** WARNING: ** this
       is a destructive change despite there being a backup provided! '''
   # TODO: Clean this timestamp up
   #now = datetime.datetime.now()
   now = ".bak"
   manifest_file_name = __manifest_file_name__
   if os.path.exists(manifest_path + manifest_file_name):
      os.rename(manifest_path + manifest_file_name, manifest_path + manifest_file_name + now)
   D = {}
   with open(manifest_path + '/' + manifest_file_name, 'w') as fout:
      for directory in file_locations:
         for filename in os.listdir(directory):
            fhash = HashCalc(directory + "/" + filename)
            D[fhash] = directory + "/" + filename
      json.dump(D, fout)


###############################################################################################
def load_manifest(path="."):
   ''' Return a dictionary that contains the json contents from the manifest file '''
   with open(path + '/' + __manifest_file_name__) as fin:
       data = json.load(fin)
   return data

###############################################################################################
def save_manifest(modified_manifest, manifest_path="."):
   ''' Write the json data to the manifest file. This is a safe write as the old manifest
       file is preserved with a backup. '''
   # TODO: fix the backup method
   now = '.bak'
   os.rename(manifest_path + manifest_file_name, manifest_path + manifest_file_name + now)
   json.dump(modified_manifest, manifest_path + '/' + __manifest_file_name__)

###############################################################################################
def build_search_paths(home_path=__content_home__, subfolders):
   ''' Returns a list of fully qualified paths to all directories that may contain
       content based on a passed common "home_path" and a "subfolders" list object. '''
   paths = []
   for dirx in subfolders:
      paths.append(home_path + '/' + dirx)
   return paths

###############################################################################################
def print_content_file_list(paths):
   ''' A combined continuous listing of all the paths passed  '''
   for folder in paths:
      print_dir_list(folder)

###############################################################################################
def print_dir_list(dirx):
   ''' Outputs a listing similar to ls of the path passed as dirx '''
   k = os.listdir(dirx)
   for x in k:
      print(x)

###############################################################################################
def structure_check(paths):
   ''' Check that each of the paths passed exist. If not return 0 otherwise return 1. '''
   for path in paths:
      if not os.path.exists(path):
         return 0
   return 1

###############################################################################################
def get_config(config_file_path):
   ''' Returns a dictionary of saved config parameters contained in the file indicated by
       config_file_path '''
   try:
      # Reading json data
      with open(config_file_path, 'r') as f:
         data = json.load(f)
   except IOError:
      print('   Configuration not accessible. Check that %s exists and is readable'%(config_file_path))
      sys.exit(1)
   return data

###############################################################################################
def get_branch_item_count(path):
   ''' Return the number of items contained in the directory indicatied by path '''
   return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])


###############################################################################################
def get_total_content_count(path, share_list):
   ''' Return the total number of items in the content tree captured by share_list '''
   total = 0
   for folder in share_list:
      total += get_branch_item_count(path + '/' + folder)
   return total

###############################################################################################
def main():
   ''' Application entry point - just string for info not intended for run '''
   print("Cromaca api version " + __version__)

###############################################################################################
if __name__ == '__main__':
        main()
