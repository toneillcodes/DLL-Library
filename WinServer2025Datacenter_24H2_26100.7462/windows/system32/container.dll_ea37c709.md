# Binary Specification: container.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\container.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ea37c709af00050c357a7379d8f7dd8aeaa4ebc9f42cdedd15e0f7fc5305743a`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `?AddRuntimeVirtualKeysToContainer@container@@YAXPEAXKPEAU_WC_VKEY_INFO@@@Z` | `0xD900` | 482 | UnwindData |  |
| 2 | `?CleanupContainer@container@@YAXPEAXPEBG@Z` | `0xDAF0` | 267 | UnwindData |  |
| 3 | `?CleanupFilesystemNamespace@container@@YAXPEAXPEBG@Z` | `0xDC10` | 240 | UnwindData |  |
| 4 | `?CreateContainer@container@@YAXPEAXAEBUContainer@Definition@Containers@Schema@@_N@Z` | `0xDD10` | 242 | UnwindData |  |
| 5 | `?GetComRegistryRoot@container@@YAPEAXPEAX@Z` | `0xDFB0` | 24 | UnwindData |  |
| 6 | `?GetContainerIdentifierString@container@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0xDFD0` | 95 | UnwindData |  |
| 7 | `?GetContainerObjectRootPath@container@@YAXPEAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xE040` | 374 | UnwindData |  |
| 8 | `?GetRegistryRootPath@container@@YAXPEAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV23@@Z` | `0xE1C0` | 123 | UnwindData |  |
| 9 | `?IsContainerQuiescent@container@@YAEPEAX@Z` | `0xE250` | 134 | UnwindData |  |
| 10 | `?IsFirstBoot@container@@YAEPEAX@Z` | `0xE2E0` | 127 | UnwindData |  |
| 11 | `?LaunchApplicationContainer@container@@YAPEAXPEAXPEBGK@Z` | `0xE370` | 941 | UnwindData |  |
| 12 | `?LaunchContainer@container@@YAXPEAX0@Z` | `0xE730` | 1,306 | UnwindData |  |
| 15 | `?SetRegistryFlushState@container@@YAXPEAXE@Z` | `0xF2C0` | 184 | UnwindData |  |
| 16 | `?SetupFilesystemNamespace@container@@YAXPEAXAEBUFilesystemNamespace@Definition@Containers@Schema@@@Z` | `0xF380` | 182 | UnwindData |  |
| 17 | `?ShutdownAppContainer@container@@YA_NPEAX@Z` | `0xF440` | 232 | UnwindData |  |
| 19 | `WcAddRuntimeVirtualKeysToContainer` | `0x11C10` | 23 | UnwindData |  |
| 20 | `WcCleanupContainer` | `0x11C30` | 23 | UnwindData |  |
| 21 | `WcCleanupFilesystemNamespace` | `0x11C50` | 23 | UnwindData |  |
| 22 | `WcCreateContainer` | `0x11C70` | 42 | UnwindData |  |
| 25 | `WcGetComRegistryRoot` | `0x11CA0` | 41 | UnwindData |  |
| 26 | `WcGetContainerIdentifier` | `0x11CD0` | 29 | UnwindData |  |
| 27 | `WcGetContainerObjectRootPath` | `0x11D00` | 172 | UnwindData |  |
| 28 | `WcGetContainerRegistryRootPath` | `0x11DC0` | 234 | UnwindData |  |
| 29 | `WcGetContainerServiceSessionId` | `0x11EB0` | 31 | UnwindData |  |
| 30 | `WcIsContainerQuiescent` | `0x11EE0` | 31 | UnwindData |  |
| 31 | `WcIsFirstBoot` | `0x11F10` | 31 | UnwindData |  |
| 32 | `WcLaunchApplicationContainer` | `0x11F40` | 32 | UnwindData |  |
| 33 | `WcLaunchContainer` | `0x11F70` | 23 | UnwindData |  |
| 36 | `WcSetRegistryFlushState` | `0x11F90` | 23 | UnwindData |  |
| 37 | `WcSetupFilesystemNamespace` | `0x11FB0` | 35 | UnwindData |  |
| 38 | `WcShutdownAppContainer` | `0x11FE0` | 34 | UnwindData |  |
| 23 | `WcCreateDescriptionFromXml` | `0x222F0` | 573 | UnwindData |  |
| 24 | `WcDestroyDescription` | `0x22540` | 38 | UnwindData |  |
| 13 | `?RegisterForContainerTerminationNotification@container@@YAPEAU_WC_CONTAINER_NOTIFICATION@@PEAXP6AX0W4_WC_CONTAINER_TERMINATION_REASON@@PEAU2@0@Z0@Z` | `0x2A840` | 576 | UnwindData |  |
| 14 | `?ReleaseContainerTerminationNotification@container@@YAXPEAU_WC_CONTAINER_NOTIFICATION@@@Z` | `0x2AA90` | 43 | UnwindData |  |
| 18 | `?WaitForContainerTerminationNotification@container@@YAXPEAU_WC_CONTAINER_NOTIFICATION@@@Z` | `0x2B4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `WcRegisterForContainerTerminationNotification` | `0x2B4C0` | 32 | UnwindData |  |
| 35 | `WcReleaseContainerTerminationNotification` | `0x2B4F0` | 17 | UnwindData |  |
| 39 | `WcWaitForContainerTerminationNotification` | `0x2B510` | 28 | UnwindData |  |
