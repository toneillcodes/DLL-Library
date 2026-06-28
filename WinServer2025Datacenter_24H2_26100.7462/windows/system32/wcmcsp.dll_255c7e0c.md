# Binary Specification: wcmcsp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wcmcsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `255c7e0ce4b7c96f802295bbe7df1d16daa0dbd5ea407b170274e819c4a95820`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EthernetCspDeInit` | `0x59D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EthernetCspInit` | `0x59E0` | 5,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WlanCspDeInit` | `0x6F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WlanCspInit` | `0x6F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WwanCspDeInit` | `0x6F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WwanCspInit` | `0x6F30` | 175,253 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
