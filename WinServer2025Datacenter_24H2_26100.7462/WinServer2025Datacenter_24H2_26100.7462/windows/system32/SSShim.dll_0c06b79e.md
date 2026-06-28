# Binary Specification: SSShim.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SSShim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0c06b79eca55332bc5534970249c393de5d3e8c97e36e9422ee7d79e4ee9a0f0`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SssBindServicingStack` | `0x3760` | 5,588 | UnwindData |  |
| 2 | `SssGetServicingStackFilePath` | `0x4D40` | 800 | UnwindData |  |
| 3 | `SssGetServicingStackFilePathLength` | `0x5070` | 519 | UnwindData |  |
| 4 | `SssGetServicingStackVersion` | `0x5280` | 389 | UnwindData |  |
| 5 | `SssPreloadDownlevelDependencies` | `0x5410` | 2,218 | UnwindData |  |
| 6 | `SssReleaseServicingStack` | `0x5CC0` | 164 | UnwindData |  |
