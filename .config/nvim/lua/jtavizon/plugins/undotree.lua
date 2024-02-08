return {
    "mbbill/undotree",
    keys = {
        {"<leader>u", "<cmd>UndotreeToggle<CR>", desc = "Toggle undotree"},
    },
    config = function()
        vim.opt.undodir = os.getenv("HOME") .. "/.vim/undodir"
        vim.opt.undofile = true
        vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle)
    end,
}
