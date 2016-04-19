# management tools

- place the manage  application directory in a directory level with the master content directory
- ensure that the content directory is named content, and had child folders, img, vid, and gif
- if the above structure is not available then modify where needed
- a config.json file should be created with the following information in json format:
{"manifest":"manifest.json","items_total":"540","subdirs":["img","vid","gif"],"last_access":"03-31-16"}
- a manifest.json file can be generated if one does not exist


## todo:
- fix the backup of the manifest naming convention
- decide if the manifest file name is stored in config or in the script
- continually generate pydoc
- seperate the presentation from the tools aspects of the application
- add functionality to check the consistency of the content against the manifest
- build search functionality up
- build display functionality
- version control
- add the content_root_path to the config file
- format the install date in photonz
- create accessor for manifest file name in toolkit for use in photonz.py info() 


## Use:
$ python photonz.py info

Version: Photonz 1.0
Content Home: /vmstore/photonz/photonz_complete_backup_2016
Manifest file: /vmstore/photonz/photonz_complete_backup_2016/app/manifest.json
Install date: 18-Mar-2016

Content:
	img:	818
	vid:	134
	gif:	32

$ python photonz.py status

photonz status:

The following items have not been added to the manifest:
	snark.jpg
	DCS5489_08122006.jpg

$ python photonz.py add

Added /vmstore/photonz/photonz_backup_2016/content/img/snark.jpg to manifest.
Added /vmstore/photonz/photonz_backup_2016/content/img/DCS5489_08122006.jpg to manifest.



