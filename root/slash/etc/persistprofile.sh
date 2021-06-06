#!/bin/bash.exe

BB="/bin/busybox.exe"
eval /bin/mount.exe '$SYMLINKS/usr' "/usr" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/bin' "/bin" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/bin' "/usr/bin" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/lib' "/lib" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/lib' "/usr/lib" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/sbin' "/sbin" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/etc' "/etc" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/opt' "/opt" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/src' "/src" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/var' "/var" 2>/dev/null
eval /bin/mount.exe '$SYMLINKS/tmp' "/tmp" 2>/dev/null
/bin/mount.exe -a
. /etc/profile

