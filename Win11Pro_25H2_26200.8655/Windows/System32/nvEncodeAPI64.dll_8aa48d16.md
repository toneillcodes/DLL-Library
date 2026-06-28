# Binary Specification: nvEncodeAPI64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\nvEncodeAPI64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8aa48d16bb99d5597e8732bab2960838d104fde99d75cd52418d2019d932e86a`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NvEncodeAPICreateInstance` | `0x44BE0` | 632 | UnwindData |  |
| 3 | `NvToolCreateInterface` | `0x5F080` | 118 | UnwindData |  |
| 4 | `NvToolDestroyInterface` | `0x5F100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `NvToolGetApiFunctionCount` | `0x5F120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `NvToolGetApiID` | `0x5F130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NvToolGetApiNames` | `0x5F140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `NvToolGetInterface` | `0x5F150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NvToolSetApiID` | `0x5F170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `NvToolSetInterface` | `0x5F180` | 6,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `NvEncodeAPIGetMaxSupportedVersion` | `0x60980` | 102 | UnwindData |  |
