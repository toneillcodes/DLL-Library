# Binary Specification: wlansvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wlansvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d4401dac28db988a8a152c2763c6bc66cdb77f4b648ece3da94cb59ed0505489`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `WLNotifyOnLogoff` | `0xA7D90` | 160 | UnwindData |  |
| 5 | `VsIeProviderGetFunctionTable` | `0xBD000` | 394 | UnwindData |  |
| 1 | `SvchostPushServiceGlobals` | `0xF2640` | 142 | UnwindData |  |
| 2 | `WlanSvcMain` | `0xF2A30` | 3,957 | UnwindData |  |
| 7 | `WLNotifyOnLogon` | `0x1489C0` | 1,146 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x1F2A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x1F2A90` | 350,283 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
