syntax on

map P :! pdflatex %<CR><CR> 
map S :! mupdf-x11 $(echo % \| sed 's/tex$/pdf/') & disown<CR><CR>

set spell
set spelllang=pt_br
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
set linebreak
set tw=80
set smartcase
set incsearch
set nu
set noswapfile

set colorcolumn=80
highlight ColorColumn ctermbg=0 guibg=lightgrey

" -------------------------------
call plug#begin('~/.vim/plugged')


" Vim Stuff
Plug 'tpope/vim-fugitive'
Plug 'vim-utils/vim-man'
Plug 'ervandew/supertab'
Plug 'raimondi/delimitmate'
Plug 'majutsushi/tagbar'
Plug 'tpope/vim-surround'
Plug 'jiangmiao/auto-pairs'
Plug 'honza/vim-snippets'
Plug 'jayli/vim-easycomplete'
Plug 'sirver/ultisnips'
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

call plug#end()
" -------------------------------


colorscheme gruvbox
set background=dark


if executable('rg')
    let g:rg_derive_root='true'
endif

" LaTeX Live Preview Configs
" let g:livepreview_previewer = 'okular'
let g:livepreview_engine = 'pdflatex'
let g:livepreview_cursorhold_recompile = 0

" Vim-Tex Configs
let g:tex_flavor='latex'
let g:vimtex_view_method='zathura'
let g:vimtex_quickfix_mode=1

" Vim-Tex-Conceal Configs
set conceallevel=1
let g:tex_conceal='abdmg'
hi Conceal ctermbg=none

" UltiSnips Configs
let g:UltiSnipsExpandTrigger = "<tab>"
let g:UltiSnipsJumpForwardTrigger = "<c-tab>"
let g:UltiSnipsJumpBackwardTrigger = "<s-tab>"
let g:UltiSnipsSnippetsDir="~/.vim/plugged/vim-snippets/UltiSnips"
let g:UltiSnipsSnippetDirectory=['UltiSnips']

" Lightline Configs 
let g:lightline = {
      \ 'colorscheme': 'powerline',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'readonly', 'filename', 'modified', 'msg' ] ]
      \ },
      \ 'component': {
      \   'msg': 'Go on!'
      \ },
      \ }

set laststatus=2

" EasyComplete Configs
let g:easycomplete_tab_trigger="<c-space>"
let g:easycomplete_diagnostics_enable = 0
let g:easycomplete_scheme="dark"
nnoremap <silent> <C-j> :EasyCompleteNextDiagnostic<CR>
nnoremap <silent> <C-k> :EasyCompletePreviousDiagnostic<CR>

