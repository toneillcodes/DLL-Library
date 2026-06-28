# Binary Specification: d3d10core.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\d3d10core.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2e2a6445a01b166b4d4e889bc3c2b58d85b64196fe5605bc22b1463d08f42f65`
* **Total Exported Functions:** 40

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `D3DKMTCloseAdapter` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `D3DKMTCreateAllocation` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `D3DKMTCreateContext` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `D3DKMTCreateDevice` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `D3DKMTCreateSynchronizationObject` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `D3DKMTDestroyAllocation` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `D3DKMTDestroyContext` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `D3DKMTDestroyDevice` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `D3DKMTDestroySynchronizationObject` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `D3DKMTEscape` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `D3DKMTGetContextSchedulingPriority` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `D3DKMTGetDisplayModeList` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `D3DKMTGetMultisampleMethodList` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `D3DKMTGetRuntimeData` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `D3DKMTGetSharedPrimaryHandle` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `D3DKMTLock` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `D3DKMTPresent` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `D3DKMTQueryAllocationResidency` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `D3DKMTRender` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `D3DKMTSetAllocationPriority` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `D3DKMTSetContextSchedulingPriority` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `D3DKMTSetDisplayMode` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `D3DKMTSetDisplayPrivateDriverFormat` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `D3DKMTSetGammaRamp` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `D3DKMTSetVidPnSourceOwner` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `D3DKMTSignalSynchronizationObject` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `D3DKMTUnlock` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `D3DKMTWaitForSynchronizationObject` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `D3DKMTWaitForVerticalBlankEvent` | `0x2070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `D3DKMTQueryAdapterInfo` | `0x2080` | 99 | UnwindData |  |
| 12 | `OpenAdapter10` | `0x2140` | 51 | UnwindData |  |
| 13 | `OpenAdapter10_2` | `0x2180` | 51 | UnwindData |  |
| 24 | `D3DKMTGetDeviceState` | `0x21C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `D3DKMTOpenAdapterFromHdc` | `0x2200` | 35 | UnwindData |  |
| 31 | `D3DKMTOpenResource` | `0x2230` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `D3DKMTQueryResourceInfo` | `0x2230` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `D3D10CoreCreateDevice` | `0x2530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `D3D10CoreGetSupportedVersions` | `0x2530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `D3D10CoreRegisterLayers` | `0x2530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `D3D10CoreGetVersion` | `0x2540` | 0 | Indeterminate |  |
