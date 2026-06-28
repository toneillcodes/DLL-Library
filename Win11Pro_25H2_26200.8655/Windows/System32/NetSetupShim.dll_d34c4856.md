# Binary Specification: NetSetupShim.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\NetSetupShim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d34c485643ca13c37e55a172a6563e4d6ddb3a9442ffb25b42867192e209eb20`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0xFBA0` | 333 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x12B70` | 42 | UnwindData |  |
| 6 | `NetSetupShimExecuteInfSection` | `0x2FF30` | 46 | UnwindData |  |
| 3 | `NetSetupCreateBindingMap` | `0x35360` | 208 | UnwindData |  |
| 4 | `NetSetupExportDatabase` | `0x35440` | 75 | UnwindData |  |
| 5 | `NetSetupResetBindings` | `0x354A0` | 381 | UnwindData |  |
