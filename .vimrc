" My .vimrc Jairo Tavizon

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

" Dracula theme from https://draculatheme.com/
"Plug 'dracula/vim',{'as':'dracula'}
"Plug 'vim-airline/vim-airline'
"Plug 'vim-airline/vim-airline-themes'

" Catppuccin theme
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'itchyny/lightline.vim'

" Undo history of that file
Plug 'mbbill/undotree'

" Ranger inside vim
Plug 'francoiscabrol/ranger.vim'

" Syntax highlighting for many languages
Plug 'sheerun/vim-polyglot'

" Autocompletion and linting for several languages 
Plug 'neoclide/coc.nvim', {'branch':'release'} 

" Creates automatic pairs for (, [, {, "
Plug 'jiangmiao/auto-pairs'

" Shows indentation lines
Plug 'Yggdroot/indentLine'

" Vimtex for LaTex support
Plug 'lervag/vimtex'

call plug#end()
"-------------------------------------------------------------------------------

colorscheme catppuccin_macchiato
let g:lightline = {'colorscheme': 'catppuccin_mocha'}

" Coc setup --------------------------------------------------------------------

 let g:coc_global_extensions = [
    \ 'coc-jedi',
    \ 'coc-texlab',
    \ 'coc-ltex',
    \ 'coc-sh',
    \]

" Use <tab> and <S-tab> to navigate completion list: >
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

" Insert <tab> when previous text is space, refresh completion if not.
inoremap <silent><expr> <TAB>
  \ coc#pum#visible() ? coc#pum#next(1):
  \ <SID>check_back_space() ? "\<Tab>" :
  \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"


" Use <c-space> to trigger completion.
"inoremap <silent><expr> <c-@> coc#refresh()

" Use <CR> to confirm completion, use: >
inoremap <expr> <CR> coc#pum#visible() ? coc#pum#confirm() : "\<CR>"


" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight the symbol and its references when holding the cursor.
autocmd CursorHold * silent call CocActionAsync('highlight')

" Explorer
let g:coc_explorer_global_presets = {
\   'floating': {
\      'position': 'floating',
\   },
\   'floatingLeftside': {
\      'position': 'floating',
\      'floating-position': 'left-center',
\      'floating-width': 30,
\   },
\   'floatingRightside': {
\      'position': 'floating',
\      'floating-position': 'right-center',
\      'floating-width': 30,
\   },
\   'simplify': {
\     'file.child.template': '[selection | clip | 1] [indent][icon | 1] [filename omitCenter 1]'
\   }
\ }
"nmap <silent> <space>e :CocCommand explorer<CR>
" nnoremap <silent> <leader>e :CocCommand explorer<CR>
" nmap <space>f :CocCommand explorer --preset floatingRightside<CR>
autocmd BufEnter * if (winnr("$") == 1 && &filetype == 'coc-explorer') | q | endif

" LaTex integration ----------------------------------------------------------

let g:coc_filetype_map = {'tex': 'latex'}

"-------------------------------------------------------------------------------

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
map <C-p> "+P

" LaTex compile with compyltex (homemade script with pdflatex, biber & latexmk) 
autocmd FileType tex nnoremap <C-@> :w<Enter>:!compyltex %<Enter>
