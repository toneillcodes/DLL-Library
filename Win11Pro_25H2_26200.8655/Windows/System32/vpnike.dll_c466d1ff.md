# Binary Specification: vpnike.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vpnike.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c466d1fff5607158839d7dabf39e335c90ffc1fc6d2ff2ea7530fe0c37b4ebfe`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `VpnIkeRoamToBestCostInterface` | `0x80C0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `InitializeProtocolEngine` | `0x8380` | 553 | UnwindData |  |
| 3 | `InitializeServerProtocolEngine` | `0x85B0` | 658 | UnwindData |  |
| 4 | `SendMessageToProtocolEngine` | `0x8850` | 41 | UnwindData |  |
| 5 | `UninitializeProtocolEngine` | `0x8880` | 193 | UnwindData |  |
| 6 | `UninitializeServerProtocolEngine` | `0x8950` | 121 | UnwindData |  |
