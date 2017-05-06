To implement:
set POD.jpg to the Desktop Wallpaper
Modify BackgroundBash to try and run InternetScraperThing.py in the directory you placed it in
copy BackgroundBash to /etc/network/if-up.d/ so that it runs when internet connection is established
   from dir BackgroundBash 
   sudo cp BackgroundBash /etc/network/if-up.d/
Allow BackgroundBash to be run
   from /etc/network/if-up.d/
   sudo chmod +x BackgroundBash

now restart and it should work perfectly!