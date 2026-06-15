# Daily Desktop Wallpaper

A desktop wallpaper manager that uses daily downloaded images from services like NASA's Astronomy Picture of the Day *(APOD)*.


## Requirements:
- Python 3.10+
  
All required modules are placed in the [`requirements.txt`](requirements.txt) file.

## Font License
This project uses [Chivo Mono](data/fonts/ChivoMono/ChivoMono-Light.ttf) by [Omnibus-Type](https://www.omnibus-type.com), licensed under [SIL Open Font License Version 1.1](https://openfontlicense.org/open-font-license-official-text/).

## Currently tested and works on:
- Windows 11
- Linux: *runs with `daimg.sh` file*
  - Gnome (Debian tested)

Other Windows versions and OSes are not guaranteed to support this project.

## Usage:
### Start up
The program is run by launching the [`daimg.py`](daimg.py) file.

At launch, the program checks for and creates:
1. file `history.csv` 
2. file `config.json`
3. path `data/errors_hangout`
4. file `.errors_info.json`
5. path `images`
> These are personalised along with the use of the program, so they are not added to the repository.

*Then comes the integrity check.* **Not implemented yet**

### Running the program
First, it looks for the API key for APOD in the`data/.env` file. If not found, it asks for it, checks it, and asks to save it locally.

Then comes the process of downloading the image and setting it as the desktop wallpaper.


## Services provided now:
1. NASA's APOD (Astronomy Picture of the Day) with provided API key


## Features and improvements:

### Needs a fix:
- Currently program doesn't (re)check if the new image is being set. That means if at the moment when the program is run today's image is already downloaded, the program will not download it again BUT it won't set it as a wallpaper either if it's not for some reason.

### Planned:
- Create a software interface for this program for the user, where the program settings can be changed. The following settings are planned to be controlled:
  - Run the algorithm on startup to work in the background.
  - Automatic setting of the downloaded image.
  - An option to choose a **custom folder** where images will be downloaded to.
    > Thus, the user might use the slideshow option, especially with a custom folder, adding their images into it.

- Add a photo editing process, where:
  - The image is put on a dark background, so the whole image can be seen, shifted to the side.
  - On the empty space of other side is a description of this image.
    > All done with aesthetic proportions.
     The **informatical format** editing is saved as an image. Other versions of editing are planned to be added to choose from.  

- Make the program with a GUI interface.
- Obviously, provide more services.

### Implemented:
- On click, check for available and usable image, download it in the highest resolution, and set it as a desktop wallpaper.

    Every image is stored in a folder named `images` in the project's directory. *This folder is created with the first run of the program.*


## Error handling
Every error report is saved in the `data/errors_hangout` folder. For private contact about any program problems, use my contacts.


## Contacts

> Telegram: [d13samoylyuk](https://t.me/d13samoylyuk)

> Email: sam.daniil13@gmail.com