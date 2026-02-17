return {
    "mbbill/undotree",
    config = function()
        local undodir = vim.fn.expand("~") .. "/.vim/undodir"
        vim.fn.mkdir(undodir, "p")
        vim.opt.undodir = undodir
        vim.opt.undofile = true
        vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle, { desc = "Toggle undotree" })
    end,
}
