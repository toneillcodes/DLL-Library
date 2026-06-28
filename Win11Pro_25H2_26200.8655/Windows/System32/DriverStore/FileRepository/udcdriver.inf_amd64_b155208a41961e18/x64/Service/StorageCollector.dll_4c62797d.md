# Binary Specification: StorageCollector.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\udcdriver.inf_amd64_b155208a41961e18\x64\Service\StorageCollector.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4c62797d9222e2ee81f10a945769f5f4c7abe40c33b251f094af8c2a185f8dc8`
* **Total Exported Functions:** 152

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 141 | `?getName@HardDiskSmartInfo@StorageCollector@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x28A0` | 30 | UnwindData |  |
| 145 | `?getRaw@HardDiskSmartInfo@StorageCollector@@QEBA_KXZ` | `0x28C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??1HardDiskSmartInfo@StorageCollector@@UEAA@XZ` | `0x28D0` | 110 | UnwindData |  |
| 14 | `??0HardDiskSmartInfo@StorageCollector@@QEAA@AEBV01@@Z` | `0x2940` | 61 | UnwindData |  |
| 50 | `??4HardDiskSmartInfo@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x2980` | 70 | UnwindData |  |
| 59 | `??4StorageDeviceDescriptorData@StorageCollector@@QEAAAEAT01@$$QEAT01@@Z` | `0x2A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??4StorageDeviceDescriptorData@StorageCollector@@QEAAAEAT01@AEBT01@@Z` | `0x2A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0HardDiskBasicInfo@StorageCollector@@QEAA@XZ` | `0x2A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??1HardDiskBasicInfo@StorageCollector@@QEAA@XZ` | `0x2AA0` | 100 | UnwindData |  |
| 9 | `??0HardDiskBasicInfo@StorageCollector@@QEAA@AEBU01@@Z` | `0x2B10` | 59 | UnwindData |  |
| 8 | `??0HardDiskBasicInfo@StorageCollector@@QEAA@$$QEAU01@@Z` | `0x2B50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??4HardDiskBasicInfo@StorageCollector@@QEAAAEAU01@AEBU01@@Z` | `0x2BA0` | 78 | UnwindData |  |
| 44 | `??4HardDiskBasicInfo@StorageCollector@@QEAAAEAU01@$$QEAU01@@Z` | `0x2BF0` | 59 | UnwindData |  |
| 13 | `??0HardDiskInfo@StorageCollector@@QEAA@XZ` | `0x2C30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??1HardDiskInfo@StorageCollector@@QEAA@XZ` | `0x2CA0` | 449 | UnwindData |  |
| 12 | `??0HardDiskInfo@StorageCollector@@QEAA@AEBU01@@Z` | `0x2E70` | 151 | UnwindData |  |
| 11 | `??0HardDiskInfo@StorageCollector@@QEAA@$$QEAU01@@Z` | `0x2F10` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??4HardDiskInfo@StorageCollector@@QEAAAEAU01@AEBU01@@Z` | `0x3060` | 238 | UnwindData |  |
| 46 | `??4HardDiskInfo@StorageCollector@@QEAAAEAU01@$$QEAU01@@Z` | `0x3150` | 143 | UnwindData |  |
| 25 | `??1HardDisk@StorageCollector@@UEAA@XZ` | `0x31E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `?GetNominalMediaRotationRate@HardDisk@StorageCollector@@UEAAGXZ` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `?getStorageBusType@HardDisk@StorageCollector@@QEBA?AW4_STORAGE_BUS_TYPE@@XZ` | `0x3210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `?getProductName@HardDisk@StorageCollector@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x3220` | 30 | UnwindData |  |
| 146 | `?getSerialNumber@HardDisk@StorageCollector@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x3240` | 30 | UnwindData |  |
| 139 | `?getFirmwareVersion@HardDisk@StorageCollector@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x3260` | 30 | UnwindData |  |
| 135 | `?getCapacity@HardDisk@StorageCollector@@QEBA_KXZ` | `0x3280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?getDriveType@HardDisk@StorageCollector@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x3290` | 33 | UnwindData |  |
| 137 | `?getDrivePath@HardDisk@StorageCollector@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x32C0` | 30 | UnwindData |  |
| 136 | `?getDiskNumber@HardDisk@StorageCollector@@QEBAHXZ` | `0x32E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?getNumOfPartitions@HardDisk@StorageCollector@@QEBAHXZ` | `0x32F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `?getPartitionStyle@HardDisk@StorageCollector@@QEBAKXZ` | `0x3300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0HardDisk@StorageCollector@@QEAA@AEBV01@@Z` | `0x3310` | 41 | UnwindData |  |
| 43 | `??4HardDisk@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x3340` | 31 | UnwindData |  |
| 32 | `??4AtaSmart@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??4AtaSmart@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??4AtaSmartMapping@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??4AtaSmartMapping@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??4HardDiskInfoCollector@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??4HardDiskInfoCollector@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??4NVMe@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??4NVMe@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??4NativeMethods@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??4NativeMethods@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `?getSmartSpecialConverter@NVMeSmart@StorageCollector@@QEAAAEAV?$map@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$function@$$A6A_KPEAUNVMeHealthInfoLog@NVMe@StorageCollector@@@Z@2@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$function@$$A6A_KPEAUNVMeHealthInfoLog@NVMe@StorageCollector@@@Z@2@@std@@@2@@std@@XZ` | `0x3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `?__autoclassinit2@AtaHardDisk@Ata@StorageCollector@@QEAAX_K@Z` | `0x3430` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `?__autoclassinit2@NVMeHardDisk@StorageCollector@@QEAAX_K@Z` | `0x3430` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `?__autoclassinit2@NVMeIdentifyMapping@StorageCollector@@QEAAX_K@Z` | `0x3430` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `?__autoclassinit2@NVMeSmart@StorageCollector@@QEAAX_K@Z` | `0x3430` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??4AtaSmartReadLogValue@StorageCollector@@QEAAAEAU01@AEBU01@@Z` | `0x3500` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??4AtaSmartThresholdValue@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x3500` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??4AtaSmartValue@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0x3500` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??4AtaSmartValue@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0x3570` | 2,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??4AtaSmartThresholdValue@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0x3FC0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??4AtaSmartReadLogValue@StorageCollector@@QEAAAEAU01@$$QEAU01@@Z` | `0x42E0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??1AtaSmartInfo@AtaSmart@StorageCollector@@UEAA@XZ` | `0x4730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0AtaSmartInfo@AtaSmart@StorageCollector@@QEAA@AEBV012@@Z` | `0x4740` | 101 | UnwindData |  |
| 34 | `??4AtaSmartInfo@AtaSmart@StorageCollector@@QEAAAEAV012@AEBV012@@Z` | `0x47B0` | 100 | UnwindData |  |
| 1 | `??0AtaHardDisk@Ata@StorageCollector@@QEAA@AEBUHardDiskInfo@2@@Z` | `0x48C0` | 58 | UnwindData |  |
| 23 | `??1AtaHardDisk@Ata@StorageCollector@@UEAA@XZ` | `0x4900` | 65 | UnwindData |  |
| 151 | `?setIdentify@AtaHardDisk@Ata@StorageCollector@@IEAAXV?$unique_ptr@UIdentifyDeviceData@NativeMethods@StorageCollector@@U?$default_delete@UIdentifyDeviceData@NativeMethods@StorageCollector@@@std@@@std@@@Z` | `0x4950` | 86 | UnwindData |  |
| 80 | `?GetDisk@AtaHardDisk@Ata@StorageCollector@@SA?AV?$unique_ptr@VHardDisk@StorageCollector@@U?$default_delete@VHardDisk@StorageCollector@@@std@@@std@@AEBUHardDiskBasicInfo@3@TStorageDeviceDescriptorData@3@@Z` | `0x49B0` | 2,272 | UnwindData |  |
| 111 | `?IsMediaTypeHDD@AtaHardDisk@Ata@StorageCollector@@QEAA_NXZ` | `0x5290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `?GetNominalMediaRotationRate@AtaHardDisk@Ata@StorageCollector@@UEAAGXZ` | `0x52B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `?GetSmartAttributes@AtaHardDisk@Ata@StorageCollector@@UEAAXAEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@std@@@Z` | `0x52D0` | 42 | UnwindData |  |
| 124 | `?RunShortSelfTest@AtaHardDisk@Ata@StorageCollector@@UEAA_NXZ` | `0x5300` | 33 | UnwindData |  |
| 121 | `?RunAndGetShortSelfTestResult@AtaHardDisk@Ata@StorageCollector@@UEAA_NPEAXAEAK@Z` | `0x5330` | 125 | UnwindData |  |
| 88 | `?GetIdentify@AtaHardDisk@Ata@StorageCollector@@SA?AV?$unique_ptr@UIdentifyDeviceData@NativeMethods@StorageCollector@@U?$default_delete@UIdentifyDeviceData@NativeMethods@StorageCollector@@@std@@@std@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@5@@Z` | `0x53B0` | 663 | UnwindData |  |
| 128 | `?SwapBytes@AtaHardDisk@Ata@StorageCollector@@CAXQEAEG@Z` | `0x5650` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?DiskSpecification@AtaHardDisk@Ata@StorageCollector@@UEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x5690` | 879 | UnwindData |  |
| 110 | `?IsLenovoQualifiedAttributesSupported@AtaHardDisk@Ata@StorageCollector@@AEAA_NXZ` | `0x5A00` | 488 | UnwindData |  |
| 3 | `??0AtaSmartInfo@AtaSmart@StorageCollector@@QEAA@H_K000@Z` | `0x6990` | 843 | UnwindData |  |
| 5 | `??0AtaSmartValue@StorageCollector@@QEAA@XZ` | `0x6CE0` | 98 | UnwindData |  |
| 4 | `??0AtaSmartThresholdValue@StorageCollector@@QEAA@XZ` | `0x6D50` | 53 | UnwindData |  |
| 125 | `?RunShortSelfTest@AtaSmart@StorageCollector@@SA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x6D90` | 472 | UnwindData |  |
| 104 | `?GetShortSelfTestResult@AtaSmart@StorageCollector@@SA_NPEAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAK@Z` | `0x6F70` | 668 | UnwindData |  |
| 66 | `?CombineSmartAndThreshold@AtaSmart@StorageCollector@@SAXAEBVAtaSmartValue@2@AEBVAtaSmartThresholdValue@2@AEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@std@@@Z` | `0x7210` | 1,140 | UnwindData |  |
| 127 | `?SendDeviceIoControlCommand@AtaSmart@StorageCollector@@CA_NPEAXIW4Operation@2@0H@Z` | `0x7690` | 251 | UnwindData |  |
| 79 | `?GetDeviceIoControlInParamsFor@AtaSmart@StorageCollector@@CA?AU_SENDCMDINPARAMS@@W4Operation@2@@Z` | `0x7790` | 174 | UnwindData |  |
| 106 | `?GetSmartAttributes@AtaSmart@StorageCollector@@SAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@4@@Z` | `0x7840` | 930 | UnwindData |  |
| 112 | `?IsSmartCapable@AtaSmart@StorageCollector@@SA_NPEAX@Z` | `0x7BF0` | 141 | UnwindData |  |
| 134 | `?ata_get_attr_raw_value@AtaSmart@StorageCollector@@CA_KAEBUAtaSmartAttribute@2@W4ata_attr_raw_format@2@@Z` | `0x7C80` | 432 | UnwindData |  |
| 108 | `?GetSmartReadLog@AtaSmart@StorageCollector@@SA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAUAtaSmartReadLogValue@2@@Z` | `0x7E30` | 645 | UnwindData |  |
| 78 | `?GetAtaReadLogExtQueryParams@AtaSmart@StorageCollector@@CAXPEAUStorageProtocolSpecificQueryWithReadLogExt@2@@Z` | `0x80C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `?GetAtaReadLogExt@AtaSmart@StorageCollector@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV34@@Z` | `0x8100` | 741 | UnwindData |  |
| 6 | `??0HardDisk@StorageCollector@@IEAA@AEBUHardDiskInfo@1@@Z` | `0x8820` | 37 | UnwindData |  |
| 82 | `?GetDriveCapacity@HardDisk@StorageCollector@@SA_KV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x8850` | 398 | UnwindData |  |
| 122 | `?RunAndGetShortSelfTestResult@HardDisk@StorageCollector@@UEAA_NPEAXAEAK@Z` | `0x89E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?DiskSpecification@HardDisk@StorageCollector@@UEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x89F0` | 57 | UnwindData |  |
| 140 | `?getIdentify@NVMeHardDisk@StorageCollector@@QEBAPEAUNVMeIdentifyControllerData@NVMe@2@XZ` | `0x8A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?GetDriveDescriptor@HardDiskInfoCollector@StorageCollector@@CA?ATStorageDeviceDescriptorData@2@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x8A40` | 530 | UnwindData |  |
| 76 | `?GetAllPhysicalDrivePaths@HardDiskInfoCollector@StorageCollector@@SA?AV?$list@UHardDiskBasicInfo@StorageCollector@@V?$allocator@UHardDiskBasicInfo@StorageCollector@@@std@@@std@@XZ` | `0x8C60` | 2,265 | UnwindData |  |
| 85 | `?GetDriveInstance@HardDiskInfoCollector@StorageCollector@@SA?AV?$unique_ptr@VHardDisk@StorageCollector@@U?$default_delete@VHardDisk@StorageCollector@@@std@@@std@@AEBUHardDiskBasicInfo@2@@Z` | `0x95A0` | 471 | UnwindData |  |
| 109 | `?IsDriveTypeHDD@HardDiskInfoCollector@StorageCollector@@SA_NXZ` | `0x9780` | 1,066 | UnwindData |  |
| 15 | `??0HardDiskSmartInfo@StorageCollector@@QEAA@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_K@Z` | `0xA610` | 187 | UnwindData |  |
| 72 | `?CreateDeviceHandle@NativeMethods@StorageCollector@@SAPEAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xA6D0` | 172 | UnwindData |  |
| 31 | `??1NVMeSmart@StorageCollector@@QEAA@XZ` | `0xA900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0NVMeSmart@StorageCollector@@QEAA@AEBV01@@Z` | `0xA910` | 102 | UnwindData |  |
| 20 | `??0NVMeSmart@StorageCollector@@QEAA@$$QEAV01@@Z` | `0xA980` | 94 | UnwindData |  |
| 56 | `??4NVMeSmart@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0xA9E0` | 57 | UnwindData |  |
| 55 | `??4NVMeSmart@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0xAA20` | 68 | UnwindData |  |
| 16 | `??0NVMeHardDisk@StorageCollector@@QEAA@AEBUHardDiskInfo@1@@Z` | `0xAAB0` | 65 | UnwindData |  |
| 29 | `??1NVMeHardDisk@StorageCollector@@UEAA@XZ` | `0xAB00` | 65 | UnwindData |  |
| 152 | `?setIdentify@NVMeHardDisk@StorageCollector@@IEAAXV?$unique_ptr@UNVMeIdentifyControllerData@NVMe@StorageCollector@@U?$default_delete@UNVMeIdentifyControllerData@NVMe@StorageCollector@@@std@@@std@@@Z` | `0xAB50` | 86 | UnwindData |  |
| 81 | `?GetDisk@NVMeHardDisk@StorageCollector@@SA?AV?$unique_ptr@VHardDisk@StorageCollector@@U?$default_delete@VHardDisk@StorageCollector@@@std@@@std@@AEBUHardDiskBasicInfo@2@TStorageDeviceDescriptorData@2@@Z` | `0xABB0` | 2,276 | UnwindData |  |
| 89 | `?GetIdentify@NVMeHardDisk@StorageCollector@@CA?AV?$unique_ptr@UNVMeIdentifyControllerData@NVMe@StorageCollector@@U?$default_delete@UNVMeIdentifyControllerData@NVMe@StorageCollector@@@std@@@std@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@4@@Z` | `0xB4A0` | 645 | UnwindData |  |
| 107 | `?GetSmartAttributes@NVMeHardDisk@StorageCollector@@UEAAXAEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@std@@@Z` | `0xB730` | 510 | UnwindData |  |
| 84 | `?GetDriveIdentificationAttributes@NVMeHardDisk@StorageCollector@@UEAAXAEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@std@@@Z` | `0xB930` | 331 | UnwindData |  |
| 86 | `?GetEnduranceGroupAttributes@NVMeHardDisk@StorageCollector@@UEAAXAEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@std@@@Z` | `0xBA80` | 115 | UnwindData |  |
| 71 | `?ConvertSmartValues@NVMeHardDisk@StorageCollector@@CAXAEAUNVMeHealthInfoLog@NVMe@2@AEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@std@@@Z` | `0xBB00` | 2,191 | UnwindData |  |
| 67 | `?ConvertDriveIdentificationAttributeValues@NVMeHardDisk@StorageCollector@@CAXAEAUNVMeDriveIdentificationLog@NVMe@2@AEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@std@@@Z` | `0xC3B0` | 846 | UnwindData |  |
| 68 | `?ConvertEnduranceGroupAttributeValues@NVMeHardDisk@StorageCollector@@CAXAEAUNVMeEnduranceGroupLog@NVMe@2@AEAV?$list@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@V?$allocator@V?$unique_ptr@VHardDiskSmartInfo@StorageCollector@@U?$default_delete@VHardDiskSmartInfo@StorageCollector@@@std@@@std@@@2@@std@@@Z` | `0xC700` | 389 | UnwindData |  |
| 100 | `?GetNamespaceInfo@NVMeHardDisk@StorageCollector@@QEAAPEAUNVMeIdentifyNamespaceData@NVMe@2@XZ` | `0xC890` | 457 | UnwindData |  |
| 87 | `?GetErrorInfoLog@NVMeHardDisk@StorageCollector@@QEAAPEAUNVMeErrorInfoLog@NVMe@2@XZ` | `0xCA60` | 469 | UnwindData |  |
| 103 | `?GetSelfTestLog@NVMeHardDisk@StorageCollector@@QEAA?AV?$unique_ptr@UNVMeDeviceSelfTestLog@NVMe@StorageCollector@@U?$default_delete@UNVMeDeviceSelfTestLog@NVMe@StorageCollector@@@std@@@std@@XZ` | `0xCC40` | 648 | UnwindData |  |
| 126 | `?RunShortSelfTest@NVMeHardDisk@StorageCollector@@UEAA_NXZ` | `0xCED0` | 463 | UnwindData |  |
| 75 | `?DiskSpecification@NVMeHardDisk@StorageCollector@@UEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xD0A0` | 556 | UnwindData |  |
| 123 | `?RunAndGetShortSelfTestResult@NVMeHardDisk@StorageCollector@@UEAA_NPEAXAEAK@Z` | `0xD2D0` | 371 | UnwindData |  |
| 97 | `?GetNVMeIdentityQueryParams@NVMeHardDisk@StorageCollector@@CAXAEAUStorageProtocolSpecificQueryWithBufferForIdentity@2@@Z` | `0xD450` | 69 | UnwindData |  |
| 95 | `?GetNVMeHealthInfoQueryParams@NVMeHardDisk@StorageCollector@@CAXPEAUStorageProtocolSpecificQueryWithBufferForHealthInfoLog@2@@Z` | `0xD4A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?GetNVMeIdentityNameSpaceQueryParams@NVMeHardDisk@StorageCollector@@CAXPEAUStorageProtocolSpecificQueryWithBufferForIdentityNamespace@2@@Z` | `0xD4E0` | 12 | UnwindData |  |
| 94 | `?GetNVMeErrorInfoQueryParams@NVMeHardDisk@StorageCollector@@CAXPEAUStorageProtocolSpecificQueryWithBufferForErrorInfoLog@2@@Z` | `0xD530` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `?GetNVMeSelfTestLogQueryParams@NVMeHardDisk@StorageCollector@@CAXPEAUStorageProtocolSpecificQueryWithBufferForSelfTestLog@2@@Z` | `0xD560` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?GetNVMeSelfTestQueryParams@NVMeHardDisk@StorageCollector@@CAXIPEAU_STORAGE_PROTOCOL_COMMAND@@@Z` | `0xD590` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?GetNVMeDriveIdentificationLogQueryParams@NVMeHardDisk@StorageCollector@@CAXPEAUStorageProtocolSpecificQueryWithBufferForDriveIdentificationLog@2@@Z` | `0xD5E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `?GetNVMeEnduranceGroupLogQueryParams@NVMeHardDisk@StorageCollector@@CAXPEAUStorageProtocolSpecificQueryWithBufferForEnduranceGroupLog@2@@Z` | `0xD620` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `?GetNVMeDriveIdentificationLog@NVMeHardDisk@StorageCollector@@EEAA_NAEAUNVMeDriveIdentificationLog@NVMe@2@@Z` | `0xD660` | 536 | UnwindData |  |
| 92 | `?GetNVMeEnduranceGroupLog@NVMeHardDisk@StorageCollector@@EEAA_NAEAUNVMeEnduranceGroupLog@NVMe@2@@Z` | `0xD880` | 563 | UnwindData |  |
| 30 | `??1NVMeIdentifyMapping@StorageCollector@@QEAA@XZ` | `0xE450` | 43 | UnwindData |  |
| 18 | `??0NVMeIdentifyMapping@StorageCollector@@QEAA@AEBV01@@Z` | `0xE480` | 244 | UnwindData |  |
| 17 | `??0NVMeIdentifyMapping@StorageCollector@@QEAA@$$QEAV01@@Z` | `0xE580` | 241 | UnwindData |  |
| 54 | `??4NVMeIdentifyMapping@StorageCollector@@QEAAAEAV01@AEBV01@@Z` | `0xE680` | 153 | UnwindData |  |
| 53 | `??4NVMeIdentifyMapping@StorageCollector@@QEAAAEAV01@$$QEAV01@@Z` | `0xE720` | 188 | UnwindData |  |
| 19 | `??0NVMeIdentifyMapping@StorageCollector@@QEAA@XZ` | `0xE7F0` | 188 | UnwindData |  |
| 149 | `?initIdentifyConverter@NVMeIdentifyMapping@StorageCollector@@AEAAXXZ` | `0xE8B0` | 7,259 | UnwindData |  |
| 150 | `?initNameSpaceConverter@NVMeIdentifyMapping@StorageCollector@@AEAAXXZ` | `0x10510` | 4,700 | UnwindData |  |
| 69 | `?ConvertIdentify@NVMeIdentifyMapping@StorageCollector@@QEAA_KPEAUNVMeIdentifyControllerData@NVMe@2@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x11770` | 311 | UnwindData |  |
| 70 | `?ConvertIdentify@NVMeIdentifyMapping@StorageCollector@@QEAA_KPEAUNVMeIdentifyNamespaceData@NVMe@2@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x118B0` | 315 | UnwindData |  |
| 22 | `??0NVMeSmart@StorageCollector@@QEAA@XZ` | `0x134B0` | 4,867 | UnwindData |  |
| 119 | `?NumberAtaSmartAttributes@AtaSmartThresholdValue@StorageCollector@@0HB` | `0x1AAB4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?NumberAtaSmartAttributes@AtaSmartValue@StorageCollector@@0HB` | `0x1AAB4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??_7HardDisk@StorageCollector@@6B@` | `0x1AAC0` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??_7HardDiskSmartInfo@StorageCollector@@6B@` | `0x1AAF8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??_7AtaSmartInfo@AtaSmart@StorageCollector@@6B@` | `0x1AB08` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??_7AtaHardDisk@Ata@StorageCollector@@6B@` | `0x1AB18` | 7,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `?NVMeMaxLogSize@NVMe@StorageCollector@@2HB` | `0x1C868` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `?NVMeNamespaceAll@NVMe@StorageCollector@@2IB` | `0x1C86C` | 188 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??_7NVMeHardDisk@StorageCollector@@6B@` | `0x1C928` | 63,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `?LENOVO_NOT_QUALIFIED_SPEC@HardDisk@StorageCollector@@2V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@B` | `0x2C040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?LENOVO_QUALIFIED_SPEC@HardDisk@StorageCollector@@2V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@B` | `0x2C060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?KelvinToCelsius@NVMeSmart@StorageCollector@@2V?$function@$$A6AIG@Z@std@@A` | `0x2C080` | 24,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `?_mapLenovoQualifiedSmartAttributes@AtaHardDisk@Ata@StorageCollector@@0V?$map@HV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@U?$less@H@2@V?$allocator@U?$pair@$$CBHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@std@@@2@@std@@A` | `0x32158` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?Mapping@AtaSmartMapping@StorageCollector@@2V?$map@HV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@U?$less@H@2@V?$allocator@U?$pair@$$CBHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@std@@@2@@std@@A` | `0x32168` | 0 | Indeterminate |  |
