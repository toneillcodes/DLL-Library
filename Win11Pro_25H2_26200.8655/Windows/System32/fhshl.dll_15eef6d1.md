# Binary Specification: fhshl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fhshl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `15eef6d148f477c6d8e4a29fd2baacb5fb282a437504e5414f67b3ec84add649`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CreateSearchBindCtx` | `0x102E0` | 618 | UnwindData |  |
| 5 | `GetBackupPathFromPidl` | `0x105F0` | 372 | UnwindData |  |
| 6 | `ParsePIDL` | `0x10C20` | 196 | UnwindData |  |
| 1 | `CreateCatalog` | `0x12A00` | 548 | UnwindData |  |
| 3 | `CreateVirtualItem` | `0x12F90` | 133 | UnwindData |  |
| 4 | `FreeCatalog` | `0x13020` | 84 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x13880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllGetClassObject` | `0x138A0` | 23 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x139B0` | 716 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x13C90` | 166 | UnwindData |  |
