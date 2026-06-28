# Binary Specification: wcmcsp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wcmcsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f23fefcc14e8de9bc90b3ab72774a69bb99a639d6ee645f10bfef6a9fa56fbc6`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EthernetCspDeInit` | `0x59E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EthernetCspInit` | `0x59F0` | 5,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WlanCspDeInit` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WlanCspInit` | `0x6F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WwanCspDeInit` | `0x6F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WwanCspInit` | `0x6F60` | 167,493 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
