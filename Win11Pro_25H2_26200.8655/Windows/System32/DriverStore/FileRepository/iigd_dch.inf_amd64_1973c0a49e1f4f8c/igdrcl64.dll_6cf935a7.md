# Binary Specification: igdrcl64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igdrcl64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6cf935a7541ac5301af395c286244069f6cde805e5a12d374abf615d7a928662`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `clGetExtensionFunctionAddress` | `0x29D40` | 5,682 | UnwindData |  |
| 6 | `clGetPlatformInfo` | `0x2D550` | 41 | UnwindData |  |
| 1 | `GTPin_Init` | `0x33CC0` | 1,889,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `clEnqueueMarkerWithSyncObjectINTEL` | `0x2012B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `clGetCLEventInfoINTEL` | `0x2012C0` | 32 | UnwindData |  |
| 4 | `clGetCLObjectInfoINTEL` | `0x201560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `clReleaseGlSharedEventINTEL` | `0x201570` | 240 | UnwindData |  |
