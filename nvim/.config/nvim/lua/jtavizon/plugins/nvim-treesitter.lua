return {
	{
		"nvim-treesitter/nvim-treesitter",
		lazy = false,
		branch = "main",
		build = ":TSUpdate",
		dependencies = {
			{ "nvim-treesitter/nvim-treesitter-textobjects", branch = "main" },
			"windwp/nvim-ts-autotag",
		},
		config = function()
			require("nvim-treesitter").setup()

			vim.api.nvim_create_autocmd("FileType", {
				pattern = "*",
				callback = function()
					pcall(vim.treesitter.start)
				end,
			})

			require("nvim-ts-autotag").setup()
		end,
	},
}
