return {
	"lukas-reineke/indent-blankline.nvim",
	event = { "BufReadPost", "BufNewFile" },
	main = "ibl",
	opts = {
		indent = {
			char = "▎",
		},
		scope = {
			enabled = true,
			show_start = false,
			show_end = false,
		},
		exclude = {
			filetypes = {
				"help",
				"alpha",
				"dashboard",
				"nvim-tree",
				"Trouble",
				"lazy",
				"mason",
			},
		},
	},
}
