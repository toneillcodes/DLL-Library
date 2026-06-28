# Binary Specification: umpo-overrides.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\umpo-overrides.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4a7368281c60d10d16a225acaf46ea29c9f0462351d9cc2ff8547573ef84c825`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `UmpoDisablePowerSettingOverrideUpdates` | `0x82A0` | 360 | UnwindData |  |
| 2 | `UmpoEnablePowerSettingOverrideUpdates` | `0x8410` | 1,243 | UnwindData |  |
| 3 | `UmpoGetPowerSettingOverrides` | `0x8960` | 9,420 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
