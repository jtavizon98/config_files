return {
	"catppuccin/nvim",
	name = "catppuccin",
	priority = 1000,
	opts = {
		flavour = "mocha",
		integrations = {
			alpha = true,
			cmp = true,
			-- Updated for IBL v3
			indent_blankline = {
				enabled = true,
				scope_color = "lavender", -- You can specify a catppuccin color here
				colored_indent_levels = false,
			},
			nvimtree = true,
			treesitter = true,
			telescope = {
				enabled = true,
			},
		},
	},
	config = function(_, opts)
		require("catppuccin").setup(opts)
		vim.cmd.colorscheme("catppuccin")
	end,
}
