return {
	{
		"nvim-treesitter/nvim-treesitter",
		event = { "BufReadPre", "BufNewFile" },
		build = ":TSUpdate",
		dependencies = {
			"nvim-treesitter/nvim-treesitter-textobjects",
			"windwp/nvim-ts-autotag",
		},
		config = function()
			local treesitter = require("nvim-treesitter.configs")

			treesitter.setup({
				highlight = { enable = true },
				indent = { enable = true },
				ensure_installed = {
					"json",
					"html",
					"bash",
					"lua",
					"vim",
					"dockerfile",
					"gitignore",
					"python",
					"latex",
					"bibtex",
					"c",
					"cpp",
				},
			})

			require("nvim-ts-autotag").setup()
		end,
	},
}
