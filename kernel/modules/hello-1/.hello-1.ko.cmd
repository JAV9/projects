savedcmd_/home/javi/Documents/kernel/modules/hello-1/hello-1.ko := ld -r -m elf_x86_64 -z noexecstack --build-id=sha1  -T scripts/module.lds -o /home/javi/Documents/kernel/modules/hello-1/hello-1.ko /home/javi/Documents/kernel/modules/hello-1/hello-1.o /home/javi/Documents/kernel/modules/hello-1/hello-1.mod.o;  make -f ./arch/x86/Makefile.postlink /home/javi/Documents/kernel/modules/hello-1/hello-1.ko
