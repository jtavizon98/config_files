return {
    "stevearc/conform.nvim",
    lazy = true,
    event = { "BufReadPre", "BufNewFile" }, -- to disable, comment this out
    config = function()
        local conform = require("conform")

        local function repository_name(bufnr)
            local filename = vim.api.nvim_buf_get_name(bufnr)
            local root = filename ~= "" and vim.fs.root(filename, ".git") or nil
            return root and vim.fs.basename(root) or nil
        end

        local function format_options(bufnr)
            local exclude_filetypes = { "help", "alpha", "dashboard", "lazy", "mason" }
            local filetype = vim.bo[bufnr].filetype
            if vim.tbl_contains(exclude_filetypes, filetype) then
                return
            end

            local repository = repository_name(bufnr)
            if repository == "TopCPToolkit" then
                if vim.tbl_contains({ "c", "cpp", "objc", "objcpp", "cuda" }, filetype) then
                    return { timeout_ms = 1000, formatters = {}, lsp_format = "prefer" }
                elseif filetype == "python" then
                    return { timeout_ms = 1000, formatters = { "black" }, lsp_format = "never" }
                end

                return { timeout_ms = 1000, formatters = {}, lsp_format = "never", quiet = true }
            elseif repository == "fastframes" then
                return { timeout_ms = 1000, formatters = {}, lsp_format = "never", quiet = true }
            end

            return { timeout_ms = 1000, lsp_format = "fallback" }
        end

        conform.setup({
            formatters_by_ft = {
                json = { "prettier" },
                yaml = { "prettier" },
                markdown = { "prettier" },
                lua = { "stylua" },
                python = { "isort", "black" },
                latex = { "latexindent" },
            },
            format_on_save = format_options,
        })

        vim.keymap.set({ "n", "v" }, "<leader>mp", function()
            local options = format_options(0)
            if not options then
                return
            end
            options.async = false
            conform.format(options)
        end, { desc = "Format file or range (in visual mode)" })
    end,
}
