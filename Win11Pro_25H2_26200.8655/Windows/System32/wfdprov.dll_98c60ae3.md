# Binary Specification: wfdprov.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wfdprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `98c60ae342411ec29adcecd7b9fcb0d28a05438c70ca574de70337552b6853c2`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WFDProvConfigureAndProvisionDevice` | `0x2CF0` | 385 | UnwindData |  |
| 2 | `WFDProvDeinitialize` | `0x2E80` | 45 | UnwindData |  |
| 3 | `WFDProvGetInfo` | `0x2EC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WFDProvInitialize` | `0x2F00` | 50 | UnwindData |  |
