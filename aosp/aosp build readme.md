## AOSP Build
Once you have download the repo successfully using repo sync.   
Now, To build aosp follow below commends.   
```
cd aosp15
source build/envsetup.sh
```
Next you can optionally execute next 4 commands to get to know the lunch command info:
 - Execute `lunch --help` to get more lunch info. If you are building first time then it is good to have some more info.

 - Now the first command `list_products`, it will display list of **products**. It will take couple of seconds to display the huge list. Choose your option from the list and run with the next commend.

Output:
```
aosp_64bitonly_x86_64
aosp_arm
aosp_arm64
aosp_arm64_fullmte
aosp_arm64_plus_armv7
aosp_cf_arm64_auto
aosp_cf_arm64_minidroid
aosp_cf_arm64_only_phone
aosp_cf_arm64_only_phone_hwasan
aosp_cf_arm64_only_phone_vendor
aosp_cf_arm64_phone
aosp_cf_arm64_phone_fullmte
aosp_cf_arm64_phone_hwasan
aosp_cf_arm64_phone_pgagnostic
aosp_cf_arm64_phone_vendor
aosp_cf_arm64_slim
aosp_cf_arm_minidroid
aosp_cf_riscv64_minidroid
aosp_cf_riscv64_phone
aosp_cf_riscv64_slim
aosp_cf_riscv64_wear
aosp_cf_x86_64_auto
aosp_cf_x86_64_auto_dd
aosp_cf_x86_64_auto_dewd
aosp_cf_x86_64_auto_md
aosp_cf_x86_64_auto_mdnd
aosp_cf_x86_64_auto_portrait
aosp_cf_x86_64_foldable
aosp_cf_x86_64_host
aosp_cf_x86_64_minidroid
aosp_cf_x86_64_only_phone
aosp_cf_x86_64_only_phone_hsum
aosp_cf_x86_64_pc
aosp_cf_x86_64_phone
aosp_cf_x86_64_phone_pgagnostic
aosp_cf_x86_64_phone_soong_system
aosp_cf_x86_64_phone_vendor
aosp_cf_x86_64_slim
aosp_cf_x86_64_ssi
aosp_cf_x86_64_tv
aosp_cf_x86_64_wear
aosp_cf_x86_go_phone
aosp_cf_x86_tv
aosp_cf_x86_wear
aosp_cheetah_car
aosp_husky_car
aosp_panther_car
aosp_riscv64
aosp_tangorpro_car
aosp_trout_arm64
aosp_trout_x86_64
aosp_tv_arm64
aosp_tv_x86
aosp_x86
aosp_x86_64
aosp_x86_arm
arm_krait
arm_v7_v8
armv8
armv8_cortex_a55
armv8_kryo385
csi_arm
csi_arm64
csi_x86
csi_x86_64
db845c
db845c_mini
full
full_x86
generic
generic_system_arm64
generic_system_x86
generic_system_x86_64
generic_system_x86_arm
generic_x86
gsi_arm
gsi_arm64
gsi_car_arm64
gsi_car_x86_64
gsi_tv_arm
gsi_tv_arm64
gsi_x86
gsi_x86_64
hikey
hikey32
hikey64_only
hikey960
hikey960_tv
hikey_tv
linaro_swr
linux_bionic
mainline_sdk
mainline_system_arm64
mainline_system_x86
mainline_system_x86_64
mainline_system_x86_arm
mgsi_arm
mgsi_arm64
mgsi_x86
mgsi_x86_64
mini_arm64
mini_armv7a_neon
mini_x86
mini_x86_64
module_arm
module_arm64
module_arm64only
module_riscv64
module_x86
module_x86_64
module_x86_64only
ndk
qemu_trusty_arm64
riscv64
sdk
sdk_atv64_arm64
sdk_atv_x86
sdk_car_arm64
sdk_car_cw_x86_64
sdk_car_dewd_x86_64
sdk_car_md_arm64
sdk_car_md_x86_64
sdk_car_x86_64
sdk_phone16k_arm64
sdk_phone16k_x86_64
sdk_phone64_arm64
sdk_phone64_arm64_minigbm
sdk_phone64_arm64_riscv64
sdk_phone64_x86_64
sdk_phone64_x86_64_minigbm
sdk_phone64_x86_64_riscv64
sdk_slim_arm64
sdk_slim_x86_64
sdk_tablet_arm64
sdk_tablet_x86_64
sdk_with_runtime_apis
silvermont
sm8x50
trout_arm64_ds
yukawa
```
 - Next the `list_releases [you_selected_product]` command will display list of **releases**.

Output:
```
aosp_current
ap2a
ap3a
ap4a
bp1a
bp2a
bp3a
trunk_staging
```
 - Then the last `list_variants` command will display list of **variants**. 

Output:
```
user
userdebug
eng
```
 

After checking the lists now it is time to execute the lunch commend with correct combination. Here is the syntax of an lunch command `lunch [list_products]-[list_releases]-[list_variants]`

Here is a sample lunch commend with selected combination.   
```
lunch aosp_cf_x86_64_only_phone-aosp_current-userdebug
```

Now you can execute this `echo "$TARGET_PRODUCT-$TARGET_BUILD_VARIANT"` to verify the selected combination. But it is just for verification not necessary to execute.

Finally you can build using the command `m`.
```
m
```
The `m` command can handle parallel tasks with a `-jN` argument. If you don't provide a `-j` argument, the build system automatically selects a parallel task count that it thinks is optimal for your system.
```
m -j1
```

## Final Output
After complete the build successfully a `super.img` file will be generated in this path `../aosp15/out/target/product/vsoc_x86_64_only/super.img`


### Reference 
https://source.android.com/docs/setup/build/building


### System requirement
 - OS: Ubuntu or MAC
 - RAM: 16GB minimum. Good to have 24GB or 32GB.
 - SWAP memory: Enable swap memory in Ubuntu. Recommended 32GB of swap memory
 - Storage type: SSD. HDD not recommended.
 - Storage space: 500GB space required for AOSP build only. So good to have 1TB SSD.
