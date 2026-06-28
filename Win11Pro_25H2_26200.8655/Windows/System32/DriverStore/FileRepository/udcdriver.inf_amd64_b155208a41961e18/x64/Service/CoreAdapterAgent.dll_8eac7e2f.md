# Binary Specification: CoreAdapterAgent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\udcdriver.inf_amd64_b155208a41961e18\x64\Service\CoreAdapterAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8eac7e2f6264fd4f91b55271318e820b75351e2a61b8ac53485ac1e4bf03cf71`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CoreAdapterAgent@@QEAA@PEAUICoreApi@UDCCore@@V?$shared_ptr@UIConfigAgent@@@std@@PEAVEpUrlProvider@UDC@@@Z` | `0x6030` | 838 | UnwindData |  |
| 2 | `??0LogThrottler@@QEAA@XZ` | `0x6380` | 290 | UnwindData |  |
| 3 | `??0PersonaUtility@udc@@QEAA@$$QEAV01@@Z` | `0x64B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0PersonaUtility@udc@@QEAA@AEBV01@@Z` | `0x64C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0PersonaUtility@udc@@QEAA@XZ` | `0x64D0` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0UDCHelperFactory@udc@@QEAA@AEBV01@@Z` | `0x6B20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0UDCTag@@QEAA@$$QEAV0@@Z` | `0x6BC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0UDCTag@@QEAA@AEBV0@@Z` | `0x6C20` | 55 | UnwindData |  |
| 9 | `??1LogThrottler@@QEAA@XZ` | `0x91F0` | 31 | UnwindData |  |
| 10 | `??1UDCTag@@QEAA@XZ` | `0x9390` | 31 | UnwindData |  |
| 11 | `??1UdcStatusManager@UDC@@QEAA@XZ` | `0x93B0` | 392 | UnwindData |  |
| 12 | `??4GpuTagGenerator@@QEAAAEAV0@$$QEAV0@@Z` | `0xA310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??4GpuTagGenerator@@QEAAAEAV0@AEBV0@@Z` | `0xA320` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??4Persona@udc@@QEAAAEAV01@$$QEAV01@@Z` | `0xA430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??4Persona@udc@@QEAAAEAV01@AEBV01@@Z` | `0xA440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??4PersonaUtility@udc@@QEAAAEAV01@$$QEAV01@@Z` | `0xA450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??4PersonaUtility@udc@@QEAAAEAV01@AEBV01@@Z` | `0xA460` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??4UDCHelperFactory@udc@@QEAAAEAV01@AEBV01@@Z` | `0xA670` | 369 | UnwindData |  |
| 19 | `??4UDCTag@@QEAAAEAV0@$$QEAV0@@Z` | `0xA7F0` | 141 | UnwindData |  |
| 20 | `??4UDCTag@@QEAAAEAV0@AEBV0@@Z` | `0xA880` | 86 | UnwindData |  |
| 21 | `??4Version@@QEAAAEAV0@$$QEAV0@@Z` | `0xA8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??4Version@@QEAAAEAV0@AEBV0@@Z` | `0xA900` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??8Version@@QEAA_NAEBV0@@Z` | `0xA9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??9Version@@QEAA_NAEBV0@@Z` | `0xA9B0` | 19 | UnwindData |  |
| 25 | `??MVersion@@QEAA_NAEBV0@@Z` | `0xAA70` | 19 | UnwindData |  |
| 26 | `??NVersion@@QEAA_NAEBV0@@Z` | `0xAA90` | 19 | UnwindData |  |
| 27 | `??OVersion@@QEAA_NAEBV0@@Z` | `0xAAB0` | 19 | UnwindData |  |
| 28 | `??PVersion@@QEAA_NAEBV0@@Z` | `0xAAD0` | 19 | UnwindData |  |
| 30 | `??_FCoreAdapterAgent@@QEAAXXZ` | `0xAD30` | 48 | UnwindData |  |
| 31 | `?WriteDeviceIDToRegistry@CoreAdapterAgent@@QEAAXXZ` | `0x15540` | 1,541 | UnwindData |  |
| 32 | `?__autoclassinit2@AppAndTagCollection@@QEAAX_K@Z` | `0x1DBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?__autoclassinit2@ApplicabilityEvaluator@@QEAAX_K@Z` | `0x1DBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?__autoclassinit2@LogThrottler@@QEAAX_K@Z` | `0x1DBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `?__autoclassinit2@UDCHelperFactory@udc@@QEAAX_K@Z` | `0x1DC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?__autoclassinit2@UdcStatusManager@UDC@@QEAAX_K@Z` | `0x1DC10` | 30,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??_7PersonaUtility@udc@@6B@` | `0x254A8` | 0 | Indeterminate |  |
