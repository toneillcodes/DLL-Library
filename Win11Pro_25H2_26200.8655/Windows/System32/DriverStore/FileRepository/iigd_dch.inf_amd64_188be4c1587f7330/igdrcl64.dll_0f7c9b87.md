# Binary Specification: igdrcl64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igdrcl64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0f7c9b87ce12e01f185a100a1d9545e36700b1596048e5458657017721f9a6f3`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `clGetExtensionFunctionAddress` | `0x2A880` | 5,825 | UnwindData |  |
| 6 | `clGetPlatformInfo` | `0x2E1D0` | 61 | UnwindData |  |
| 1 | `GTPin_Init` | `0x34880` | 1,791,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `clEnqueueMarkerWithSyncObjectINTEL` | `0x1E9CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `clGetCLEventInfoINTEL` | `0x1E9CF0` | 32 | UnwindData |  |
| 4 | `clGetCLObjectInfoINTEL` | `0x1E9F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `clReleaseGlSharedEventINTEL` | `0x1E9F90` | 240 | UnwindData |  |
