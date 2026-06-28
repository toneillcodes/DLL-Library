# Binary Specification: dnsclientpsprovider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\dnsclientpsprovider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `568eeba0ab7afc126d0a6e2d5288f509e284efcbcef6b5e2d92b49662ba165aa`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x2DD0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x2F00` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2F40` | 113 | UnwindData |  |
| 3 | `DllMain` | `0x2FC0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3020` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3070` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x31F0` | 110,460 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
