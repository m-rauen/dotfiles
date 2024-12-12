syntax on

"map I :! pdflatex %<CR><CR> 
"map S :! mupdf-x11 $(echo % \| sed 's/tex$/pdf/') & disown<CR><CR>

set spelllang=en_us,pt_br
set paste
set ignorecase
set smartcase
set clipboard+=unnamedplus  "if 'unnamedplus' doesnt work, try 'unnamed'"
set noerrorbells
set encoding=utf8
set keymap=accents
set tabstop=4 softtabstop=4     
set shiftwidth=4
set expandtab
set smartindent
set nocompatible
set wrap
set hlsearch
set linebreak
set tw=80
set smartcase
set incsearch
set nu
set relativenumber
set noswapfile

set colorcolumn=80
highlight ColorColumn ctermbg=0 guibg=lightgrey

"---

call plug#begin('~/.vim/plugged')

" Vim Stuff
Plug 'tpope/vim-fugitive'
Plug 'romainl/vim-cool'
Plug 'vim-utils/vim-man'
Plug 'ervandew/supertab'
Plug 'raimondi/delimitmate'
Plug 'majutsushi/tagbar'
Plug 'tpope/vim-surround'
Plug 'jiangmiao/auto-pairs'
Plug 'honza/vim-snippets'
Plug 'jayli/vim-easycomplete'
"Plug 'sirver/ultisnips'
Plug 'itchyny/lightline.vim'

" Markdown Stuff
Plug 'gabrielelana/vim-markdown'

" LaTeX Stuff
Plug 'vim-latex/vim-latex'
Plug 'xuhdev/vim-latex-live-preview'
Plug 'vim-scripts/matchit.zip'
Plug 'lervag/vimtex'
Plug 'poppyschmo/deoplete-latex'
Plug 'pietropate/vim-tex-conceal'

" Programming Stuff
Plug 'rkulla/pydiction'
Plug 'vim-scripts/taglist.vim'
Plug 'yggdroot/indentline'

" Themes Stuff
Plug 'morhetz/gruvbox'
Plug 'ghifarit53/tokyonight-vim'
Plug 'nlknguyen/papercolor-theme'
Plug 'junegunn/seoul256.vim'

call plug#end()

"--- 

colorscheme tokyonight
set background=dark

"--- 

if executable('rg')
    let g:rg_derive_root='true'
endif

" Tokyonight Configs
let g:tokyonight_style = 'storm' " available: night, storm
let g:tokyonight_enable_italic = 1

" Vim-Cool Configs
let g:cool_total_matches = 1

" Vim-Tex-Conceal Configs
set conceallevel=1
let g:tex_conceal='abdmg'
hi Conceal ctermbg=none

" Lightline Configs
let g:lightline = {
      \ 'colorscheme': 'powerline',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'readonly', 'filename', 'modified', 'msg' ] ]
      \ },
      \ 'component': {
      \   'msg': 'Keep Grinding'
      \ },
      \ }

set laststatus=2
