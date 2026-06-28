# Binary Specification: pcaui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pcaui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4ba1c0204026df45f167dbaf9b516e890251fda8d15f1ab5f6c18d30985a1037`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `PcaShowDialog` | `0x214E0` | 97 | UnwindData |  |
| 1 | `DisplayApphelpDialog` | `0x23C20` | 62 | UnwindData |  |
| 2 | `PcaLaunchApplicationWithConsent` | `0x23C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PcaPersistSettingsAndLaunchApplication` | `0x23C80` | 281 | UnwindData |  |
