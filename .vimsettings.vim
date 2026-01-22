" Use actual tab characters instead of spaces
set noexpandtab
set tabstop=4      " Visual width of a tab character
set shiftwidth=4   " Number of spaces to use for autoindent
set softtabstop=-1 " Use value from shiftwidth (makes Tab/Shift-Tab work properly)

" Filetype-specific settings - override with 4-space tabs for C/C++ files
autocmd Filetype h setlocal noexpandtab tabstop=4 shiftwidth=4 softtabstop=-1
autocmd Filetype hpp setlocal noexpandtab tabstop=4 shiftwidth=4 softtabstop=-1
autocmd Filetype c setlocal noexpandtab tabstop=4 shiftwidth=4 softtabstop=-1
autocmd Filetype cpp setlocal noexpandtab tabstop=4 shiftwidth=4 softtabstop=-1

" Keep your existing key mapping
nnoremap cc :e %:p:s,.h$,.X123X,:s,.cpp$,.h,:s,.X123X$,.cpp,<CR>
