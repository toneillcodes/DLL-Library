# Binary Specification: AppVEntSubsystems64.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppVEntSubsystems64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `323d26ef2271abe42517e0169b98dc0e26f2a59cf1cfc7f0fdc2905f11a43f5c`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `RequestUnhookedFunctionList` | `0xE320` | 50 | UnwindData |  |
| 1 | `APIExportForDetours` | `0x134B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CurrentThreadIsVirtualized` | `0x134C0` | 189 | UnwindData |  |
| 6 | `IsProcessHooked` | `0x141D0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `VirtualizeCurrentProcess` | `0x14400` | 318 | UnwindData |  |
| 3 | `VirtualizeCurrentThread` | `0x14550` | 95 | UnwindData |  |
