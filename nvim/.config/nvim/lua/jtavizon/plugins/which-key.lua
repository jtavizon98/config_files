return {
    "folke/which-key.nvim",
    event = "VeryLazy",
    init = function()
        vim.o.timeout = true
        vim.o.timeoutlen = 500
    end,
    config = function()
        local wk = require("which-key")
        wk.add({
            { "<leader>e", group = "Explorer", icon = "󰙅" },
            { "<leader>f", group = "Find", icon = "󰈞" },
            { "<leader>h", group = "Harpoon", icon = "󱡀" },
            { "<leader>w", group = "Workspace", icon = "󰞏" },
            { "<leader>c", group = "Code", icon = "󰌞" },
            { "<leader>d", group = "Diagnostics", icon = "󰒖" },
            { "<leader>r", group = "Refactor", icon = "󰑓" },
            { "<leader>x", group = "Delete", icon = "󰆴" },
            { "<leader>y", group = "Yank", icon = "󰆏" },
        })
    end,
}
