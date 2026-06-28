# Binary Specification: Windows.SharedPC.AccountManager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.SharedPC.AccountManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7570c8e15ffc93352ecd1e219e6ebf1375242fde16dd0a472759d388dc0c88d1`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x5FF0` | 32 | UnwindData |  |
| 2 | `ServiceMain` | `0x9BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `StartMaintenance` | `0x9BE0` | 247 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x9CE0` | 118,492 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
