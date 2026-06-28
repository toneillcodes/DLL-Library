# Binary Specification: vpnike.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vpnike.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `81490e6192dcb81b950bc60c8dd7308c8b443b1c377315e776b50957190c7fde`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `VpnIkeRoamToBestCostInterface` | `0x80B0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `InitializeProtocolEngine` | `0x8370` | 553 | UnwindData |  |
| 3 | `InitializeServerProtocolEngine` | `0x85A0` | 658 | UnwindData |  |
| 4 | `SendMessageToProtocolEngine` | `0x8840` | 41 | UnwindData |  |
| 5 | `UninitializeProtocolEngine` | `0x8870` | 193 | UnwindData |  |
| 6 | `UninitializeServerProtocolEngine` | `0x8940` | 121 | UnwindData |  |
