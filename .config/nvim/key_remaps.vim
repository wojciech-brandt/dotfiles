""""""""""""""
" KEY REMAPS "
""""""""""""""

" using space as leader
nnoremap <Space> <Nop>
let mapleader=" "

" easier jumping between windows
nnoremap <leader>h <C-w>h
nnoremap <leader>j <C-w>j
nnoremap <leader>k <C-w>k
nnoremap <leader>l <C-w>l

" faster NvimTree opening
nnoremap <leader><leader>n :NvimTreeToggle<CR>

" saving 
nnoremap <leader>w :update<cr>
nnoremap <leader>W :wa<cr>

" opening the terminal and easier exit
nnoremap <leader><leader>t <C-w>s:terminal<cr>10<C-w>_
tnoremap <Esc> <C-\><C-n>

" quickly closing a window
nnoremap <leader>q <C-w>q

" Making adjusting window sizes a bit more friendly
nnoremap <silent> <C-Left> :vertical resize +3<CR>
nnoremap <silent> <C-Right> :vertical resize -3<CR>
nnoremap <silent> <C-Up> :resize +3<CR>
nnoremap <silent> <C-Down> :resize -3<CR>


" Move to previous/next
nnoremap <silent>    <A-,> :BufferPrevious<CR>
nnoremap <silent>    <A-.> :BufferNext<CR>
" Re-order to previous/next
nnoremap <silent>    <A-<> :BufferMovePrevious<CR>
nnoremap <silent>    <A->> :BufferMoveNext<CR>
" Goto buffer in position...
nnoremap <silent>    <A-1> :BufferGoto 1<CR>
nnoremap <silent>    <A-2> :BufferGoto 2<CR>
nnoremap <silent>    <A-3> :BufferGoto 3<CR>
nnoremap <silent>    <A-4> :BufferGoto 4<CR>
nnoremap <silent>    <A-5> :BufferGoto 5<CR>
nnoremap <silent>    <A-6> :BufferGoto 6<CR>
nnoremap <silent>    <A-7> :BufferGoto 7<CR>
nnoremap <silent>    <A-8> :BufferGoto 8<CR>
nnoremap <silent>    <A-9> :BufferLast<CR>
" Close buffer
nnoremap <silent>    <A-c> :BufferClose<CR>
" Magic buffer-picking mode
nnoremap <silent>    <A-s> :BufferPick<CR>


