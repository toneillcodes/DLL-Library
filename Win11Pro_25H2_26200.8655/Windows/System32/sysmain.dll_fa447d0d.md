# Binary Specification: sysmain.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sysmain.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fa447d0dfd79fa5a92edd459a61257d73b00f695e19d915ec4e1e3d8db75ef6b`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `OpenReadyBoostPerfData` | `0x6A450` | 269 | UnwindData |  |
| 3 | `AgPdLoad` | `0x6EA00` | 327 | UnwindData |  |
| 5 | `CloseReadyBoostPerfData` | `0x6EED0` | 68,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CollectReadyBoostPerfData` | `0x7FAC0` | 283 | UnwindData |  |
| 16 | `SysMtServiceMain` | `0x7FEE0` | 415 | UnwindData |  |
| 12 | `MI_Main` | `0x800B0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PfSvWsSwapAssessmentTask` | `0x802F0` | 709 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x806C0` | 56 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x80700` | 353 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x80870` | 56 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x808B0` | 49 | UnwindData |  |
| 11 | `GetProviderClassID` | `0x808F0` | 3,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `AgGlLoad` | `0x81660` | 225 | UnwindData |  |
| 4 | `AgTwLoad` | `0x87170` | 316 | UnwindData |  |
| 14 | `PfSvSysprepCleanup` | `0x8AAC0` | 1,208 | UnwindData |  |
| 15 | `PfSvUnattendCallback` | `0x8B080` | 684 | UnwindData |  |
