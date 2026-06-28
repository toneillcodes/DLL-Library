# Binary Specification: vmdevicehost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vmdevicehost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `66114e4e567ff4d68e6cca9f87d25f2199175616df33dc81526768e70ebae67f`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `HdvCreateDeviceInstance` | `0xC3F0` | 332 | UnwindData |  |
| 2 | `HdvCreateGuestMemoryAperture` | `0xC550` | 197 | UnwindData |  |
| 3 | `HdvCreateSectionBackedMmioRange` | `0xC620` | 146 | UnwindData |  |
| 4 | `HdvDeliverGuestInterrupt` | `0xC6C0` | 95 | UnwindData |  |
| 5 | `HdvDestroyGuestMemoryAperture` | `0xC730` | 115 | UnwindData |  |
| 6 | `HdvDestroySectionBackedMmioRange` | `0xC7B0` | 93 | UnwindData |  |
| 7 | `HdvInitializeDeviceHost` | `0xC820` | 153 | UnwindData |  |
| 8 | `HdvInitializeDeviceHostEx` | `0xC8C0` | 150 | UnwindData |  |
| 9 | `HdvInitializeDeviceHostForProxy` | `0xC960` | 310 | UnwindData |  |
| 10 | `HdvInitializeDeviceHostForProxyEx` | `0xCAA0` | 311 | UnwindData |  |
| 11 | `HdvProxyDeviceHost` | `0xCBE0` | 340 | UnwindData |  |
| 12 | `HdvReadGuestMemory` | `0xCD40` | 199 | UnwindData |  |
| 13 | `HdvRegisterDoorbell` | `0xCE10` | 135 | UnwindData |  |
| 14 | `HdvRegisterDoorbellPage` | `0xCEA0` | 109 | UnwindData |  |
| 15 | `HdvTeardownDeviceHost` | `0xCF20` | 243 | UnwindData |  |
| 16 | `HdvUnregisterDoorbell` | `0xD020` | 119 | UnwindData |  |
| 17 | `HdvUnregisterDoorbellPage` | `0xD0A0` | 93 | UnwindData |  |
| 18 | `HdvWriteGuestMemory` | `0xD110` | 199 | UnwindData |  |
