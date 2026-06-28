# Binary Specification: storagewmi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\storagewmi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c39b2f2643fd860622d68113fd523e9e1ede0deb9b6177cc75aa2a23b479fe00`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x4AA0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x4AE0` | 113 | UnwindData |  |
| 3 | `DllMain` | `0x4B60` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4BC0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4C10` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x4D90` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x5210` | 1,248,892 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
