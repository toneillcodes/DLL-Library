# Binary Specification: bcd.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\bcd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3bc87d5759db46fdfc8d1a33b6d409b9dffb79d3f4e348f66543ecdd25e4fb50`
* **Total Exported Functions:** 75

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `BcdDeleteElement` | `0x12F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `BcdEnumerateAndUnpackElements` | `0x1300` | 468 | UnwindData |  |
| 13 | `BcdEnumerateElementTypes` | `0x14E0` | 585 | UnwindData |  |
| 14 | `BcdEnumerateElements` | `0x1730` | 40 | UnwindData |  |
| 15 | `BcdEnumerateElementsWithFlags` | `0x1760` | 44 | UnwindData |  |
| 21 | `BcdGetElementData` | `0x17A0` | 26 | UnwindData |  |
| 22 | `BcdGetElementDataWithFlags` | `0x17C0` | 736 | UnwindData |  |
| 33 | `BcdSetElementData` | `0x1AB0` | 26 | UnwindData |  |
| 34 | `BcdSetElementDataWithFlags` | `0x1AD0` | 735 | UnwindData |  |
| 35 | `BcdSetLogging` | `0x7A80` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `BcdCloseObject` | `0x7B90` | 56 | UnwindData |  |
| 6 | `BcdCreateObject` | `0x7BD0` | 168 | UnwindData |  |
| 9 | `BcdDeleteObject` | `0x7C80` | 86 | UnwindData |  |
| 16 | `BcdEnumerateObjects` | `0x7CE0` | 737 | UnwindData |  |
| 28 | `BcdOpenObject` | `0x7FD0` | 511 | UnwindData |  |
| 32 | `BcdQueryObject` | `0x81E0` | 155 | UnwindData |  |
| 2 | `BcdCloseStore` | `0x88C0` | 173 | UnwindData |  |
| 7 | `BcdCreateStore` | `0x8980` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `BcdDeleteObjectReferences` | `0x8CC0` | 507 | UnwindData |  |
| 11 | `BcdDeleteSystemStore` | `0x8ED0` | 610 | UnwindData |  |
| 19 | `BcdFlushStore` | `0x9140` | 109 | UnwindData |  |
| 20 | `BcdForciblyUnloadStore` | `0x91C0` | 199 | UnwindData |  |
| 26 | `BcdMarkAsSystemStore` | `0x9290` | 107 | UnwindData |  |
| 29 | `BcdOpenStore` | `0x9310` | 593 | UnwindData |  |
| 30 | `BcdOpenStoreFromFile` | `0x9570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `BcdOpenSystemStore` | `0x9590` | 101 | UnwindData |  |
| 36 | `BcdSetSystemStoreDevice` | `0x9600` | 470 | UnwindData |  |
| 3 | `BcdCopyObject` | `0xB720` | 31 | UnwindData |  |
| 4 | `BcdCopyObjectEx` | `0xB750` | 2,000 | UnwindData |  |
| 5 | `BcdCopyObjects` | `0xBF30` | 443 | UnwindData |  |
| 17 | `BcdExportStore` | `0xC100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `BcdExportStoreEx` | `0xC120` | 463 | UnwindData |  |
| 24 | `BcdImportStore` | `0xC300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `BcdImportStoreWithFlags` | `0xC310` | 134 | UnwindData |  |
| 27 | `BcdMigrateObjectElementValues` | `0xC3A0` | 361 | UnwindData |  |
| 23 | `BcdGetSystemStorePath` | `0x10CB0` | 640 | UnwindData |  |
| 69 | `SyspartDirectGetSystemDisk` | `0x13830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `SyspartDirectGetSystemPartition` | `0x13850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `SyspartDirectSetSystemDevice` | `0x13870` | 49 | UnwindData |  |
| 72 | `SyspartGetPhysicalPartitions` | `0x13920` | 543 | UnwindData |  |
| 73 | `SyspartGetSystemDisk` | `0x13B50` | 274 | UnwindData |  |
| 74 | `SyspartGetSystemPartition` | `0x13C70` | 101 | UnwindData |  |
| 75 | `SyspartIsSpace` | `0x13CE0` | 109 | UnwindData |  |
| 43 | `GUID_FIRMWARE_BOOTMGR` | `0x197B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `GUID_RESUME_LOADER_SETTINGS_GROUP` | `0x197C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `GUID_WINDOWS_MEMORY_TESTER` | `0x197D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `PARTITION_SYSTEM_GUID` | `0x197E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `GUID_BOOT_LOADER_SETTINGS_GROUP` | `0x197F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `GUID_WINDOWS_BOOTMGR` | `0x19800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `GUID_WINDOWS_LEGACY_NTLDR` | `0x19810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `GUID_WINDOWS_RESUME_TARGET_TEMPLATE_EFI` | `0x19820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `PARTITION_LDM_DATA_GUID` | `0x19830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `GUID_DEBUGGER_SETTINGS_GROUP` | `0x19840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `GUID_WINDOWS_RESUME_TARGET_TEMPLATE_PCAT` | `0x19850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `PARTITION_BASIC_DATA_GUID` | `0x19860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `GUID_WINDOWS_SETUP_PCAT` | `0x19870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `GUID_WINDOWS_SETUP_EFI` | `0x19880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `PARTITION_SPACES_GUID` | `0x19890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `GUID_WINDOWS_OS_TARGET_TEMPLATE_PCAT` | `0x198A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `PARTITION_ENTRY_UNUSED_GUID` | `0x198B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `GUID_EMS_SETTINGS_GROUP` | `0x198C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `PARTITION_MSFT_RESERVED_GUID` | `0x198D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `PARTITION_MSFT_RECOVERY_GUID` | `0x198E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `PARTITION_LDM_METADATA_GUID` | `0x198F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `GUID_HYPERVISOR_SETTINGS_GROUP` | `0x19900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `GUID_GLOBAL_SETTINGS_GROUP` | `0x19910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `GUID_KERNEL_DEBUGGER_SETTINGS_GROUP` | `0x19920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `GUID_CURRENT_BOOT_ENTRY` | `0x19930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `GUID_BAD_MEMORY_GROUP` | `0x19940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `GUID_WINDOWS_OS_TARGET_TEMPLATE_EFI` | `0x19950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `GUID_WINDOWS_SETUP_RAMDISK_OPTIONS` | `0x19970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `PARTITION_CLUSTER_GUID` | `0x19980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `GUID_DEFAULT_BOOT_ENTRY` | `0x19990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `PARTITION_MSFT_SNAPSHOT_GUID` | `0x199B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `GUID_VHD_BOOT_OPTIONS` | `0x199C0` | 0 | Indeterminate |  |
