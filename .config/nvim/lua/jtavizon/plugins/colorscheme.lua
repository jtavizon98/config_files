return {
    "catppuccin/nvim",
    name = "catppuccin",
    priority = 1000,
    opts = { flavour = mocha },
    config = function()
        -- load colorscheme
        vim.cmd([[colorscheme catppuccin]])
    end,
}
