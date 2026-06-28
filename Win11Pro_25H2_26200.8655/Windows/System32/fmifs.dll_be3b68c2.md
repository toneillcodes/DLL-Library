# Binary Specification: fmifs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fmifs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `be3b68c20faf690d10654fae158c5f5b5b56def904a3138dc06fe951e5d0e416`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 26 | `QueryIsDiskCheckScheduledForNextBoot` | `0x1010` | 306 | UnwindData |  |
| 22 | `QueryCorruptionStateByHandle` | `0x3960` | 461 | UnwindData |  |
| 16 | `GetDefaultFileSystem` | `0x4140` | 77 | UnwindData |  |
| 24 | `QueryDeviceInformationByHandle` | `0x41A0` | 76 | UnwindData |  |
| 21 | `QueryCorruptionState` | `0x43B0` | 153 | UnwindData |  |
| 5 | `ComputeFmMediaType` | `0x5060` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `EnableVolumeCompression` | `0x51B0` | 171 | UnwindData |  |
| 9 | `EnableVolumeIntegrity` | `0x5270` | 192 | UnwindData |  |
| 11 | `Format` | `0x5340` | 1,808 | UnwindData |  |
| 12 | `FormatEx` | `0x5A60` | 2,062 | UnwindData |  |
| 13 | `FormatEx2` | `0x6280` | 2,559 | UnwindData |  |
| 17 | `GetDefaultFileSystem2` | `0x6C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `GetFsFormatOptions` | `0x6CB0` | 712 | UnwindData |  |
| 20 | `QueryAvailableFileSystemFormat` | `0x6F80` | 174 | UnwindData |  |
| 23 | `QueryDeviceInformation` | `0x7040` | 493 | UnwindData |  |
| 25 | `QueryFileSystemName` | `0x7240` | 1,295 | UnwindData |  |
| 27 | `QueryLatestFileSystemVersion` | `0x7760` | 173 | UnwindData |  |
| 28 | `QuerySupportedMedia` | `0x7820` | 503 | UnwindData |  |
| 4 | `ClearPerMachineFileSystemState` | `0x7A20` | 323 | UnwindData |  |
| 6 | `CreatePerMachineFileSystemStateKey` | `0x7B70` | 387 | UnwindData |  |
| 29 | `SetLabel` | `0x7D00` | 756 | UnwindData |  |
| 7 | `DiskCopy` | `0x8000` | 45 | UnwindData |  |
| 1 | `GetFirstCorruptionInfo` | `0x80B0` | 481 | UnwindData |  |
| 2 | `Chkdsk` | `0x82A0` | 1,112 | UnwindData |  |
| 3 | `ChkdskEx` | `0x8700` | 4,935 | UnwindData |  |
| 14 | `FreeCorruptionInfo` | `0x9A50` | 44 | UnwindData |  |
| 15 | `GetCorruptionInfoClose` | `0x9A90` | 126 | UnwindData |  |
| 19 | `GetNextCorruptionInfo` | `0x9B20` | 949 | UnwindData |  |
| 10 | `Extend` | `0xA000` | 693 | UnwindData |  |
