" ==============================================================================
" Minimal Portable .vimrc
" Drop this on any server - no plugins required
" Keybinds match nvim config for muscle memory
" ==============================================================================

" Automatic Reloading
autocmd! bufwritepost .vimrc source %

" ------------------------------------------------------------------------------
" Basic Settings
" ------------------------------------------------------------------------------
set nocompatible
filetype plugin indent on
syntax enable

" Tabs and indentation
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab
set smartindent

" UI
set number
set relativenumber
set nowrap
set scrolloff=10
set colorcolumn=80
highlight ColorColumn ctermbg=0
set cursorline
set showcmd
set wildmenu
set laststatus=2

" Search
set ignorecase
set smartcase
set incsearch
set hlsearch

" Files
set nobackup
set nowritebackup
set noswapfile
set undofile
set undodir=~/.vim/undodir

" Splits
set splitbelow
set splitright

" Performance
set updatetime=50
set timeoutlen=500

" Mouse
set mouse=a

" Allow hidden buffers
set hidden

" Better command line completion
set wildmode=list:longest

" Terminal colors
if has('termguicolors')
    set termguicolors
endif

" ------------------------------------------------------------------------------
" Leader Key
" ------------------------------------------------------------------------------
let mapleader = " "
let maplocalleader = " "

" ------------------------------------------------------------------------------
" Window Navigation (matches nvim config)
" ------------------------------------------------------------------------------
nnoremap <leader>q :q<CR>
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" Window resizing
nnoremap <silent> <leader>= :vertical resize +5<CR>
nnoremap <silent> <leader>- :vertical resize -5<CR>
nnoremap <leader>\ :split<CR>
nnoremap <leader><bar> :vsplit<CR>

" Save
nnoremap <leader>w :w<CR>

" ------------------------------------------------------------------------------
" Visual Mode (matches nvim config)
" ------------------------------------------------------------------------------
" Keep visual mode when indenting
vnoremap < <gv
vnoremap > >gv

" Move lines up/down in visual mode
vnoremap J :m '>+1<CR>gv=gv
vnoremap K :m '<-2<CR>gv=gv

" ------------------------------------------------------------------------------
" Scrolling (keep centered - matches nvim config)
" ------------------------------------------------------------------------------
nnoremap <C-d> <C-d>zz
nnoremap <C-u> <C-u>zz
nnoremap n nzzzv
nnoremap N Nzzzv

" ------------------------------------------------------------------------------
" Clipboard (matches nvim config)
" ------------------------------------------------------------------------------
" Paste without yanking replaced text
xnoremap <leader>P "_dP

" Yank to system clipboard
nnoremap <leader>y "+y
vnoremap <leader>y "+y
nnoremap <leader>Y "+Y

" Delete to void register
nnoremap <leader>x "_d
vnoremap <leader>x "_d

" Quick paste from system clipboard
nnoremap <C-p> "+P

" ------------------------------------------------------------------------------
" Editing Convenience (matches nvim config)
" ------------------------------------------------------------------------------
" Exit insert mode with Ctrl-C
inoremap <C-c> <Esc>

" Replace word under cursor
nnoremap <leader>S :%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>

" Clear search highlighting
nnoremap <leader><space> :nohlsearch<CR>

" Toggle relative line number
nmap <C-n><C-n> :set invrelativenumber<CR>

" ------------------------------------------------------------------------------
" Buffer Navigation
" ------------------------------------------------------------------------------
nnoremap <leader>bn :bnext<CR>
nnoremap <leader>bp :bprevious<CR>
nnoremap <leader>bd :bdelete<CR>
nnoremap <leader>bl :buffers<CR>

" ------------------------------------------------------------------------------
" Quick Navigation
" ------------------------------------------------------------------------------
nnoremap <C-j> :cnext<CR>
nnoremap <C-k> :cprev<CR>

" ------------------------------------------------------------------------------
" File Explorer (netrw - built-in)
" ------------------------------------------------------------------------------
let g:netrw_banner = 0
let g:netrw_liststyle = 3
let g:netrw_browse_split = 4
let g:netrw_altv = 1
let g:netrw_winsize = 25
nnoremap <leader>ee :Lexplore<CR>
nnoremap <leader>ef :Lexplore %:p:h<CR>

" ------------------------------------------------------------------------------
" Quick Edit vimrc
" ------------------------------------------------------------------------------
nnoremap <leader>ev :e $MYVIMRC<CR>
nnoremap <leader>sv :source $MYVIMRC<CR>

" ------------------------------------------------------------------------------
" Create undodir if it doesn't exist
" ------------------------------------------------------------------------------
if !isdirectory(&undodir)
    call mkdir(&undodir, 'p')
endif

" ------------------------------------------------------------------------------
" Status Line (minimal)
" ------------------------------------------------------------------------------
set statusline=
set statusline+=%f
set statusline+=%m
set statusline+=%r
set statusline+=%=
set statusline+=%y
set statusline+=\ %l:%c
set statusline+=\ %p%%
