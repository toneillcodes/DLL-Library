# Binary Specification: vmdevicehost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vmdevicehost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d5f3ba855801219ddb99b2bcc916ba7e8792f5d3dba27b9238943b5ef212ee2c`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `HdvCreateDeviceInstance` | `0xC3E0` | 332 | UnwindData |  |
| 2 | `HdvCreateGuestMemoryAperture` | `0xC540` | 197 | UnwindData |  |
| 3 | `HdvCreateSectionBackedMmioRange` | `0xC610` | 146 | UnwindData |  |
| 4 | `HdvDeliverGuestInterrupt` | `0xC6B0` | 95 | UnwindData |  |
| 5 | `HdvDestroyGuestMemoryAperture` | `0xC720` | 115 | UnwindData |  |
| 6 | `HdvDestroySectionBackedMmioRange` | `0xC7A0` | 93 | UnwindData |  |
| 7 | `HdvInitializeDeviceHost` | `0xC810` | 153 | UnwindData |  |
| 8 | `HdvInitializeDeviceHostEx` | `0xC8B0` | 150 | UnwindData |  |
| 9 | `HdvInitializeDeviceHostForProxy` | `0xC950` | 310 | UnwindData |  |
| 10 | `HdvInitializeDeviceHostForProxyEx` | `0xCA90` | 311 | UnwindData |  |
| 11 | `HdvProxyDeviceHost` | `0xCBD0` | 340 | UnwindData |  |
| 12 | `HdvReadGuestMemory` | `0xCD30` | 199 | UnwindData |  |
| 13 | `HdvRegisterDoorbell` | `0xCE00` | 135 | UnwindData |  |
| 14 | `HdvRegisterDoorbellPage` | `0xCE90` | 109 | UnwindData |  |
| 15 | `HdvTeardownDeviceHost` | `0xCF10` | 243 | UnwindData |  |
| 16 | `HdvUnregisterDoorbell` | `0xD010` | 119 | UnwindData |  |
| 17 | `HdvUnregisterDoorbellPage` | `0xD090` | 93 | UnwindData |  |
| 18 | `HdvWriteGuestMemory` | `0xD100` | 199 | UnwindData |  |
