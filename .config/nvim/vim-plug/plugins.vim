" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " File Explorer
    Plug 'kyazdani42/nvim-web-devicons'
    Plug 'kyazdani42/nvim-tree.lua'
    " Surround
    Plug 'tpope/vim-surround'
    " Gruvbox colorscheme
    Plug 'morhetz/gruvbox'
    " Dracula colorscheme
    Plug 'dracula/vim'
    " Airline
    Plug 'bling/vim-airline'
    " Airline themes
    Plug 'vim-airline/vim-airline-themes'
    " EasyMotion
    Plug 'easymotion/vim-easymotion'
    " IndentLine
    Plug 'yggdroot/indentline'
    " Fugitive Git wrapper
    Plug 'tpope/vim-fugitive'
   "" Startify
   " Plug 'mhinz/vim-startify'
    " Dashboard 
    Plug 'glepnir/dashboard-nvim' 
    " Telescope - fuzzy file finder
    Plug 'nvim-lua/popup.nvim'
    Plug 'nvim-lua/plenary.nvim'
    Plug 'nvim-telescope/telescope.nvim'
    " Comment/Uncomment tool
    Plug 'scrooloose/nerdcommenter'
    " Switch to the begining and the end of a block by pressing %
    Plug 'tmhedberg/matchit'
    " Nord
    Plug 'arcticicestudio/nord-vim'
    " Better syntax-highlighting for filetypes in vim
    Plug 'sheerun/vim-polyglot'
    " Intellisense engine
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Auto-close braces and scopes
    Plug 'jiangmiao/auto-pairs'
    " barbar tabline
    Plug 'romgrk/barbar.nvim'

call plug#end()
