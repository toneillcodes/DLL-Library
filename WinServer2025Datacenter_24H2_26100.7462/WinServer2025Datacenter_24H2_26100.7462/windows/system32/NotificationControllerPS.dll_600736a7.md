# Binary Specification: NotificationControllerPS.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\NotificationControllerPS.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `600736a79a973f167612ecba3a894c4100c7d14d8501c29a8395b4229fdec364`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x4360` | 1,219 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x4C20` | 102 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xFE00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xFE30` | 206,780 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
