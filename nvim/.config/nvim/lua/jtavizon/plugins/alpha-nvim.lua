return {
	"goolord/alpha-nvim",
	event = "VimEnter",
	dependencies = { "nvim-tree/nvim-web-devicons" },
	config = function()
		local alpha = require("alpha")
		local dashboard = require("alpha.themes.dashboard")

		-- Header
		dashboard.section.header.val = {
			"        ▄▄▄▄▄███████████████████▄▄▄▄▄     ",
			"      ▄██████████▀▀▀▀▀▀▀▀▀▀██████▀████▄   ",
			"     █▀████████▄             ▀▀████ ▀██▄  ",
			"    █▄▄██████████████████▄▄▄         ▄██▀ ",
			"     ▀█████████████████████████▄    ▄██▀  ",
			"       ▀████▀▀▀▀▀▀▀▀▀▀▀▀█████████▄▄██▀    ",
			"         ▀███▄              ▀██████▀      ",
			"           ▀██████▄        ▄████▀         ",
			"              ▀█████▄▄▄▄▄▄▄███▀           ",
			"                ▀████▀▀▀████▀             ",
			"                  ▀███▄███▀               ",
			"                     ▀█▀                  ",
		}

		-- Set menu
		dashboard.section.buttons.val = {
			dashboard.button("n", "  > New File", "<cmd>ene<CR>"),
			dashboard.button("e", "  > Toggle file explorer", "<cmd>NvimTreeToggle<CR>"),
			dashboard.button("f", "󰱼  > Find File", "<cmd>Telescope find_files<CR>"),
			dashboard.button("s", "  > Find Word", "<cmd>Telescope live_grep<CR>"),
			dashboard.button("r", "󰁯  > Restore Session For Current Directory", "<cmd>SessionRestore<CR>"),
			dashboard.button("q", "  > Quit NVIM", "<cmd>qa<CR>"),
		}

		-- Send config to alpha
		alpha.setup(dashboard.opts)

		-- Disable folding on alpha buffer
		vim.api.nvim_create_autocmd("FileType", {
			pattern = "alpha",
			callback = function()
				vim.opt_local.foldenable = false
			end,
		})
	end,
}
