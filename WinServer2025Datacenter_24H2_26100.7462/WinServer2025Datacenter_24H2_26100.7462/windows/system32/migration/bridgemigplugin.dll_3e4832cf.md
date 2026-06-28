# Binary Specification: bridgemigplugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\bridgemigplugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3e4832cf7e838ff3b51c96ad4792a3382e93e17f3bb63db697ed0f9add773a55`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x5D10` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x5D40` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x5E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x5EA0` | 301 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x5FE0` | 162 | UnwindData |  |
