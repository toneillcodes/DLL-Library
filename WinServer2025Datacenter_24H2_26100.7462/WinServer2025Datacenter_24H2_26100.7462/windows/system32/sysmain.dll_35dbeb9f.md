# Binary Specification: sysmain.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sysmain.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `35dbeb9f8e7a6d39f961d36927cfb0e3a9d4770c309434c44865c3e21eee5a00`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `OpenReadyBoostPerfData` | `0x6A430` | 269 | UnwindData |  |
| 3 | `AgPdLoad` | `0x6E9E0` | 327 | UnwindData |  |
| 5 | `CloseReadyBoostPerfData` | `0x6EEB0` | 68,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CollectReadyBoostPerfData` | `0x7FB40` | 283 | UnwindData |  |
| 16 | `SysMtServiceMain` | `0x7FF60` | 415 | UnwindData |  |
| 12 | `MI_Main` | `0x80130` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PfSvWsSwapAssessmentTask` | `0x80370` | 709 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x80740` | 56 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x80780` | 353 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x808F0` | 56 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x80930` | 49 | UnwindData |  |
| 11 | `GetProviderClassID` | `0x80970` | 3,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `AgGlLoad` | `0x816E0` | 225 | UnwindData |  |
| 4 | `AgTwLoad` | `0x871F0` | 316 | UnwindData |  |
| 14 | `PfSvSysprepCleanup` | `0x8AB40` | 1,208 | UnwindData |  |
| 15 | `PfSvUnattendCallback` | `0x8B100` | 684 | UnwindData |  |
