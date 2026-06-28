# Binary Specification: prnfldr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\prnfldr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `34e6ad99d4eb17c1be2262130553caa495594cf4e9bf8bb76894019e3199fd5e`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x5280` | 57 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x55A0` | 56 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1E2D0` | 58,488 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1E2D0` | 58,488 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
