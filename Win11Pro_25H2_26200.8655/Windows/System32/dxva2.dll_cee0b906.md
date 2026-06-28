# Binary Specification: dxva2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dxva2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cee0b90613f6152b6baa8522d57d9f6236b59d2c3ad752fd7bd45a7b0c9b2d99`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `OPMGetVideoOutputForTarget` | `0x6480` | 408 | UnwindData |  |
| 19 | `GetNumberOfPhysicalMonitorsFromHMONITOR` | `0x6720` | 366 | UnwindData |  |
| 4 | `DXVA2CreateVideoService` | `0x75A0` | 182 | UnwindData |  |
| 5 | `DXVAHD_CreateDevice` | `0x88D0` | 160 | UnwindData |  |
| 24 | `GetVCPFeatureAndVCPFeatureReply` | `0x9F50` | 191 | UnwindData |  |
| 8 | `DestroyPhysicalMonitors` | `0xA5B0` | 123 | UnwindData |  |
| 7 | `DestroyPhysicalMonitor` | `0xA640` | 49 | UnwindData |  |
| 39 | `SetVCPFeature` | `0xACE0` | 155 | UnwindData |  |
| 3 | `DXVA2CreateDirect3DDeviceManager9` | `0xAD90` | 176 | UnwindData |  |
| 11 | `GetMonitorCapabilities` | `0xBDF0` | 153 | UnwindData |  |
| 26 | `OPMGetVideoOutputsFromHMONITOR` | `0xC3C0` | 31,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetPhysicalMonitorFromTarget` | `0x13D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetNumberOfPhysicalMonitorsFromIDirect3DDevice9` | `0x13D30` | 82 | UnwindData |  |
| 21 | `GetPhysicalMonitorsFromHMONITOR` | `0x13D90` | 49 | UnwindData |  |
| 22 | `GetPhysicalMonitorsFromIDirect3DDevice9` | `0x13DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CapabilitiesRequestAndCapabilitiesReply` | `0x13DE0` | 156 | UnwindData |  |
| 9 | `GetCapabilitiesStringLength` | `0x13E90` | 140 | UnwindData |  |
| 23 | `GetTimingReport` | `0x13F30` | 140 | UnwindData |  |
| 31 | `SaveCurrentSettings` | `0x13FD0` | 125 | UnwindData |  |
| 6 | `DegaussMonitor` | `0x14240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `GetMonitorBrightness` | `0x14260` | 28 | UnwindData |  |
| 12 | `GetMonitorColorTemperature` | `0x14290` | 157 | UnwindData |  |
| 13 | `GetMonitorContrast` | `0x14340` | 28 | UnwindData |  |
| 14 | `GetMonitorDisplayAreaPosition` | `0x14370` | 93 | UnwindData |  |
| 15 | `GetMonitorDisplayAreaSize` | `0x143E0` | 93 | UnwindData |  |
| 16 | `GetMonitorRedGreenOrBlueDrive` | `0x14450` | 93 | UnwindData |  |
| 17 | `GetMonitorRedGreenOrBlueGain` | `0x144C0` | 93 | UnwindData |  |
| 18 | `GetMonitorTechnologyType` | `0x14530` | 173 | UnwindData |  |
| 28 | `RestoreMonitorFactoryColorDefaults` | `0x145F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `RestoreMonitorFactoryDefaults` | `0x14610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SaveCurrentMonitorSettings` | `0x14630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `SetMonitorBrightness` | `0x14640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SetMonitorColorTemperature` | `0x14650` | 142 | UnwindData |  |
| 34 | `SetMonitorContrast` | `0x146F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `SetMonitorDisplayAreaPosition` | `0x14700` | 74 | UnwindData |  |
| 36 | `SetMonitorDisplayAreaSize` | `0x14750` | 74 | UnwindData |  |
| 37 | `SetMonitorRedGreenOrBlueDrive` | `0x147A0` | 74 | UnwindData |  |
| 38 | `SetMonitorRedGreenOrBlueGain` | `0x147F0` | 74 | UnwindData |  |
| 27 | `OPMGetVideoOutputsFromIDirect3DDevice9Object` | `0x1C830` | 13,708 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
