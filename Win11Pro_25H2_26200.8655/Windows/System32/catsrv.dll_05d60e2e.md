# Binary Specification: catsrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\catsrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `05d60e2ec24cb27493912b78d8e0570018ccc094ef4337e1c1c25c9d45f3398a`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllGetClassObject` | `0x5DE0` | 133 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x6680` | 105 | UnwindData |  |
| 4 | `?GetReadICR@@YAJHPEAPEAUIComponentRecords@@@Z` | `0x9300` | 45 | UnwindData |  |
| 6 | `OpenComponentLibraryTS` | `0x9CC0` | 106 | UnwindData |  |
| 1 | `?CancelWriteICR@@YAJPEAPEAUIComponentRecords@@@Z` | `0xDF40` | 2,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `?GetWriteICR@@YAJPEAPEAUIComponentRecords@@@Z` | `0xE860` | 6,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?ReleaseReadICR@@YAXPEAPEAUIComponentRecords@@@Z` | `0x100C0` | 44 | UnwindData |  |
| 8 | `?SaveWriteICR@@YAJPEAPEAUIComponentRecords@@@Z` | `0x10150` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllRegisterServer` | `0x10850` | 70 | UnwindData |  |
| 12 | `DllUnregisterServer` | `0x108A0` | 136 | UnwindData |  |
| 13 | `GetAppImport` | `0x10930` | 127 | UnwindData |  |
| 2 | `CreateComponentLibraryTS` | `0x2B7D0` | 106 | UnwindData |  |
| 3 | `GetCatalogCRMClerk` | `0x2B990` | 46 | UnwindData |  |
