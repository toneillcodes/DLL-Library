# Binary Specification: Websocket.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Websocket.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `61ede2a204ad579e732e128c416b529a972c46f89a5d8ffa14ec1d5771a76be3`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WebSocketAbortHandle` | `0x2020` | 63 | UnwindData |  |
| 2 | `WebSocketBeginClientHandshake` | `0x2070` | 138 | UnwindData |  |
| 3 | `WebSocketBeginServerHandshake` | `0x2100` | 150 | UnwindData |  |
| 4 | `WebSocketCompleteAction` | `0x21A0` | 67 | UnwindData |  |
| 5 | `WebSocketCreateClientHandle` | `0x21F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WebSocketCreateServerHandle` | `0x2210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WebSocketDeleteHandle` | `0x2230` | 38 | UnwindData |  |
| 8 | `WebSocketEndClientHandshake` | `0x2260` | 139 | UnwindData |  |
| 9 | `WebSocketEndServerHandshake` | `0x2300` | 58 | UnwindData |  |
| 10 | `WebSocketGetAction` | `0x2340` | 134 | UnwindData |  |
| 11 | `WebSocketGetGlobalProperty` | `0x23D0` | 107 | UnwindData |  |
| 12 | `WebSocketReceive` | `0x2450` | 74 | UnwindData |  |
| 13 | `WebSocketSend` | `0x24A0` | 88 | UnwindData |  |
