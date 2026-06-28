# Binary Specification: configmanager2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\configmanager2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `864e831d18a1c33aa502f185dc45b5a413ed2c6c0d3ad9911539f0b691eec9ab`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CmLockSvcInit` | `0x105D0` | 789 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x35D10` | 287 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x3E370` | 5,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CmLockSvcDeinit` | `0x3F910` | 253,580 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
