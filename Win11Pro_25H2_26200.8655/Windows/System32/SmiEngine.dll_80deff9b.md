# Binary Specification: SmiEngine.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SmiEngine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `80deff9be22f1927fa0160bc82ab5082057e5ce143b302007ec2b7c62a748f8e`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllCanUnloadNow` | `0x3460` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllGetClassObject` | `0x3490` | 357 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x3780` | 416 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x3930` | 185 | UnwindData |  |
| 3 | `ConstructRegLocation` | `0x4F90` | 468 | UnwindData |  |
| 5 | `CreateWcmEngineCore` | `0x5170` | 116 | UnwindData |  |
| 6 | `DeleteCompilerObject` | `0x2FDE0` | 40 | UnwindData |  |
| 11 | `GetCompilerObject` | `0x2FE10` | 173 | UnwindData |  |
| 2 | `CreateSettingsEnginePriv` | `0x416D0` | 153 | UnwindData |  |
| 12 | `GetItemFromCoreObject` | `0x44630` | 556 | UnwindData |  |
| 1 | `ConstructHiveLocation` | `0x4E060` | 12,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateLalInstance` | `0x512B0` | 38 | UnwindData |  |
| 13 | `SetLalCreator` | `0x512E0` | 322,489 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
