# Binary Specification: bindfltapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\bindfltapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `84ba384781c302dae5369f8ceb16dee5d47a88852e8fd686ec04128da6c07bdf`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `BfConfigureFilter` | `0x2AF0` | 220 | UnwindData |  |
| 3 | `BfGenerateBatchedConfig` | `0x2BE0` | 807 | UnwindData |  |
| 4 | `BfGenerateMappingConfiguration` | `0x2F10` | 1,028 | UnwindData |  |
| 5 | `BfGetMappings` | `0x3320` | 838 | UnwindData |  |
| 7 | `BfRemoveMappingEx` | `0x3670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `BfSetupFilterBatched` | `0x3680` | 742 | UnwindData |  |
| 10 | `BfSetupFilterEx` | `0x3970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `BfTrackWritesFromSilo` | `0x3980` | 400 | UnwindData |  |
| 12 | `CreateBindLink` | `0x204D0` | 163 | UnwindData |  |
| 13 | `RemoveBindLink` | `0x20580` | 111 | UnwindData |  |
| 1 | `BfAttachFilter` | `0x22DB0` | 301 | UnwindData |  |
| 6 | `BfRemoveMapping` | `0x23BC0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `BfSetupFilter` | `0x23E40` | 53 | UnwindData |  |
