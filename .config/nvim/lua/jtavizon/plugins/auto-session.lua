return {
	"rmagatti/auto-session",
	config = function()
		require("auto-session").setup({
			auto_restore_enabled = false,
			-- Updated: suppressed_dirs is the modern key name
			suppressed_dirs = { "~/", "~/Downloads", "~/Documents", "~/Desktop/" },
		})

		vim.keymap.set("n", "<leader>wr", "<cmd>AutoSession restore<CR>", { desc = "Restore session" })
		vim.keymap.set("n", "<leader>ws", "<cmd>AutoSession save<CR>", { desc = "Save session" })
	end,
}
