# Binary Specification: RdpDwmEncoder.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\RdpDwmEncoder.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3a02b7c9e9707de74b91e901671d360679bd12201832d684632cbe60d509576d`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x6140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x6160` | 53 | UnwindData |  |
| 4 | `GetProxyDllInfo` | `0x61A0` | 8,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WindowNotificationSubscriberInit` | `0x8160` | 76 | UnwindData |  |
