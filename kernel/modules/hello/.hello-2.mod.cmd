savedcmd_/home/javi/Documents/projects/kernel/modules/hello/hello-2.mod := printf '%s\n'   hello-2.o | awk '!x[$$0]++ { print("/home/javi/Documents/projects/kernel/modules/hello/"$$0) }' > /home/javi/Documents/projects/kernel/modules/hello/hello-2.mod
