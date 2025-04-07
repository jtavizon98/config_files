require("catppuccin").setup({
    flavour = "mocha"
})
function ColorMyPencils(color) 
	color = "catppuccin"
	vim.cmd.colorscheme(color)
end

ColorMyPencils()
