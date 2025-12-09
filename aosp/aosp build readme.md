### AOSP Build
Once you have download the repo successfully using repo sync.   
Now, To build aosp follow below commends.   

**Importent**
```
cd aosp15
source build/envsetup.sh
```
Next:
 - Execute `lunch --help` to get more lunch info.

 - This `list_variants` command will display list of **variants**.
 - Next the `list_releases` command will display list of **releases**.
 - And the last and most important command `list_products`  will display list of **products**. 

After checking the lists now it is time to execute the lunch commend with correct combination.
```
lunch `list_products`-`list_releases`-`list_variants`
```
Here is a sample lunch commend with selected combination.   

**Importent**
```
lunch aosp_cf_x86_64_only_phone-aosp_current-userdebug
```

Now you can execute this to verify the selected combination. But it is just for verification not necessary to execute.
```
echo "$TARGET_PRODUCT-$TARGET_BUILD_VARIANT"
```
Finally you can build using the command `m`.

**Importent**

```
m
```
The `m` command can handle parallel tasks with a `-jN` argument. If you don't provide a `-j` argument, the build system automatically selects a parallel task count that it thinks is optimal for your system.


### Refferance 
https://source.android.com/docs/setup/build/building


### System requirement
 - OS: Ubuntu or MAC
 - RAM: 16GB minimum. Good to have 24GB or 32GB.
 - SWAP memory: Enable swap memory in Ubuntu. Recomended 32GB of swap memory
 - Storage type: SSD. HDD not recomended.
 - Storage space: 500GB space required for AOSP build only. So good to have 1TB SSD.