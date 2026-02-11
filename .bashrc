# 1. Exit if not running interactively
[[ $- != *i* ]] && return

# 2. Shell Options
shopt -s checkwinsize
shopt -s histappend
shopt -s expand_aliases

# 3. Completion
if [ -r /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
fi

# 4. Prompt (PS1)
C_ROJO='\[\033[1;38;5;196m\]'
C_AZUL='\[\033[1;38;5;27m\]'
C_LBLU='\[\033[1;38;5;31m\]'
C_ROSA='\[\033[1;38;5;200m\]'
C_PURP='\[\033[1;38;5;129m\]'
C_BOLD='\[\033[1m\]'

C_RESET='\[\033[00m\]'

if [[ "$TERM" == "linux" ]]; then
    SYMBOL='$'
else
    SYMBOL="❯"
fi

if [[ ${EUID} == 0 ]]; then
    PS1="${C_ROJO}|\u${C_LBLU}@\h${C_ROJO} ${C_RESET}${C_BOLD}\W${C_ROJO} ${SYMBOL}${C_RESET} "
else
    PS1="${C_AZUL}|\u${C_LBLU}@\h${C_AZUL} ${C_RESET}${C_BOLD}\W${C_AZUL} ${SYMBOL}${C_RESET} "
fi

# Clean up variables
unset C_AZUL C_ROSA C_PURP C_GOLD C_LBLU C_RESET C_ROJO

# 5. Essential Aliases
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias cp='cp -i'
alias df='df -h'
alias free='free -m'
alias more='less'

# 6. Personal Aliases
alias qinit="qtile start -b wayland"
alias dotfiles='git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
complete -cf sudo
