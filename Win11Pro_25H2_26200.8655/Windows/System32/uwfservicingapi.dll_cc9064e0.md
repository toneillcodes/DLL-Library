# Binary Specification: uwfservicingapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\uwfservicingapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cc9064e0f7ccd384c25c3ec976b3c2d59f87028abdf9d794eeffc3076a0a56a9`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetServicingModeState` | `0x2630` | 54 | UnwindData |  |
| 2 | `SetServicingModeState` | `0x2670` | 79 | UnwindData |  |
| 3 | `UwfServicingCleanup` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `UwfServicingInitialize` | `0x3210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `UwfServicingWinUpdateApply` | `0x3220` | 124 | UnwindData |  |
| 6 | `UwfServicingWinupdateCleanup` | `0x32B0` | 148 | UnwindData |  |
| 7 | `UwfServicingWinupdateInitialize` | `0x3350` | 82 | UnwindData |  |
