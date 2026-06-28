# Binary Specification: AppVEntSubsystems64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AppVEntSubsystems64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c935e5c408ec6280b10b144518090c853706b538e024745e639919887b139234`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `RequestUnhookedFunctionList` | `0xE330` | 50 | UnwindData |  |
| 1 | `APIExportForDetours` | `0x134C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CurrentThreadIsVirtualized` | `0x134D0` | 189 | UnwindData |  |
| 6 | `IsProcessHooked` | `0x141E0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `VirtualizeCurrentProcess` | `0x14410` | 318 | UnwindData |  |
| 3 | `VirtualizeCurrentThread` | `0x14560` | 95 | UnwindData |  |
