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
eval "cp .bash_aliases ~/" 
eval "cp .bash_profile ~/"
install "firacode" "sudo apt install fonts-firacode"
install "vim" "sudo apt install vim"
install "curl" "sudo apt install curl"
install "okular" "sudo apt install okular"
install "gnome-tweaks" "sudo add-apt-repository universe && sudo apt install gnome-tweaks"
install "gnome-extensions" "sudo apt install gnome-shell-extensions"
install "bash-it" "git clone --depth=1 https://github.com/Bash-it/bash-it.git
~/.bash_it && cp custom.aliases.bash ~/.bash_it/aliases/ && cd ~/.bash_it/install.sh &&"
install "starship" "curl -sS https://starship.rs/install.sh | sh && cp .config/starship.toml ~/.config/"
install "gogh" "git clone https://github.com/Gogh-Co/Gogh.git ~/.gogh"
install "tmux" "sudo apt install tmux && mv .tmux.conf ~/"
install "ctags" "sudo apt install universal-ctags"
install "pip" "sudo apt install python3-pip"
install "latex" "sudo apt install texlive"
install "latex_pt-br" "sudo apt install texlive-lang-portuguese"


