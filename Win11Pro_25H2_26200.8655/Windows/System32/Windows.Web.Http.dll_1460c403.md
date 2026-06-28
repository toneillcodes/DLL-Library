# Binary Specification: Windows.Web.Http.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Web.Http.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1460c403a528fa2a153bbed62eb1cb54a500102fc589afca01c2a56e3ec54be5`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x5BDC0` | 822 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x62440` | 108 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x63D40` | 136 | UnwindData |  |
| 4 | `DllMain` | `0x7D4E0` | 112 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xC1A60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0xC1A90` | 15,340 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
