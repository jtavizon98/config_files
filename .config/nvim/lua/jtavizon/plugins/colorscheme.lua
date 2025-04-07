return {
	"catppuccin/nvim",
	name = "catppuccin",
	priority = 1000,
	opts = {
		flavour = "mocha",
		background = {
			light = "latte",
			dark = "mocha",
		},
		integrations = {
			alpha = true,
			cmp = true,
			indent_blankline = {
				enabled = true,
				scope_color = "",
				colored_indent_levels = false,
			},
			nvimtree = true,
			treesitter = true,
			telescope = {
				enabled = true,
			},
		},
	},
	config = function()
		-- load colorscheme
		vim.cmd([[colorscheme catppuccin]])
	end,
}
