set nomore
runtime plugin/vimballPlugin.vim
let g:vimball_home = getcwd()
call mkdir("plugin", "p")
call writefile(readfile("greeting.vim"), "plugin/greeting.vim")
edit manifest.txt
1,1MkVimball! hello
qa!
