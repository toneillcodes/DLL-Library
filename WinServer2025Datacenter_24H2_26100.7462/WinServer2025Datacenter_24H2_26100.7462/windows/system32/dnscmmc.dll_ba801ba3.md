# Binary Specification: dnscmmc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dnscmmc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ba801ba33665b302b95f6449b9542f23c186ec544d1416c387dc3097a51a4138`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0xBB90` | 290 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0xBCB8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xBCD8` | 13,864 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xBCD8` | 13,864 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
