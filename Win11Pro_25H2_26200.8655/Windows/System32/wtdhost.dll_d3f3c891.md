# Binary Specification: wtdhost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wtdhost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d3f3c891d5309e034088d494d074e94958b23d3c212218971b46016f0e1f1fdd`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WtdhAllocateEvent` | `0x2180` | 75 | UnwindData |  |
| 4 | `WtdhFreeEventIoPacket` | `0x21E0` | 69 | UnwindData |  |
| 5 | `WtdhGetProcessId` | `0x2230` | 214 | UnwindData |  |
| 6 | `WtdhRegister` | `0x2310` | 573 | UnwindData |  |
| 7 | `WtdhUnregister` | `0x2560` | 515 | UnwindData |  |
| 8 | `WtdhWaitForSensorEvent` | `0x2770` | 1,350 | UnwindData |  |
| 2 | `WtdhDisableSensors` | `0x2E30` | 292 | UnwindData |  |
| 3 | `WtdhEnableSensors` | `0x2F60` | 296 | UnwindData |  |
