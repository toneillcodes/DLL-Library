# Binary Specification: wcimage.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wcimage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0b6e266022f5e380a542b5ff5599be4f0b7020f2fcc990b9a17f5b0d7f966a05`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `WcConvertToReparsePoint` | `0x3B20` | 245 | UnwindData |  |
| 5 | `WcCreateContainerImageFromWim` | `0x3C20` | 39 | UnwindData |  |
| 6 | `WcCreateContainerImageFromWimEx` | `0x3C50` | 666 | UnwindData |  |
| 10 | `WcExpandContainerWim` | `0x3EF0` | 826 | UnwindData |  |
| 12 | `WcProcessContainerLayer` | `0x4230` | 797 | UnwindData |  |
| 4 | `WcCreateContainerImageFromPortableBaseLayer` | `0x73B0` | 1,847 | UnwindData |  |
| 1 | `WcCompressFile` | `0x7E30` | 334 | UnwindData |  |
| 2 | `WcCompressFileAsync` | `0x7F90` | 274 | UnwindData |  |
| 9 | `WcEnsurePathExists` | `0x80B0` | 371 | UnwindData |  |
| 14 | `WcWaitForPendingFileCompressionOperations` | `0x8230` | 111 | UnwindData |  |
| 7 | `WcDismountVirtualDisk` | `0x9200` | 523 | UnwindData |  |
| 8 | `WcDismountVirtualDiskFromHandle` | `0x9420` | 255 | UnwindData |  |
| 11 | `WcMountVirtualDisk` | `0x9530` | 2,328 | UnwindData |  |
| 13 | `WcSetVirtualDiskAttributes` | `0x9E50` | 664 | UnwindData |  |
