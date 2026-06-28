# Binary Specification: NvCamera64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\NvCamera\NvCamera64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ecc3638dd277a537be69b3edb6bee549d7edcedc17dc18cb0ae54dd9578598a6`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `?AnselShimDisableCheck@@YA_NXZ` | `0xAEEF0` | 50 | UnwindData |  |
| 2 | `AnselEnableCheck` | `0xAF030` | 50 | UnwindData |  |
| 3 | `AnselGetFunctionTable` | `0xAF070` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AnselGetFunctionTableSize` | `0xAF280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `AnselGetVersion` | `0xAF290` | 416,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `OnInstall` | `0x114D90` | 327,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetIpcVersion` | `0x164D60` | 90 | UnwindData |  |
| 8 | `SetFreeStyleStatus` | `0x164DC0` | 2,778,892 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
