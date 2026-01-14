-- Rebind <Leader> key
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Basic navigation keybindings
vim.keymap.set("n", "<leader>q", ":q<CR>")

vim.keymap.set("n", "<leader>h", ":wincmd h<CR>")
vim.keymap.set("n", "<leader>j", ":wincmd j<CR>")
vim.keymap.set("n", "<leader>k", ":wincmd k<CR>")
vim.keymap.set("n", "<leader>l", ":wincmd l<CR>")

vim.keymap.set("n", "<silent> <leader>=", ":vertical resize +5<CR>")
vim.keymap.set("n", "<silent> <leader>-", ":vertical resize -5<CR>")
vim.keymap.set("n", "<leader>\\", ":split<CR>")
vim.keymap.set("n", "<leader>|", ":vsplit<CR>")

-- easier moving of code blocks
vim.keymap.set("v", "<", "<gv")
vim.keymap.set("v", ">", ">gv")

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '>-2<CR>gv=gv")

-- keeping things in the middle
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- Persistent clipboard after Paste over deletion
vim.keymap.set("x", "<leader>P", [["_dP]])

-- copying from vim to the clipboard
vim.keymap.set({ "n", "v" }, "<leader>y", [["+y]])
vim.keymap.set("n", "<leader>Y", [["+Y]])

-- eXterminate: delete to void register
vim.keymap.set({ "n", "v" }, "<leader>x", [["_d]])

-- For visual block mode editing
vim.keymap.set("i", "<C-c>", "<Esc>")

-- Easier find and replace
vim.keymap.set("n", "<leader>S", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])
