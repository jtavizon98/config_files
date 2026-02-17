return {
    "williamboman/mason.nvim",
    dependencies = {
        "WhoIsSethDaniel/mason-tool-installer.nvim",
    },
    config = function()
        local mason = require("mason")
        local mason_tool_installer = require("mason-tool-installer")

        -- enable mason and configure icons
        mason.setup({
            ui = {
                icons = {
                    package_installed = "✓ ",
                    package_pending = "➜ ",
                    package_uninstalled = "✗ ",
                },
            },
        })

        -- Install LSP servers and tools
        -- Note: With pure native LSP, we install servers via mason-tool-installer
        mason_tool_installer.setup({
            ensure_installed = {
                -- LSP servers
                "bash-language-server",
                "clangd",
                "ltex-ls",
                "texlab",
                "lua-language-server",
                "python-lsp-server",
                -- Formatters and linters
                "prettier",
                "stylua",
                "isort",
                "black",
                "pylint",
                "latexindent",
            },
        })
    end,
}
