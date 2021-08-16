source $HOME/.config/nvim/vim-plug/plugins.vim
source $HOME/.config/nvim/airline_setup.vim
source $HOME/.config/nvim/key_remaps.vim
source $HOME/.config/nvim/dashboard_config.vim
source $HOME/.config/nvim/coc_config.vim
source $HOME/.config/nvim/nvimtree_config.vim

set nowrap
set hlsearch
set showmatch
set ruler
set updatetime=100
set ignorecase
set smartcase
set incsearch
set noerrorbells visualbell t_vb= "turn off the annoying default linux error bell sound
set mouse+=a "add basic mouse support, for convenience
set number relativenumber
set showcmd
set splitbelow splitright
au ColorScheme * hi Normal ctermbg=none guibg=none
au ColorScheme myspecialcolors hi Normal ctermbg=red guibg=red

set bg=dark

let g:indentLine_showFirstIndentLevel = 1

if (has("termguicolors"))
 set termguicolors
endif

" Theme
syntax enable
colorscheme dracula


