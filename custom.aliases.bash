# apt aliases 
alias mkinstall='sudo make install'
alias aptclean='sudo apt clean'
alias aptautorm='sudo apt autoremove'
alias pkgf='dpkg --listfiles'
alias pkgl='dpkg --list'
alias pkglist='dpkg --list'

# tmux aliases 
alias tmx='tmux'
alias tlist='tmux ls' #list sessions 
alias tnew='tmux new-session -s' #start named session 
alias tattach='tmux a -t' #attach to specific session 
alias tdetach='tmux detach' #detach from the current session 
alias tkill='tmux kill-session -t'  #kill session specified 
alias trename='tmux rename-session -t' #rename specific session 
alias tinfo='tmux info' #show every session, window, pane, etc

# vim aliases 
alias vver='vim --version'

#git aliases 
alias gi='git init -b master'
alias ginit='git init -b master'
alias gimain='git init -b main'

alias gadd='git add .'

alias gc='git commit -v -m'

alias gclone='git clone'

alias gmerge='git merge'

alias gpll='git pull'
alias gpull='git pull'
