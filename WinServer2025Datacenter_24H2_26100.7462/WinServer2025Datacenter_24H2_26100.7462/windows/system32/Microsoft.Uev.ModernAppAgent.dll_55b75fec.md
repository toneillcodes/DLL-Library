# Binary Specification: Microsoft.Uev.ModernAppAgent.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft.Uev.ModernAppAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `55b75fec16941a79da76f0094f5b44971f87cbf71d294117e744ac23f9b18f22`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AllocateSettingsContext` | `0x22E00` | 165 | UnwindData |  |
| 2 | `ExportModernSettings` | `0x22EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ExportSettingsToStore` | `0x22ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FreeSettingsContext` | `0x22EF0` | 22 | UnwindData |  |
| 4 | `GetModernTemplateId` | `0x22F10` | 510 | UnwindData |  |
| 9 | `GetOSSettingsRoamingState` | `0x23120` | 333 | UnwindData |  |
| 5 | `ImportModernSettings` | `0x23280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ImportSettingsFromStore` | `0x232A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `InitializeRollbackState` | `0x232C0` | 1,016,764 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
