import json
from pprint import pprint
import os
import sys

import search
import photonz_toolkit as tk

###############################################################################################
def print_open():
   ''' print the startup screen info with config '''
   print("\n\nCromaca Cli " + tk.get_version())
   print


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
def validate_env(dirs):
   print("   Checking structure...")
   if(structure_check(dirs)):
      print("   Structure ok")
   else:
      print("   *** ERROR: Structure of content home is broken: " + root)
      sys.exit(1)


###############################################################################################
def getpct(total, part):
   pct = 0.0
   pct = float(part)/total
   return pct*100

###############################################################################################
def print_branch_counts(branches):
   for a in branches:
      print("   " + a + "   "  + str(get_branch_item_count(a)) )

###############################################################################################
def main():
   configuration = tk.get_config('config.json')
   home = tk.get_content_home()
   folder_list = configuration['subdirs']
   search_paths = tk.build_search_paths(home, folder_list)
   # THIS WORKS tk.generate_manifest(search_paths)
   manifest = tk.load_manifest()
   pprint(manifest)
   '''
   search_paths = build_search_paths(__content_home__, folder_list)
   last_total = configuration['items_total']
   print_content_file_list(search_paths)
   validate_env(search_paths)
   print("   Getting content totals....")
   print_branch_counts(search_paths)
   current_total = get_total_content_count(__content_home__, folder_list)
   print("   Total Items in content: " + str(get_total_content_count(__content_home__, folder_list)))
   if current_total != last_total:
      print("\n   *** WARNING: Total number of items has changed from " +
            str(last_total) + " to " + str(current_total) +
            " since last run.")

   if search.search(__content_home__ + '/gif', 'topoff2.gif'):
      print "Search works"
   '''
   pass

###############################################################################################
if __name__ == '__main__':
        main()

