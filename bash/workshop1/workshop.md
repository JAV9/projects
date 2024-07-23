*1. Write a command that executes ifconfig and redirects standard output to a file named ipaddress.txt*
> `ifconfig > ipaddress.txt`

*2. Write a command that executes ifconfig and redirects standard output and appends it to a file named ipaddress.txt.*
> `ifconfig >> ipaddress.txt`

*3. Write a command that copies all of the files in the directory /etc/a to the directory /etc/b and redirects standard error to the file copyerror.log.*
> `cp -r /etc/a/* /etc/b 2> copyerror.log`

*4. Write a command that performs a directory listing (ls) on the root file directory and pipes the output into the more command.*
> `ls / | more`

*5. Write a command that executes mytask.sh and sends it to the background.*
> `./mytask.sh &`

*6. Given the following job list, write the command that brings the Amazon ping task to the foreground.*
```
[1] Running ping www.google.com > /dev/null & 
[2]- Running ping www.amazon.com > /dev/null &
[3]+ Running ping www.oreilly.com > /dev/null &
```
> `fg 2`