# Binary Specification: RdpDwmEncoder.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\RdpDwmEncoder.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ab71377fc0918995390ad9902b6b6ad411ae22991ca4ea9dae9ba571994569cd`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x6080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x60A0` | 53 | UnwindData |  |
| 4 | `GetProxyDllInfo` | `0x60E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WindowNotificationSubscriberInit` | `0x6100` | 76 | UnwindData |  |
