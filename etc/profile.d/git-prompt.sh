#!/usr/bin/env bash
if test -f /etc/profile.d/git-sdk.sh
then
	TITLEPREFIX=SDK-${MSYSTEM#MINGW}
else
	TITLEPREFIX=$MSYSTEM
fi

if test -f ~/.config/git/git-prompt.sh
then
	. ~/.config/git/git-prompt.sh
else
	PS1='\[\033]0;$MSYSTEM:$PWD\007\]' # set window titleif test -z "$WINELOADERNOEXEC"
	PS1="$PS1"'\[\033[36m\]'       # change to green
	PS1="$PS1"'($MSYSTEM) '             # user@host<space>
	PS1="$PS1"'\[\033[32m\]'       # change to green
	PS1="$PS1"'\u@\h'             # user@host<space>
	PS1="$PS1"'\[\033[0m\]'        # change color
	PS1="$PS1"':'             # user@host<space>
	PS1="$PS1"'\[\033[34m\]'       # change to brownish yellow
	PS1="$PS1"'\w'                 # current working directory

	PS1="$PS1"'\[\033[0m\]'        # change color
	PS1="$PS1"''                 # new line
	PS1="$PS1"'$ '                 # prompt: always $
fi

MSYS2_PS1="$PS1"               # for detection by MSYS2 SDK's bash.basrc

# Evaluate all user-specific Bash completion scripts (if any)
if test -z "$WINELOADERNOEXEC"
then
	for c in "$HOME"/bash_completion.d/*.bash
	do
		# Handle absence of any scripts (or the folder) gracefully
		test ! -f "$c" ||
		. "$c"
	done
fi
alias lua="/usr/bin/lua.exe"
alias far="/usr/bin/far/far.exe"
alias beep="/usr/bin/beep.exe"
alias graphics="python /bin/graphics.py"
alias connect="python /bin/connect.py"
alias edit="/usr/bin/far/edit.exe"
alias commit='git commit -a -m '
alias mirror="git push origin main"
alias ifconfig="python /usr/bin/ifconfig.py"
alias apt="python /etc/profile.d/apt.py"
alias apt-get="python /etc/profile.d/apt.py"
alias kb="/bin/kb.exe"
alias log="git log"
alias ipy="/sample/IronPython/ipy.exe"
alias pip="/sample/IronPython/Scripts/pip.exe"