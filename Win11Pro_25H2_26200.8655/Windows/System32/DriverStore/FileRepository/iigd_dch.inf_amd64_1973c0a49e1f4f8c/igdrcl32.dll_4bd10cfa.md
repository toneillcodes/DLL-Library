# Binary Specification: igdrcl32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igdrcl32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `4bd10cfa1d7cd8da560fdbf7ea42d3b8bf639245b7993422d0df43eacebf7ed5`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `clGetExtensionFunctionAddress` | `0x26CC0` | 10,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `clGetPlatformInfo` | `0x29790` | 22,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GTPin_Init` | `0x2F050` | 1,782,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `clEnqueueMarkerWithSyncObjectINTEL` | `0x1E2420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `clGetCLEventInfoINTEL` | `0x1E2430` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `clGetCLObjectInfoINTEL` | `0x1E2620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `clReleaseGlSharedEventINTEL` | `0x1E2630` | 1,438,410 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
