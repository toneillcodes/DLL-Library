# Binary Specification: Storprop.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Storprop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `04b2a67ae969f68395ab330294400514ef91af7fe53453179a67bdc06c1c68b1`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CdromDisableDigitalPlayback` | `0x1A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CdromEnableDigitalPlayback` | `0x1A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CdromIsDigitalPlaybackEnabled` | `0x1A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CdromKnownGoodDigitalPlayback` | `0x1A40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DiskClassInstaller` | `0x1F60` | 89 | UnwindData |  |
| 8 | `DiskPropPageProvider` | `0x27E0` | 997 | UnwindData |  |
| 6 | `CdromSetDefaultDvdRegion` | `0x4360` | 146 | UnwindData |  |
| 9 | `DvdClassInstaller` | `0x46F0` | 169 | UnwindData |  |
| 11 | `DvdPropPageProvider` | `0x4D30` | 604 | UnwindData |  |
| 10 | `DvdLauncher` | `0x5280` | 1,405 | UnwindData |  |
| 1 | `AtaPropPageProvider` | `0x6AE0` | 291 | UnwindData |  |
| 12 | `HdcCoInstaller` | `0x6C10` | 203 | UnwindData |  |
