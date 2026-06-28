# Binary Specification: dciman32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dciman32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `63906959ae0023a6a6a697f81fa330a53f3859bb800576f11a722ea3bbef720e`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DCIBeginAccess` | `0x1960` | 728 | UnwindData |  |
| 2 | `DCICloseProvider` | `0x1C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DCICreateOffscreen` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DCICreateOverlay` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DCIDraw` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DCIEnum` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DCISetClipList` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DCISetDestination` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DCISetSrcDestClip` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DCICreatePrimary` | `0x1C70` | 673 | UnwindData |  |
| 6 | `DCIDestroy` | `0x1F20` | 141 | UnwindData |  |
| 8 | `DCIEndAccess` | `0x1FC0` | 134 | UnwindData |  |
| 10 | `DCIOpenProvider` | `0x2050` | 268 | UnwindData |  |
| 14 | `GetDCRegionData` | `0x2170` | 143 | UnwindData |  |
| 15 | `GetWindowRegionData` | `0x2210` | 120 | UnwindData |  |
| 16 | `WinWatchClose` | `0x2290` | 136 | UnwindData |  |
| 17 | `WinWatchDidStatusChange` | `0x2320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `WinWatchGetClipList` | `0x2330` | 205 | UnwindData |  |
| 19 | `WinWatchNotify` | `0x2410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `WinWatchOpen` | `0x2420` | 125 | UnwindData |  |
