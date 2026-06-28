# Binary Specification: WMIMigrationPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migwiz\dlmanifests\Microsoft-Windows-WMI-Core\WMIMigrationPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `600edde63d118f7517865e559c488b271b9c42d13d30f26709a04e1872436d36`
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
