-- LSP Configuration using nvim-lspconfig (Neovim 0.11+)
-- nvim-lspconfig provides default configs and convenience commands (:LspInfo, :LspRestart, etc.)
return {
    "neovim/nvim-lspconfig",
    event = { "BufReadPre", "BufNewFile" },
    dependencies = {
        "hrsh7th/cmp-nvim-lsp",
        { "antosha417/nvim-lsp-file-operations", config = true },
    },
    config = function()
        local capabilities = require("cmp_nvim_lsp").default_capabilities()

        vim.api.nvim_create_autocmd("LspAttach", {
            group = vim.api.nvim_create_augroup("UserLspConfig", {}),
            callback = function(ev)
                local opts = { noremap = true, silent = true, buffer = ev.buf }

                opts.desc = "Go to definition"
                vim.keymap.set("n", "gd", "<cmd>Telescope lsp_definitions<CR>", opts)

                opts.desc = "Show LSP implementations"
                vim.keymap.set("n", "gI", "<cmd>Telescope lsp_implementations<CR>", opts)

                opts.desc = "Show LSP type definitions"
                vim.keymap.set("n", "gt", "<cmd>Telescope lsp_type_definitions<CR>", opts)

                opts.desc = "See available code actions"
                vim.keymap.set({ "n", "v" }, "<leader>ca", vim.lsp.buf.code_action, opts)

                opts.desc = "Smart rename"
                vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename, opts)

                opts.desc = "Show buffer diagnostics"
                vim.keymap.set("n", "<leader>db", "<cmd>Telescope diagnostics bufnr=0<CR>", opts)

                opts.desc = "Show line diagnostics"
                vim.keymap.set("n", "<leader>dl", vim.diagnostic.open_float, opts)

                opts.desc = "Go to previous diagnostic"
                vim.keymap.set("n", "[d", function()
                    vim.diagnostic.goto_prev({ float = { border = "rounded" } })
                end, opts)

                opts.desc = "Go to next diagnostic"
                vim.keymap.set("n", "]d", function()
                    vim.diagnostic.goto_next({ float = { border = "rounded" } })
                end, opts)

                opts.desc = "Show documentation"
                vim.keymap.set("n", "K", vim.lsp.buf.hover, opts)

                opts.desc = "Restart LSP"
                vim.keymap.set("n", "<leader>rs", "<cmd>LspRestart<CR>", opts)
            end,
        })

        vim.api.nvim_create_autocmd("LspDetach", {
            group = vim.api.nvim_create_augroup("UserLspConfigDetach", {}),
            callback = function(ev)
                local mappings = { "gd", "gI", "gt", "<leader>ca", "<leader>rn", "<leader>db", "<leader>dl", "[d", "]d", "K", "<leader>rs" }
                for _, mapping in ipairs(mappings) do
                    pcall(vim.keymap.del, "n", mapping, { buffer = ev.buf })
                end
            end,
        })

        local severity = vim.diagnostic.severity
        vim.diagnostic.config({
            underline = true,
            signs = {
                text = {
                    [severity.ERROR] = " ",
                    [severity.WARN] = " ",
                    [severity.HINT] = "󰠠 ",
                    [severity.INFO] = " ",
                },
            },
            update_in_insert = false,
            severity_sort = true,
            float = {
                border = "rounded",
                source = true,
                header = "",
                prefix = "",
            },
        })

        vim.lsp.config("pylsp", {
            capabilities = capabilities,
            settings = {
                pylsp = {
                    plugins = {
                        pycodestyle = { enabled = false },
                        pyflakes = { enabled = false },
                        mccabe = { enabled = false },
                        pylint = { enabled = false },
                    },
                },
            },
            before_init = function(_, config)
                local venv = vim.env.VIRTUAL_ENV
                if venv then
                    config.settings = config.settings or {}
                    config.settings.pylsp = config.settings.pylsp or {}
                    config.settings.pylsp.plugins = config.settings.pylsp.plugins or {}
                    config.settings.pylsp.plugins.jedi = config.settings.pylsp.plugins.jedi or {}
                    config.settings.pylsp.plugins.jedi.environment = venv .. "/bin/python"
                end
            end,
        })

        vim.lsp.config("lua_ls", {
            capabilities = capabilities,
            settings = {
                Lua = {
                    diagnostics = { globals = { "vim" } },
                    workspace = {
                        library = {
                            [vim.fn.expand("$VIMRUNTIME/lua")] = true,
                            [vim.fn.stdpath("config") .. "/lua"] = true,
                        },
                    },
                },
            },
        })

        vim.lsp.config("bashls", { capabilities = capabilities })
        vim.lsp.config("clangd", { capabilities = capabilities })
        vim.lsp.config("ltex", {
            capabilities = capabilities,
            cmd = { "env", "JAVA_OPTS=-Djdk.xml.totalEntitySizeLimit=0", vim.fn.exepath("ltex-ls") },
        })
        vim.lsp.config("texlab", { capabilities = capabilities })

        vim.lsp.enable({ "bashls", "clangd", "ltex", "texlab", "pylsp", "lua_ls" })
    end,
}
