# Binary Specification: msctfui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msctfui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `452891dcb0e69bdde53bdb03f2d33da47e4076eecd86b2f494c8076130d1bbe2`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x28B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x28C0` | 253 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x29D0` | 153 | UnwindData |  |
