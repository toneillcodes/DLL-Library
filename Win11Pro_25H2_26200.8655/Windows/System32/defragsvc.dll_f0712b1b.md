# Binary Specification: defragsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\defragsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f0712b1bc058fa579aec8016db92f2812f50f947566959f69001173dffaff30d`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3FFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x3FFE0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x401F0` | 131 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x40280` | 98 | UnwindData |  |
| 5 | `ServiceMain` | `0x40410` | 172,604 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
