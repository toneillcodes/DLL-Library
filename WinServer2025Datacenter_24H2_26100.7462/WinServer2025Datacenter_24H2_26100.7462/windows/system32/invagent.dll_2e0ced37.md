# Binary Specification: invagent.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\invagent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2e0ced374e0cc8d4a36fb2a6a52167a7de6fe932935aa6670138ca46ffe9a7e5`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetDetailedAppInventoryReport` | `0x14630` | 1,613 | UnwindData |  |
| 2 | `GetFileSigningInfoTC` | `0x14C90` | 1,055 | UnwindData |  |
| 3 | `RunUpdate` | `0x1A330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `RunUpdateTC` | `0x1A340` | 969 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x1F7F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetClassObject` | `0x1F820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0x1F830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllUnregisterServer` | `0x1F840` | 808,042 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
