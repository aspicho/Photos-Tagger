# Photos-Tagger
Simple program which helps manualy classify photos using custom tags.

## Features
- Support multiple folders marking
- Support searh in files while marking
- Allows to have specific tags for each folder
- Allows adding brand new tags while marking
- Allows adding/removing files in working folder in while marking
# How to use
After launching add your folder by clicking "Add New", then editor window will appear, in it I firstly recomend add your tags in setting tab.
By default there will be two tags "Example" and "Example2", you can delete them without any troubles. Just don't forget to save settings before leaving tab!
In main tab you can see list of files in current folder at right side, you can click on each file in that lsit to choose it for editing. Above it located search bar, at the bottom of window located control panel, where you can add or remove tags for photo, scroll through list of files, save result, or load data if data-file were modified in some other way while editor was open. In controll panel you also can see name and index of current photo.
If you removed or added file in folder while editor was open, you can update list of files in settings tab.
Result of marking stored in file data.json which stored in subfolder Resources in folder you marking

# Known Issues
If delete last or first file in list while it open, change of photo will rise List Index Out of Range exception