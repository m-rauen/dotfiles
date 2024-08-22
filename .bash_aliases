#!/bin/bash -i

# lsd aliases 
alias lt='ls --tree'

# system aliases 
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias open="xdg-open 2>/dev/null"
alias po='poweroff'
alias rb='reboot'
alias q='exit'
alias reload='source ~/.bashrc'

# personal aliases 
alias doc='cd ~/Documents'
alias dow='cd ~/Downloads/'
alias pics='cd ~/Pictures/'
alias geemm='cd ~/Documents/GEEMM'
alias rotax='cd ~/Documents/GEEMM/rotaxane-study/'
alias anions='cd ~/Documents/GEEMM/anion-recognition/'
alias ovrrx='cd ~/Documents/GEEMM/overrx/'
alias amino='cd ~/Documents/GEEMM/modified_aminoacid/'
alias repos='cd ~/.repos'

# ssh alias 
alias jupiter='ssh mrauen@jupiter'
alias pcadf='ssh geem@adf'
alias newton='ssh mrauen@newton'
alias loboc='ssh mrauen@lobocarneiro'
alias tarsus='ssh renato@tarsus'

# wine aliases 
alias chemcraft='wine ~/.wine/drive_c/Chemcraft/Chemcraft.exe'
alias cc='wine ~/.wine/drive_c/Chemcraft/Chemcraft.exe '
alias gedit='gabedit '
alias killwine='wineserver -k'
alias zot='/usr/bin/zotero'

# orca aliases
alias orca='~/.orca/orca'
alias orca_plot='~/.orca/orca_plot'
alias orca2mkl='~/.orca/orca_2mkl'

# programs aliases
alias gplot='gnuplot'
alias btop='bashtop'
alias bt='bashtop'
alias avogadro='flatpak run org.openchemistry.Avogadro2'
alias nciplot='~/nciplot/src_nciplot_4.2/nciplot'
alias multiwfn='~/Multiwfn/Multiwfn'
alias mwfn='~/Multiwfn/Multiwfn'
alias molden2aim='~/.molden2aim/molden2aim.exe'

# python3 aliases 
alias pipupgd='python3 ~/.scripts/pip-upgd-all.py'
alias htk='python3 ~/.scripts/hartree-to-kcal.py'
alias mep='python3 ~/.scripts/mep.py'
alias cvb='python3 ~/.scripts/cvb.py'
alias eprep='python3 ~/.scripts/eprep.py'

