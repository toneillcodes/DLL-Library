# Binary Specification: MrmDeploy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MrmDeploy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9bf4839de68e8e593b69f9826ec17fadc0658a76195f3330bd3787045bb9c73b`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x6280` | 131 | UnwindData |  |
| 2 | `GetCanonicalMergedPriFileName` | `0x6C60` | 211 | UnwindData |  |
| 3 | `GetCanonicalMergedPriFileNameForPackages` | `0x6D40` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetOrCreatePriFileForApplicablePackages` | `0x6E20` | 163 | UnwindData |  |
| 6 | `GetOrCreatePriFileForAvailablePackages` | `0x6ED0` | 201 | UnwindData |  |
| 7 | `GetOrCreatePriFileForRelatedPackages` | `0x6FA0` | 325 | UnwindData |  |
| 8 | `GetPriFileForPackageOnly` | `0x70F0` | 219 | UnwindData |  |
| 4 | `GetInitInfoByPackageFullName` | `0x7270` | 471 | UnwindData |  |
| 9 | `MergeRelatedPriFiles` | `0x7610` | 465 | UnwindData |  |
