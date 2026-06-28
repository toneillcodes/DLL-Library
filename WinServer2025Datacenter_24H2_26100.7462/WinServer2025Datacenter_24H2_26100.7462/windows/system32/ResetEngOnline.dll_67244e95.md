# Binary Specification: ResetEngOnline.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ResetEngOnline.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `67244e95bb1cab29bbd801a36387b4f1dcde6a870ae3ee5e22f87a2d699c55bc`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `IsEsimPresent` | `0x4D50` | 726 | UnwindData |  |
| 3 | `ResetEsim` | `0x5230` | 265 | UnwindData |  |
| 4 | `ResetGetEngineInterface` | `0x5340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ResetInitializeEngine` | `0x5360` | 18 | UnwindData |  |
| 6 | `ResetRebootSystem` | `0x5380` | 200 | UnwindData |  |
| 7 | `ResetReleaseEngine` | `0x5450` | 96 | UnwindData |  |
| 8 | `UninstallFinalize` | `0x54C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `UninstallGetInterface` | `0x54D0` | 7,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetNetworkCost` | `0x7150` | 188 | UnwindData |  |
