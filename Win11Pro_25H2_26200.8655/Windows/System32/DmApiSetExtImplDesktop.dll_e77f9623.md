# Binary Specification: DmApiSetExtImplDesktop.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DmApiSetExtImplDesktop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e77f96238030ffcc9abbd3cabcfba23e5d7751546d29295917faad261c754eab`
* **Total Exported Functions:** 42

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DMCSP_DevDetail_GetDeviceHardwareData` | `0x6740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `DMCSP_DeviceStatus_IsBitlockerProtected` | `0x6760` | 2,437 | UnwindData |  |
| 27 | `DMDiag_Export_DiagnosticsLog` | `0x70F0` | 142 | UnwindData |  |
| 39 | `Mmpc_Lockdown_GetManagementUrls` | `0x7290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `Mmpc_Lockdown_IsCertificateTrustedForMmpc` | `0x72B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `Mmpc_Lockdown_IsLockedToMmpc` | `0x72D0` | 136 | UnwindData |  |
| 28 | `DMDiag_Filter_Diagnostics_Events_From_AutoLog` | `0x7360` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DMUI_DisplayConfigurationResult` | `0x7360` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `Mmpc_Lockdown_ReleaseManagementUrl` | `0x7360` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `DMUI_GetUserEditFieldInput` | `0x77B0` | 453 | UnwindData |  |
| 32 | `DMUI_GetUserPermission` | `0x7980` | 241 | UnwindData |  |
| 1 | `DMLegacy_UnActivateLOB` | `0x7A80` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DMCSP_DevDetail_GetCommercializationOperator` | `0x82F0` | 451 | UnwindData |  |
| 4 | `DMCSP_DevDetail_GetDeviceName` | `0x84C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DMCSP_DevDetail_GetDeviceType` | `0x84E0` | 73 | UnwindData |  |
| 6 | `DMCSP_DevDetail_GetFwV` | `0x8530` | 73 | UnwindData |  |
| 7 | `DMCSP_DevDetail_GetHwV` | `0x8580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DMCSP_DevDetail_GetLocalTimeString` | `0x85A0` | 410 | UnwindData |  |
| 9 | `DMCSP_DevDetail_GetMobileID` | `0x8740` | 127 | UnwindData |  |
| 10 | `DMCSP_DevDetail_GetOEM` | `0x87D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DMCSP_DevDetail_GetOSPlatform` | `0x87F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DMCSP_DevDetail_GetProcessorArchitecture` | `0x8810` | 58 | UnwindData |  |
| 13 | `DMCSP_DevDetail_GetProcessorType` | `0x8850` | 57 | UnwindData |  |
| 14 | `DMCSP_DevDetail_GetRadioSwV` | `0x8890` | 424 | UnwindData |  |
| 15 | `DMCSP_DevDetail_GetResolution` | `0x8A40` | 94 | UnwindData |  |
| 16 | `DMCSP_DevDetail_GetSwV` | `0x8AB0` | 406 | UnwindData |  |
| 17 | `DMCSP_DevDetail_GetSystemSKU` | `0x8C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `DMCSP_DevDetail_GetVoLTEServiceSetting` | `0x8C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `DMCSP_DevDetail_GetWLANMACAddress` | `0x8C80` | 42 | UnwindData |  |
| 20 | `DMCSP_DevDetail_SetDeviceName` | `0x8CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `DMCSP_DevInfo_GetDmV` | `0x8CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `DMCSP_DevInfo_GetHwDevID` | `0x8CE0` | 1,073 | UnwindData |  |
| 23 | `DMCSP_DevInfo_GetLanguage` | `0x9120` | 113 | UnwindData |  |
| 24 | `DMCSP_DevInfo_GetManufacturer` | `0x91A0` | 94 | UnwindData |  |
| 25 | `DMCSP_DevInfo_GetModel` | `0x9210` | 73 | UnwindData |  |
| 29 | `DMUI_DismissNotification` | `0x9260` | 1,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DMUI_GetUserPermissionAsync` | `0x9260` | 1,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DMUI_InformUser` | `0x9260` | 1,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DMUI_IsAbortSessionRequested` | `0x9260` | 1,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `DMUI_SyncMLAlertGetResults` | `0x9260` | 1,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `DMUI_SyncMLAlertGetStatusCode` | `0x9260` | 1,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `DMUI_SyncMLAlertShowUI` | `0x9260` | 1,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
