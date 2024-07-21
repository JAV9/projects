**Be aware that using built-ins and keywords are so much more efficient than commands (executables in external files), especially when invoked repeatedly in a loop**

```
$ compgen -k

if
then
else
elif
.
.
.
```

>You can use the compgen command to determine what commands, built-ins, and keywords are available to you. Use the -c option to list commands, -b for built-ins, and -k for keywords

**Redirection and piping**
>Stdin is file descriptor
0, stdout is file descriptor 1, and stderr is file descriptor 2, so we can redirect error messages this way 

`handywork 2> err.msgs`
>This redirects only stderr and sends any such error message output to a file we call err.msgs

`handywork < data.in > results.out 2>&1`
>This combines normal err msgs with normal output (as it does by default when both are written to the screen). Sends stderr(2) to the same location as file descriptor 1 (&1). Note that without the ampersand. the error messages would just be sent to a file named '1'. The combining of stdout and stderr is so common that there is a useful shorthand notation:
`handywork < data.in &> results.out`

*WARNING*
>*Be careful not to confuse & (which is used to send a task to the background) and &> (which is used to perform a combined redirect of standard output and standard error).*

**Running commands in the background**
> Using the & operator.
`ping 192.168.10.56 > ping.log &`
> You can use *jobs* command to list any tasks currently running in the background. Use the *fg* command and the corresponding job number to bring the task back into the foreground.

**From command line to script**
`#!/bin/bash -`
`#!/usr/bin/env bash`