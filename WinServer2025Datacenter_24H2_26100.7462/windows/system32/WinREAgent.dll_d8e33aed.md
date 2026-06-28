# Binary Specification: WinREAgent.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WinREAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d8e33aed0ad962df0e47005aad54c405bbdb555f95cab8009e0ac1989651afc0`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BackupWinRE` | `0x17250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateWinREServicingManager` | `0x17260` | 476 | UnwindData |  |
| 3 | `GetWinREAgentVersion` | `0x17450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetWinREVersion` | `0x17480` | 1,705 | UnwindData |  |
| 5 | `LoadWinREServicingManager` | `0x17B30` | 399 | UnwindData |  |
| 6 | `RestoreWinRE` | `0x17CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SaveWinREServicingManager` | `0x17CE0` | 142 | UnwindData |  |
