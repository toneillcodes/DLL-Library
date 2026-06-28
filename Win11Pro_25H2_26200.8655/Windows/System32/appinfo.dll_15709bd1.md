# Binary Specification: appinfo.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\appinfo.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `15709bd1b18a1f7514371d34b253e86cc1f08acfd1c4b251f8b3b2b465d77c59`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `AiEnableDesktopRpcInterface` | `0x12800` | 736 | UnwindData |  |
| 3 | `ServiceMain` | `0x14930` | 1,271 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x19A90` | 176,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AiDisableDesktopRpcInterface` | `0x44D10` | 272 | UnwindData |  |
