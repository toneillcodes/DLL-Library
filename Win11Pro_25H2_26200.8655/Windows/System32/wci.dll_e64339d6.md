# Binary Specification: wci.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wci.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e64339d6573a06b2f7a9d70a17ec5c34fb576f3acc8c313d4e3cddfdaa1e4ef1`
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
