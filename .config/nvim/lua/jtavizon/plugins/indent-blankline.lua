return {
    "lukas-reineke/indent-blankline.nvim",
    main = "ibl",
    config = function()
        local ibl = require("ibl")
        -- local highlight = {
        --     "red",
        --     "yellow",
        --     "blue",
        --     "green",
        --     "peach",
        --     "mauve",
        --     "teal",
        --     "pink",
        --     "maroon",
        -- }
        --
        -- local hooks = require("ibl.hooks")
        -- -- create the highlight groups in the highlight setup hook, so they are reset
        -- -- every time the colorscheme changes
        -- hooks.register(hooks.type.HIGHLIGHT_SETUP, function()
        --     vim.api.nvim_set_hl(0, "red", { fg = "#ed8796" })
        --     vim.api.nvim_set_hl(0, "yellow", { fg = "#eed49f" })
        --     vim.api.nvim_set_hl(0, "blue", { fg = "#8aadf4" })
        --     vim.api.nvim_set_hl(0, "green", { fg = "#a6da95" })
        --     vim.api.nvim_set_hl(0, "peach", { fg = "#f5a97f" })
        --     vim.api.nvim_set_hl(0, "mauve", { fg = "#c6a0f6" })
        --     vim.api.nvim_set_hl(0, "teal", { fg = "#8bd5ca" })
        --     vim.api.nvim_set_hl(0, "pink", { fg = "#f5bde6" })
        --     vim.api.nvim_set_hl(0, "maroon", { fg = "#ee99a0" })
        -- end)
        --
        -- ibl.setup({ indent = { highlight = highlight } })
        ibl.setup()
    end,
    -- opts = {},
}
