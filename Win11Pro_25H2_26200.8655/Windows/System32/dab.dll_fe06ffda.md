# Binary Specification: dab.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dab.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fe06ffda3f8370a99292ff1eb3a341c29be560d93f9e2c3f2363851561652cac`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DabNotifySessionChange` | `0x1590` | 209 | UnwindData |  |
| 2 | `DabNotifyPowerEvent` | `0xB600` | 3,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DabNotifyTimeChange` | `0xC210` | 8,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DabInitialize` | `0xE1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DabTerminate` | `0xE1D0` | 28,144 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
