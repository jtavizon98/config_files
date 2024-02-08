" My .vimrc Jairo Tavizon
" barebones for use in ssh connections when absolutely necessary

" Automatic Reloading of .vimrc
autocmd! bufwritepost .vimrc source %

" Sets =========================================================================

" Mouse functionality
set mouse=a

" Real programmers dont't use TABs but spaces
set tabstop=4 softtabstop=4
set expandtab
set shiftwidth=4
set shiftround

" Makin' it pretty 
syntax enable
set smartindent
set relativenumber
set number
set nohlsearch
set colorcolumn=80
highlight ColorColumn ctermbg=0
set scrolloff=10
set signcolumn=yes
set nowrap

" Lightline
set laststatus=2

" Undo fun
set undodir=~/.vim/undodir
set undofile

" Make search case insensitive
set ignorecase
set incsearch
set hlsearch
set smartcase

" Disable backup and swap files - they cause problems
set nobackup
set nowritebackup
set noswapfile

" Open new windows in a logical order
set splitbelow splitright

" Plugins ======================================================================

" Using vim-plug ---------------------------------------------------------------
call plug#begin('~/.vim/plugged')

" Catppuccin theme
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'itchyny/lightline.vim'

" Undo history of that file
Plug 'mbbill/undotree'

" Syntax highlighting for many languages
Plug 'sheerun/vim-polyglot'

" Creates automatic pairs for (, [, {, "
Plug 'jiangmiao/auto-pairs'

" Shows indentation lines
Plug 'Yggdroot/indentLine'

call plug#end()
"-------------------------------------------------------------------------------

colorscheme catppuccin_macchiato
let g:lightline = {'colorscheme': 'catppuccin_mocha'}

" Automatically install missing plugins on startup
autocmd VimEnter *
  \  if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \|   PlugInstall --sync | q
  \| endif


" Keybindings ==================================================================

" Rebind <Leader> key
let mapleader = " "

" Basic navigation keybindings
nnoremap <leader>q :q<CR>
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>
nnoremap <leader>u :UndotreeShow<CR>
nnoremap <silent> <leader>= :vertical resize +5<CR>
nnoremap <silent> <leader>- :vertical resize -5<CR>
nnoremap <leader>s :split<CR>
nnoremap <leader>vs :vsplit<CR>

" easier moving of code blocks
vnoremap < <gv
vnoremap > >gv

" Toggle relative line number
nmap <C-n><C-n> :set invrelativenumber<CR>

" copying from vim to the clipboard
vnoremap <C-y> "+y
map <C-p> "+PDelete .config/nvim/lua/setup directory
