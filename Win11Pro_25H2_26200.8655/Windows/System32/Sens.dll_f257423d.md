# Binary Specification: Sens.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Sens.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f257423d4153e0acf87185366c66d72f3ca85e24071951f97e888362df61c2cf`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `SensNotifyRasEvent` | `0x4EE0` | 62 | UnwindData |  |
| 5 | `SensNotifyWinlogonEvent` | `0x5E20` | 61 | UnwindData |  |
| 3 | `SensNotifyNetconEvent` | `0x8010` | 364 | UnwindData |  |
| 1 | `ServiceMain` | `0x8570` | 362 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x9AE0` | 2,480 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
