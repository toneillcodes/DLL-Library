# Binary Specification: Windows.SharedPC.AccountManager.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.SharedPC.AccountManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5db8395800836ee7af878944d84574bdd08a29374807fb2236865288a8b61fbc`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x5FA0` | 32 | UnwindData |  |
| 2 | `ServiceMain` | `0x9B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `StartMaintenance` | `0x9BA0` | 247 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x9CA0` | 110,572 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
