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
    # Configure BASH Prompt 
    PS1='\[\033]0;$MSYSTEM:$PWD\007\]'    # Set Window title
    PS1="$PS1"'\[\033[36m\]'       		  # change to Bubble blue
    PS1="$PS1"'($MSYSTEM) '        		  # Print protocol
    PS1="$PS1"'\[\033[32m\]'       		  # change to green
    PS1="$PS1"'\u@\h'             		  # user@host <space>
    PS1="$PS1"'\[\033[0m\]'        		  # change color
    PS1="$PS1"':'             		      # Set diretory division :
    PS1="$PS1"'\[\033[34m\]'       		  # change to brownish yellow
    PS1="$PS1"'\w'                 		  # current working directory
    PS1="$PS1"'\[\033[0m\]'        		  # change color
    PS1="$PS1"''                	 	  # new line
    PS1="$PS1"'$ '                 		  # prompt: always $
fi

MSYS2_PS1="$PS1"               # for detection by MSYS2 SDK's bash.basrc
# Bash completion
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

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
# Global variables
SYSTEM="osystem"
HOME="/home"

cd $HOME
# OSystem Commands
alias ls="ls --color=auto -CF" 
alias dir='dir --color=auto'
alias ll='vdir --color=auto'
alias commit='git commit -a -m ' # Git Commit
alias mirror="git push origin main" # Git push
alias ifconfig="python /usr/bin/ifconfig.py" # Print Ethernet Settings
alias kb="/bin/kb.exe" # kb Application
alias log="git log" # Git log
alias wget="/bin/wget.exe" # WGET