# Binary Specification: SettingsHandlers_StorageSense.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SettingsHandlers_StorageSense.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `da5bf809c2a2a08aa5b2bae237626cfcec17704749045b01ef28cb3bebf7ea3f`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `GetProxyDllInfo` | `0x11320` | 13,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x14970` | 55 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x149B0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x149F0` | 115 | UnwindData |  |
| 5 | `GetSetting` | `0x14AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetSettingForUser` | `0x14AD0` | 759,308 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
