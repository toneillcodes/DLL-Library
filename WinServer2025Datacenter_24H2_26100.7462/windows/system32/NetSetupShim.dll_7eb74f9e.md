# Binary Specification: NetSetupShim.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\NetSetupShim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7eb74f9e622867b5e0f37c6e3e2b9e63aaaff86bb4f77b0e5fa27086687bb0e5`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0xFB80` | 333 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x12B50` | 42 | UnwindData |  |
| 6 | `NetSetupShimExecuteInfSection` | `0x2FDF0` | 46 | UnwindData |  |
| 3 | `NetSetupCreateBindingMap` | `0x35220` | 208 | UnwindData |  |
| 4 | `NetSetupExportDatabase` | `0x35300` | 75 | UnwindData |  |
| 5 | `NetSetupResetBindings` | `0x35360` | 381 | UnwindData |  |
