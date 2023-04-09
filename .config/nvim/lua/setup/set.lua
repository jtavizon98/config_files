-- Oldstyle cursor
vim.opt.guicursor = ""

-- Mouse functionality
vim.opt.mouse = "a"

-- Real programmers dont't use TABs but spaces
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.expandtab = true
vim.opt.shiftwidth = 4

-- Makin' it pretty 
vim.opt.smartindent = true

vim.opt.wrap = false

vim.opt.number = true
vim.opt.relativenumber = true

vim.opt.termguicolors = true

vim.opt.scrolloff = 10
vim.opt.signcolumn = "yes"
vim.opt.colorcolumn = "80"

-- Incremental search
vim.opt.ignorecase = true
vim.opt.incsearch = true
vim.opt.hlsearch = false
vim.opt.smartcase = true

-- Disable backup and swap files - they cause problems
vim.opt.backup = false
vim.opt.swapfile = false

-- Undo fun
vim.opt.undodir = os.getenv("HOME") .. "/.vim/undodir"
vim.opt.undofile = true

-- Open new windows in a logical order
vim.opt.splitbelow = true
vim.opt.splitright = true

vim.opt.updatetime = 50

