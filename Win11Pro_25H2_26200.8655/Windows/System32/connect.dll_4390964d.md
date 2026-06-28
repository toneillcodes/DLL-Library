# Binary Specification: connect.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\connect.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4390964d3b544b5537c72ac48687b73924ac78f3a3c06758ab3abbfad262f299`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AddConnectionOptionListEntries` | `0x10230` | 227 | UnwindData |  |
| 2 | `CreateVPNConnection` | `0x10320` | 320 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x10470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x10490` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetInternetConnected` | `0x106F0` | 331 | UnwindData |  |
| 6 | `GetNetworkConnected` | `0x10850` | 320 | UnwindData |  |
| 7 | `GetVPNConnected` | `0x109A0` | 319 | UnwindData |  |
| 8 | `HrIsInternetConnected` | `0x10AF0` | 75 | UnwindData |  |
| 9 | `HrIsInternetConnectedGUID` | `0x10B50` | 71 | UnwindData |  |
| 10 | `IsInternetConnected` | `0x10BD0` | 205 | UnwindData |  |
| 11 | `IsInternetConnectedGUID` | `0x10CB0` | 224 | UnwindData |  |
| 12 | `IsUniqueConnectionName` | `0x10DA0` | 207 | UnwindData |  |
| 13 | `RegisterPageWithPage` | `0x11010` | 314 | UnwindData |  |
| 14 | `UnregisterPage` | `0x11150` | 251 | UnwindData |  |
| 15 | `UnregisterPagesLink` | `0x11260` | 252 | UnwindData |  |
