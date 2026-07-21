-- Rebind <Leader> key
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Basic navigation keybindings
vim.keymap.set("n", "<leader>q", ":q<CR>", { desc = "Quit" })

vim.keymap.set("n", "<leader>h", ":wincmd h<CR>", { desc = "Move to left window" })
vim.keymap.set("n", "<leader>j", ":wincmd j<CR>", { desc = "Move to bottom window" })
vim.keymap.set("n", "<leader>k", ":wincmd k<CR>", { desc = "Move to top window" })
vim.keymap.set("n", "<leader>l", ":wincmd l<CR>", { desc = "Move to right window" })

vim.keymap.set("n", "<leader>=", ":vertical resize +5<CR>", { silent = true, desc = "Increase window width" })
vim.keymap.set("n", "<leader>-", ":vertical resize -5<CR>", { silent = true, desc = "Decrease window width" })
vim.keymap.set("n", "<leader>\\", ":split<CR>", { desc = "Split window horizontally" })
vim.keymap.set("n", "<leader>|", ":vsplit<CR>", { desc = "Split window vertically" })

-- easier moving of code blocks
vim.keymap.set("v", "<", "<gv", { desc = "Indent left and reselect" })
vim.keymap.set("v", ">", ">gv", { desc = "Indent right and reselect" })

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv", { desc = "Move selection down" })
vim.keymap.set("v", "K", ":m '>-2<CR>gv=gv", { desc = "Move selection up" })

-- keeping things in the middle
vim.keymap.set("n", "<C-d>", "<C-d>zz", { desc = "Scroll down and center" })
vim.keymap.set("n", "<C-u>", "<C-u>zz", { desc = "Scroll up and center" })
vim.keymap.set("n", "n", "nzzzv", { desc = "Next search result and center" })
vim.keymap.set("n", "N", "Nzzzv", { desc = "Previous search result and center" })

-- Persistent clipboard after Paste over deletion
vim.keymap.set("x", "<leader>P", [["_dP]], { desc = "Paste without yanking" })

-- copying from vim to the clipboard
vim.keymap.set({ "n", "v" }, "<leader>y", [["+y]], { desc = "Yank to system clipboard" })
vim.keymap.set("n", "<leader>Y", [["+Y]], { desc = "Yank line to system clipboard" })

-- eXterminate: delete to void register
vim.keymap.set({ "n", "v" }, "<leader>x", [["_d]], { desc = "Delete without yanking" })

-- For visual block mode editing
vim.keymap.set("i", "<C-c>", "<Esc>", { desc = "Exit insert mode" })

-- Easier find and replace
vim.keymap.set("n", "<leader>S", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]], { desc = "Replace word under cursor" })
