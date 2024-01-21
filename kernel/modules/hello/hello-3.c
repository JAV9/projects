#include <linux/init.h>
#include <linux/module.h>
#include <linux/printk.h>
 
static int hello_3_data __initdata = 3;       
 
int __init hello_3_init(void)
{
        pr_info("Hello, world %d\n", hello_3_data);
	return 0;
}
 
void __exit hello_3_exit(void)
{
	/* hello_3_data can't be used outside of init */
	pr_info("Godbye, world %d\n", 3);
	
}
 
module_init(hello_3_init);
module_exit(hello_3_exit); 

MODULE_LICENSE("GPl");
