# Binary Specification: wci.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wci.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `048084294704e1bb07264e365b01d56308d6cf2e636f1a3a3784020ffeef0d7b`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `WciConfigureFilter` | `0x1F60` | 259 | UnwindData |  |
| 7 | `WciGenerateFilterConfiguration` | `0x2070` | 702 | UnwindData |  |
| 8 | `WciGetUnions` | `0x2340` | 852 | UnwindData |  |
| 1 | `WcAttachFilter` | `0x26B0` | 231 | UnwindData |  |
| 2 | `WcDetachFilter` | `0x2980` | 193 | UnwindData |  |
| 6 | `WciConfigureVolume` | `0x2A50` | 395 | UnwindData |  |
| 10 | `WciRemoveRoot` | `0x2BF0` | 354 | UnwindData |  |
| 14 | `WciSetupFilter` | `0x2D60` | 651 | UnwindData |  |
| 3 | `WcRemoveReparseData` | `0x3A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WcRemoveTombstoneReparseData` | `0x3AC0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `WciReadReparsePointData` | `0x3E50` | 273 | UnwindData |  |
| 11 | `WciSetReparsePointData` | `0x3F70` | 23 | UnwindData |  |
| 12 | `WciSetReparsePointDataEx` | `0x3F90` | 265 | UnwindData |  |
| 13 | `WciSetTombstone` | `0x40A0` | 29 | UnwindData |  |
