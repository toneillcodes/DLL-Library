# Binary Specification: WMIMigrationPlugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\WMIMigrationPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `04db5356e40159900fd44f1c36a99e564fdc097665bb424a4ea3bcdf328c31f5`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x5FE0` | 42 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x6010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllMain` | `0x6030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllRegisterServer` | `0x6050` | 92 | UnwindData |  |
| 7 | `DllUnregisterServer` | `0x60C0` | 89 | UnwindData |  |
| 1 | `RebuildApply` | `0x9530` | 682 | UnwindData |  |
| 2 | `RebuildGather` | `0x97E0` | 592 | UnwindData |  |
