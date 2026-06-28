# Binary Specification: AppXApplicabilityBlob.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AppXApplicabilityBlob.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `303377dfd6c48892459bc8b79608af5412b27133200884747322f22b71542641`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `GetApplicabilityFactory` | `0x10030` | 92 | UnwindData |  |
| 7 | `IsXAP` | `0x11270` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `IsAppx` | `0x112F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `IsPreThresholdDesktop` | `0x11380` | 3,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IsPreThresholdPhone` | `0x11F40` | 68,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateSerializedBundleManifestStatement` | `0x22950` | 450 | UnwindData |  |
| 4 | `IsModernApp` | `0x22B20` | 10,140 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
