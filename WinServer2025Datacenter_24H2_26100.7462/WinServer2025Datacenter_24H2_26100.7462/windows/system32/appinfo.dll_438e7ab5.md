# Binary Specification: appinfo.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\appinfo.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `438e7ab53f12d112e6c9cde860a9ef1bf56f240880cef675fd158d82d2399d23`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `AiEnableDesktopRpcInterface` | `0x11D10` | 736 | UnwindData |  |
| 3 | `ServiceMain` | `0x13DE0` | 1,271 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x1AAD0` | 159,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AiDisableDesktopRpcInterface` | `0x41BB0` | 272 | UnwindData |  |
