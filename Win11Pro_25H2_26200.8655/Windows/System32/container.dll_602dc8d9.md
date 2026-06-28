# Binary Specification: container.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\container.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `602dc8d9186a0046893195905fab9193bc193b3a55b9d4a72295784bd952d831`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `?AddRuntimeVirtualKeysToContainer@container@@YAXPEAXKPEAU_WC_VKEY_INFO@@@Z` | `0xD930` | 482 | UnwindData |  |
| 2 | `?CleanupContainer@container@@YAXPEAXPEBG@Z` | `0xDB20` | 267 | UnwindData |  |
| 3 | `?CleanupFilesystemNamespace@container@@YAXPEAXPEBG@Z` | `0xDC40` | 240 | UnwindData |  |
| 4 | `?CreateContainer@container@@YAXPEAXAEBUContainer@Definition@Containers@Schema@@_N@Z` | `0xDD40` | 242 | UnwindData |  |
| 5 | `?GetComRegistryRoot@container@@YAPEAXPEAX@Z` | `0xDFE0` | 24 | UnwindData |  |
| 6 | `?GetContainerIdentifierString@container@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0xE000` | 95 | UnwindData |  |
| 7 | `?GetContainerObjectRootPath@container@@YAXPEAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xE070` | 374 | UnwindData |  |
| 8 | `?GetRegistryRootPath@container@@YAXPEAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV23@@Z` | `0xE1F0` | 123 | UnwindData |  |
| 9 | `?IsContainerQuiescent@container@@YAEPEAX@Z` | `0xE280` | 134 | UnwindData |  |
| 10 | `?IsFirstBoot@container@@YAEPEAX@Z` | `0xE310` | 127 | UnwindData |  |
| 11 | `?LaunchApplicationContainer@container@@YAPEAXPEAXPEBGK@Z` | `0xE3A0` | 941 | UnwindData |  |
| 12 | `?LaunchContainer@container@@YAXPEAX0@Z` | `0xE760` | 1,306 | UnwindData |  |
| 15 | `?SetRegistryFlushState@container@@YAXPEAXE@Z` | `0xF2F0` | 184 | UnwindData |  |
| 16 | `?SetupFilesystemNamespace@container@@YAXPEAXAEBUFilesystemNamespace@Definition@Containers@Schema@@@Z` | `0xF3B0` | 182 | UnwindData |  |
| 17 | `?ShutdownAppContainer@container@@YA_NPEAX@Z` | `0xF470` | 232 | UnwindData |  |
| 19 | `WcAddRuntimeVirtualKeysToContainer` | `0x11C40` | 23 | UnwindData |  |
| 20 | `WcCleanupContainer` | `0x11C60` | 23 | UnwindData |  |
| 21 | `WcCleanupFilesystemNamespace` | `0x11C80` | 23 | UnwindData |  |
| 22 | `WcCreateContainer` | `0x11CA0` | 42 | UnwindData |  |
| 25 | `WcGetComRegistryRoot` | `0x11CD0` | 41 | UnwindData |  |
| 26 | `WcGetContainerIdentifier` | `0x11D00` | 29 | UnwindData |  |
| 27 | `WcGetContainerObjectRootPath` | `0x11D30` | 172 | UnwindData |  |
| 28 | `WcGetContainerRegistryRootPath` | `0x11DF0` | 234 | UnwindData |  |
| 29 | `WcGetContainerServiceSessionId` | `0x11EE0` | 31 | UnwindData |  |
| 30 | `WcIsContainerQuiescent` | `0x11F10` | 31 | UnwindData |  |
| 31 | `WcIsFirstBoot` | `0x11F40` | 31 | UnwindData |  |
| 32 | `WcLaunchApplicationContainer` | `0x11F70` | 32 | UnwindData |  |
| 33 | `WcLaunchContainer` | `0x11FA0` | 23 | UnwindData |  |
| 36 | `WcSetRegistryFlushState` | `0x11FC0` | 23 | UnwindData |  |
| 37 | `WcSetupFilesystemNamespace` | `0x11FE0` | 35 | UnwindData |  |
| 38 | `WcShutdownAppContainer` | `0x12010` | 34 | UnwindData |  |
| 23 | `WcCreateDescriptionFromXml` | `0x22320` | 573 | UnwindData |  |
| 24 | `WcDestroyDescription` | `0x22570` | 38 | UnwindData |  |
| 13 | `?RegisterForContainerTerminationNotification@container@@YAPEAU_WC_CONTAINER_NOTIFICATION@@PEAXP6AX0W4_WC_CONTAINER_TERMINATION_REASON@@PEAU2@0@Z0@Z` | `0x2A870` | 576 | UnwindData |  |
| 14 | `?ReleaseContainerTerminationNotification@container@@YAXPEAU_WC_CONTAINER_NOTIFICATION@@@Z` | `0x2AAC0` | 43 | UnwindData |  |
| 18 | `?WaitForContainerTerminationNotification@container@@YAXPEAU_WC_CONTAINER_NOTIFICATION@@@Z` | `0x2B4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `WcRegisterForContainerTerminationNotification` | `0x2B4F0` | 32 | UnwindData |  |
| 35 | `WcReleaseContainerTerminationNotification` | `0x2B520` | 17 | UnwindData |  |
| 39 | `WcWaitForContainerTerminationNotification` | `0x2B540` | 28 | UnwindData |  |
