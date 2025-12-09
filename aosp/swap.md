### Increase the size of swap memory in Ubuntu using terminal

Check your existing swap    
```shell
swapon --show
```
Output:
```shell
NAME      TYPE SIZE USED PRIO
/swapfile file  64G 1.8G   -2
```

First disable the existing swap file:    
```shell
sudo swapoff /swap.img
```

Now let's increase the size of swap file:   
```shell
sudo dd if=/dev/zero of=/swap.img bs=1M count=1024 oflag=append conv=notrunc
```

The above command will append 1GiB of zero bytes at the end of your swap file. Multiply **your_desired_size x 1024** in GB. 25600 will make 25 GB of swap memory.

Setup the file as a "swap file":    
```shell
sudo mkswap /swap.img
```

Enable swaping:     
```shell
sudo swapon /swap.img
```
