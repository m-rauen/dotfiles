#!/bin/sh

#TODO: modify 'starship' installation source
#TODO: add VSCode installation and settings 
#TODO: add Google Chrome installation and settings

command_already_exists() {
    packg=$1
    echo "\nSuccess!"
    echo "Package "\'$packg\'" already installed in your system!"
    echo "[...]\n"
}

install(){
    package=$1
    code=$2
    if ! command -v "$package" > /dev/null 2>&1; then
        echo ""\'$package\'" not found!"
        echo "Starting "\'$package\'" installation...\n"
        eval "$code"
    else 
        command_already_exists $package
    fi
}

eval "cp .bash_aliases ~/" 
eval "cp .bash_profile ~/"
eval "cp pip-upgd-all.py ~/"
eval "cp hartree-to-kcal.py ~/"
eval "cp user-dirs.dirs ~/.config"
install "nerd-fonts" "git clone --depth 1
https://github.com/ryanoasis/nerd-fonts.git ~/.nerd-fonts"
eval "cd ~/.nerd-fonts"
install "vim" "sudo apt install vim"
install "curl" "sudo apt install curl"
install "okular" "sudo apt install okular"
eval "sudo add-apt-repository universe"
install "gnome-tweaks" "sudo apt install gnome-tweaks"
install "gnome-extensions" "sudo apt install gnome-shell-extensions"
install "bash-it" "git clone --depth=1 https://github.com/Bash-it/bash-it.git
~/.bash_it" 
install "starship" "curl -sS https://starship.rs/install.sh | sh" 
install "gogh" "git clone https://github.com/Gogh-Co/Gogh.git ~/.gogh"
install "tmux" "sudo apt install tmux" 
install "ctags" "sudo apt install universal-ctags"
install "pip" "sudo apt install python3-pip"
eval "cd ~/.nerd-fonts && ./install.sh"
eval "cp .config/starship.toml ~/.config/"
eval "cp .tmux.conf ~/"


