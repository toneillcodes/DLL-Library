# Binary Specification: InstallServiceTasks.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\InstallServiceTasks.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3996bfdea364a7a68ceda42d448c7865105fd2601f9ec0c2c438bc62cabe10c2`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ForceAppInUseRestart` | `0xFA50` | 511 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xFF80` | 10,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xFF80` | 10,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x12980` | 77 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x129E0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetSetting` | `0x12BC0` | 179,004 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
