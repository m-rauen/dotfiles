#!/bin/sh

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

install "vim" "sudo apt install vim"
install "git" "sudo apt install git"
install "curl" "sudo apt install curl"
install "okular" "sudo apt install okular"
install "gnome-tweaks" "sudo add-apt-repository universe && sudo apt
#install gnome-tweaks"
install "gnome-extensions" "sudo apt install gnome-shell-extensions"
install "bash-it" "git clone --depth=1 https://github.com/Bash-it/bash-it.git
#~/.bash_it && cd ~/.bash_it/install.sh"
install "starship" "curl -sS https://starship.rs/install.sh | sh"
install "gogh" "git clone https://github.com/Gogh-Co/Gogh.git ~/.gogh"
install "tmux" "sudo apt install tmux"
install "ctags" "sudo apt install universal-ctags"




