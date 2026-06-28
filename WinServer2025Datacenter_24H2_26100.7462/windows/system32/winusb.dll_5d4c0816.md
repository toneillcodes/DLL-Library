# Binary Specification: winusb.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winusb.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5d4c0816d8c2d809640a9e35a2b519cde5be59bb6c12aea294d2d3d627ae56ae`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WinUsb_AbortPipe` | `0x1F30` | 227 | UnwindData |  |
| 2 | `WinUsb_AbortPipeAsync` | `0x2020` | 122 | UnwindData |  |
| 3 | `WinUsb_ControlTransfer` | `0x20A0` | 509 | UnwindData |  |
| 4 | `WinUsb_FlushPipe` | `0x22B0` | 310 | UnwindData |  |
| 5 | `WinUsb_Free` | `0x23F0` | 206 | UnwindData |  |
| 6 | `WinUsb_GetAdjustedFrameNumber` | `0x24D0` | 163 | UnwindData |  |
| 7 | `WinUsb_GetAssociatedInterface` | `0x2580` | 535 | UnwindData |  |
| 8 | `WinUsb_GetCurrentAlternateSetting` | `0x27A0` | 279 | UnwindData |  |
| 9 | `WinUsb_GetCurrentFrameNumber` | `0x28C0` | 355 | UnwindData |  |
| 10 | `WinUsb_GetCurrentFrameNumberAndQpc` | `0x2A30` | 322 | UnwindData |  |
| 11 | `WinUsb_GetDescriptor` | `0x2B80` | 369 | UnwindData |  |
| 12 | `WinUsb_GetOverlappedResult` | `0x2D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WinUsb_GetPipePolicy` | `0x2D20` | 373 | UnwindData |  |
| 14 | `WinUsb_GetPowerPolicy` | `0x2EA0` | 361 | UnwindData |  |
| 15 | `WinUsb_Initialize` | `0x3010` | 1,937 | UnwindData |  |
| 16 | `WinUsb_ParseConfigurationDescriptor` | `0x37B0` | 354 | UnwindData |  |
| 17 | `WinUsb_ParseDescriptors` | `0x3920` | 98 | UnwindData |  |
| 18 | `WinUsb_QueryDeviceInformation` | `0x3990` | 317 | UnwindData |  |
| 19 | `WinUsb_QueryInterfaceSettings` | `0x3AE0` | 141 | UnwindData |  |
| 20 | `WinUsb_QueryPipe` | `0x3B80` | 238 | UnwindData |  |
| 21 | `WinUsb_QueryPipeEx` | `0x3C80` | 389 | UnwindData |  |
| 22 | `WinUsb_ReadIsochPipe` | `0x3E10` | 65 | UnwindData |  |
| 23 | `WinUsb_ReadIsochPipeAsap` | `0x3E60` | 66 | UnwindData |  |
| 24 | `WinUsb_ReadPipe` | `0x4270` | 484 | UnwindData |  |
| 25 | `WinUsb_RegisterIsochBuffer` | `0x4460` | 415 | UnwindData |  |
| 26 | `WinUsb_ResetPipe` | `0x4610` | 227 | UnwindData |  |
| 27 | `WinUsb_ResetPipeAsync` | `0x4700` | 122 | UnwindData |  |
| 28 | `WinUsb_SetCurrentAlternateSetting` | `0x4780` | 227 | UnwindData |  |
| 29 | `WinUsb_SetCurrentAlternateSettingAsync` | `0x4870` | 380 | UnwindData |  |
| 30 | `WinUsb_SetPipePolicy` | `0x4A00` | 460 | UnwindData |  |
| 31 | `WinUsb_SetPowerPolicy` | `0x4BE0` | 465 | UnwindData |  |
| 32 | `WinUsb_StartTrackingForTimeSync` | `0x4DC0` | 322 | UnwindData |  |
| 33 | `WinUsb_StopTrackingForTimeSync` | `0x4F10` | 322 | UnwindData |  |
| 34 | `WinUsb_UnregisterIsochBuffer` | `0x5060` | 175 | UnwindData |  |
| 35 | `WinUsb_WriteIsochPipe` | `0x5140` | 38 | UnwindData |  |
| 36 | `WinUsb_WriteIsochPipeAsap` | `0x5170` | 39 | UnwindData |  |
| 37 | `WinUsb_WritePipe` | `0x5500` | 484 | UnwindData |  |
