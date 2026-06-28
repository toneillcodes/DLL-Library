# Binary Specification: dxva2.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dxva2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b964b915b9f92b28404a913427c25aa22374346006cc3f857e489ddd99216330`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `OPMGetVideoOutputForTarget` | `0x6470` | 408 | UnwindData |  |
| 19 | `GetNumberOfPhysicalMonitorsFromHMONITOR` | `0x6710` | 366 | UnwindData |  |
| 4 | `DXVA2CreateVideoService` | `0x7590` | 182 | UnwindData |  |
| 5 | `DXVAHD_CreateDevice` | `0x88C0` | 160 | UnwindData |  |
| 24 | `GetVCPFeatureAndVCPFeatureReply` | `0x9F40` | 191 | UnwindData |  |
| 8 | `DestroyPhysicalMonitors` | `0xA5A0` | 123 | UnwindData |  |
| 7 | `DestroyPhysicalMonitor` | `0xA630` | 49 | UnwindData |  |
| 39 | `SetVCPFeature` | `0xACD0` | 155 | UnwindData |  |
| 3 | `DXVA2CreateDirect3DDeviceManager9` | `0xAD80` | 176 | UnwindData |  |
| 11 | `GetMonitorCapabilities` | `0xBDE0` | 153 | UnwindData |  |
| 26 | `OPMGetVideoOutputsFromHMONITOR` | `0xC3B0` | 31,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetPhysicalMonitorFromTarget` | `0x13D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetNumberOfPhysicalMonitorsFromIDirect3DDevice9` | `0x13D20` | 82 | UnwindData |  |
| 21 | `GetPhysicalMonitorsFromHMONITOR` | `0x13D80` | 49 | UnwindData |  |
| 22 | `GetPhysicalMonitorsFromIDirect3DDevice9` | `0x13DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CapabilitiesRequestAndCapabilitiesReply` | `0x13DD0` | 156 | UnwindData |  |
| 9 | `GetCapabilitiesStringLength` | `0x13E80` | 140 | UnwindData |  |
| 23 | `GetTimingReport` | `0x13F20` | 140 | UnwindData |  |
| 31 | `SaveCurrentSettings` | `0x13FC0` | 125 | UnwindData |  |
| 6 | `DegaussMonitor` | `0x14230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `GetMonitorBrightness` | `0x14250` | 28 | UnwindData |  |
| 12 | `GetMonitorColorTemperature` | `0x14280` | 157 | UnwindData |  |
| 13 | `GetMonitorContrast` | `0x14330` | 28 | UnwindData |  |
| 14 | `GetMonitorDisplayAreaPosition` | `0x14360` | 93 | UnwindData |  |
| 15 | `GetMonitorDisplayAreaSize` | `0x143D0` | 93 | UnwindData |  |
| 16 | `GetMonitorRedGreenOrBlueDrive` | `0x14440` | 93 | UnwindData |  |
| 17 | `GetMonitorRedGreenOrBlueGain` | `0x144B0` | 93 | UnwindData |  |
| 18 | `GetMonitorTechnologyType` | `0x14520` | 173 | UnwindData |  |
| 28 | `RestoreMonitorFactoryColorDefaults` | `0x145E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `RestoreMonitorFactoryDefaults` | `0x14600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SaveCurrentMonitorSettings` | `0x14620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `SetMonitorBrightness` | `0x14630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SetMonitorColorTemperature` | `0x14640` | 142 | UnwindData |  |
| 34 | `SetMonitorContrast` | `0x146E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `SetMonitorDisplayAreaPosition` | `0x146F0` | 74 | UnwindData |  |
| 36 | `SetMonitorDisplayAreaSize` | `0x14740` | 74 | UnwindData |  |
| 37 | `SetMonitorRedGreenOrBlueDrive` | `0x14790` | 74 | UnwindData |  |
| 38 | `SetMonitorRedGreenOrBlueGain` | `0x147E0` | 74 | UnwindData |  |
| 27 | `OPMGetVideoOutputsFromIDirect3DDevice9Object` | `0x1C420` | 13,724 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
