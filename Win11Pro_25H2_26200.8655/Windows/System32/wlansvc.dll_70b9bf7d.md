# Binary Specification: wlansvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wlansvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `70b9bf7d8e5f28c9309a21f99db761e1f2544db2afc63435bf6278331536e592`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `WLNotifyOnLogoff` | `0xA7230` | 160 | UnwindData |  |
| 5 | `VsIeProviderGetFunctionTable` | `0xAAFB0` | 312 | UnwindData |  |
| 1 | `SvchostPushServiceGlobals` | `0xF0050` | 142 | UnwindData |  |
| 2 | `WlanSvcMain` | `0xF0440` | 3,957 | UnwindData |  |
| 7 | `WLNotifyOnLogon` | `0x1424D0` | 1,146 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x1E74A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x1E74C0` | 339,483 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
