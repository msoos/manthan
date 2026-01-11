autocmd Filetype h setlocal tabstop=4 shiftwidth=4 softtabstop=4 noexpandtab
autocmd Filetype hpp setlocal tabstop=4 shiftwidth=4 softtabstop=4 noexpandtab
autocmd Filetype c setlocal tabstop=4 shiftwidth=4 softtabstop=4 noexpandtab
autocmd Filetype cpp setlocal tabstop=4 shiftwidth=4 softtabstop=4 noexpandtab
set shiftwidth=4
set noexpandtab
setlocal shiftwidth=4
setlocal noexpandtab
nnoremap cc :e %:p:s,.h$,.X123X,:s,.cpp$,.h,:s,.X123X$,.cpp,<CR>
