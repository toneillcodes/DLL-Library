# Binary Specification: es.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\es.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4167b9302dc866f6c22f664d48fff9b5dab3b77993ae85c0bd564c646d1804df`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `ServiceMain` | `0xECB0` | 215 | UnwindData |  |
| 5 | `NotifyLogoffUser` | `0x11570` | 32 | UnwindData |  |
| 6 | `NotifyLogonUser` | `0x119F0` | 35 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x11FB0` | 525 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x26380` | 33,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SvchostPushServiceGlobals` | `0x2E580` | 37,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `LCEControlServer` | `0x37670` | 134 | UnwindData |  |
