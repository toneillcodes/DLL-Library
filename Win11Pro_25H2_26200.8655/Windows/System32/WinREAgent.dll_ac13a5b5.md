# Binary Specification: WinREAgent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WinREAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ac13a5b58b2a8a2f197a2f6809d4f48784b94b26646fa2435877478a4c1cac15`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BackupWinRE` | `0x16C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateWinREServicingManager` | `0x16C10` | 476 | UnwindData |  |
| 3 | `GetWinREAgentVersion` | `0x16E00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetWinREVersion` | `0x16E30` | 1,705 | UnwindData |  |
| 5 | `LoadWinREServicingManager` | `0x174E0` | 399 | UnwindData |  |
| 6 | `RestoreWinRE` | `0x17680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SaveWinREServicingManager` | `0x17690` | 142 | UnwindData |  |
