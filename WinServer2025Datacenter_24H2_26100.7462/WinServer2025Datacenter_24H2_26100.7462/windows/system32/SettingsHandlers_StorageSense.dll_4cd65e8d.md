# Binary Specification: SettingsHandlers_StorageSense.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SettingsHandlers_StorageSense.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4cd65e8d5fb295d3231036aca4aac6184f913abcef09e5f843915e7b2cad15c0`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `GetProxyDllInfo` | `0x11680` | 3,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x12520` | 55 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x12560` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x125A0` | 115 | UnwindData |  |
| 5 | `GetSetting` | `0x12670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetSettingForUser` | `0x12680` | 831,308 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
