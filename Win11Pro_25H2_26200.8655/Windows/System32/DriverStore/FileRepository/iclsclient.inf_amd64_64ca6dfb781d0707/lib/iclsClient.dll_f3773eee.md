# Binary Specification: iclsClient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iclsclient.inf_amd64_64ca6dfb781d0707\lib\iclsClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f3773eeea947ff6a094af33f9dabc9b9234e9227d05049d62a8bc272cf34b00f`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `iclsGetClientVersion` | `0x4B30` | 370 | UnwindData |  |
| 10 | `iclsInit` | `0x4F70` | 81 | UnwindData |  |
| 12 | `iclsInitPCH` | `0x4FD0` | 71 | UnwindData |  |
| 11 | `iclsInitDG1` | `0x5020` | 71 | UnwindData |  |
| 14 | `iclsPermitInstall` | `0x5070` | 270 | UnwindData |  |
| 15 | `iclsPermitInstallIndirect` | `0x5180` | 253 | UnwindData |  |
| 6 | `iclsGetPermitInfo` | `0x5280` | 176 | UnwindData |  |
| 4 | `iclsGetGlobalAttribute` | `0x5330` | 126 | UnwindData |  |
| 5 | `iclsGetPermitAttribute` | `0x53B0` | 192 | UnwindData |  |
| 7 | `iclsGetPermitInfoCapability` | `0x5470` | 173 | UnwindData |  |
| 1 | `iclsDestroyPermitInfo` | `0x5520` | 176 | UnwindData |  |
| 8 | `iclsGetPlatformInfo` | `0x55D0` | 176 | UnwindData |  |
| 9 | `iclsGetPlatformType` | `0x5680` | 164 | UnwindData |  |
| 2 | `iclsDestroyPlatformInfo` | `0x5730` | 176 | UnwindData |  |
| 13 | `iclsPassThrough` | `0x57E0` | 192 | UnwindData |  |
