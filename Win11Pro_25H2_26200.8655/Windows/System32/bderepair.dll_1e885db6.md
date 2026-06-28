# Binary Specification: bderepair.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\bderepair.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1e885db6720f29f2257d4957511e51b7b4769fabe07bf1d16965edf18e755683`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `FveAuthWithClearKey` | `0x2030` | 136 | UnwindData |  |
| 2 | `FveAuthWithKey` | `0x20C0` | 418 | UnwindData |  |
| 3 | `FveAuthWithPassphraseW` | `0x2270` | 366 | UnwindData |  |
| 4 | `FveAuthWithPasswordW` | `0x23F0` | 250 | UnwindData |  |
| 5 | `FveCreateRestoreContext` | `0x24F0` | 195 | UnwindData |  |
| 6 | `FveDecryptData` | `0x25C0` | 237 | UnwindData |  |
| 7 | `FveDestroyRestoreContext` | `0x26C0` | 323 | UnwindData |  |
| 8 | `FveGetConvLogOffset` | `0x2810` | 222 | UnwindData |  |
| 9 | `FveGetInterruptedRangeOffset` | `0x2900` | 272 | UnwindData |  |
| 10 | `FveGetMetadataFromRestoreContext` | `0x2A20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `FveLoadConvLog` | `0x2A60` | 408 | UnwindData |  |
| 12 | `FveRecoverBlock` | `0x2C00` | 478 | UnwindData |  |
| 13 | `FveSupplyInformationBlock` | `0x2DF0` | 562 | UnwindData |  |
| 14 | `FveSupplyKeyPackage` | `0x3030` | 247 | UnwindData |  |
| 15 | `FveSupplyWatermark` | `0x3130` | 228 | UnwindData |  |
