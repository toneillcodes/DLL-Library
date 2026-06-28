# Binary Specification: wdc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wdc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4cb89720131fde712eab20c9f23b91dc04618f089e96d985574e686487f86e82`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x2D0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x2D0F0` | 205 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x2D2E0` | 246,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x2D2E0` | 246,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WdcParseLegacyFile` | `0x69580` | 201 | UnwindData |  |
| 2 | `WdcRunTaskAsInteractiveUser` | `0x69CD0` | 1,303 | UnwindData |  |
