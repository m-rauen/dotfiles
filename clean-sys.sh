echo "Start cleaning system...\n"

sudo apt autoremove --purge 
sudo apt clean 
sudo apt autoclean 
sudo journalctl --vacuum-time=3d 

sudo rm -rfv ~/.cache/thumbnails/
sudo rm -rfv ~/.local/share/Trash/* 

flatpak uninstall --unused 

echo "Everything clean!"
echo "Enjoy it! :)"


