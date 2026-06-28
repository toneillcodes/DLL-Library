# Binary Specification: MrmDeploy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MrmDeploy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0b64cd64fa2e95cb2baf92f0d45d3207e43ac2330754592e28054628adef28be`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x6480` | 131 | UnwindData |  |
| 2 | `GetCanonicalMergedPriFileName` | `0x6E60` | 211 | UnwindData |  |
| 3 | `GetCanonicalMergedPriFileNameForPackages` | `0x6F40` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetOrCreatePriFileForApplicablePackages` | `0x7020` | 163 | UnwindData |  |
| 6 | `GetOrCreatePriFileForAvailablePackages` | `0x70D0` | 201 | UnwindData |  |
| 7 | `GetOrCreatePriFileForRelatedPackages` | `0x71A0` | 325 | UnwindData |  |
| 8 | `GetPriFileForPackageOnly` | `0x72F0` | 219 | UnwindData |  |
| 4 | `GetInitInfoByPackageFullName` | `0x7470` | 471 | UnwindData |  |
| 9 | `MergeRelatedPriFiles` | `0xA5C0` | 465 | UnwindData |  |
