# Binary Specification: hid.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\hid.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e8043b16f4d7fd2b815ffd1638d2def7be4c0e0e324fe2dcee3b262bdce0d2ac`
* **Total Exported Functions:** 47

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 30 | `HidP_GetUsageValue` | `0x1010` | 93 | UnwindData |  |
| 33 | `HidP_GetUsagesEx` | `0x12E0` | 64 | UnwindData |  |
| 32 | `HidP_GetUsages` | `0x1330` | 98 | UnwindData |  |
| 24 | `HidP_GetData` | `0x18D0` | 92 | UnwindData |  |
| 36 | `HidP_InitializeReportForID` | `0x1D80` | 23 | UnwindData |  |
| 41 | `HidP_SetScaledUsageValue` | `0x2010` | 82 | UnwindData |  |
| 44 | `HidP_SetUsages` | `0x22F0` | 83 | UnwindData |  |
| 46 | `HidP_UnsetUsages` | `0x2460` | 101 | UnwindData |  |
| 42 | `HidP_SetUsageValue` | `0x2C00` | 83 | UnwindData |  |
| 31 | `HidP_GetUsageValueArray` | `0x2F50` | 98 | UnwindData |  |
| 27 | `HidP_GetScaledUsageValue` | `0x31E0` | 93 | UnwindData |  |
| 7 | `HidD_GetIndexedString` | `0x35C0` | 68 | UnwindData |  |
| 9 | `HidD_GetManufacturerString` | `0x3610` | 59 | UnwindData |  |
| 1 | `HidD_FlushQueue` | `0x3660` | 56 | UnwindData |  |
| 19 | `HidD_SetNumInputBuffers` | `0x36A0` | 63 | UnwindData |  |
| 20 | `HidD_SetOutputReport` | `0x36F0` | 59 | UnwindData |  |
| 8 | `HidD_GetInputReport` | `0x3740` | 59 | UnwindData |  |
| 15 | `HidD_GetSerialNumberString` | `0x3790` | 59 | UnwindData |  |
| 5 | `HidD_GetFeature` | `0x37E0` | 59 | UnwindData |  |
| 14 | `HidD_GetProductString` | `0x3830` | 59 | UnwindData |  |
| 13 | `HidD_GetPreparsedData` | `0x3880` | 245 | UnwindData |  |
| 18 | `HidD_SetFeature` | `0x3980` | 59 | UnwindData |  |
| 34 | `HidP_GetValueCaps` | `0x3CC0` | 47 | UnwindData |  |
| 29 | `HidP_GetSpecificValueCaps` | `0x3D00` | 65 | UnwindData |  |
| 3 | `HidD_GetAttributes` | `0x4000` | 718 | UnwindData |  |
| 23 | `HidP_GetCaps` | `0x42E0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `HidP_MaxUsageListLength` | `0x4480` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `HidP_GetButtonCaps` | `0x4520` | 47 | UnwindData |  |
| 28 | `HidP_GetSpecificButtonCaps` | `0x4560` | 93 | UnwindData |  |
| 26 | `HidP_GetLinkCollectionNodes` | `0x4800` | 57 | UnwindData |  |
| 37 | `HidP_MaxDataListLength` | `0x48E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `HidD_FreePreparsedData` | `0x4970` | 43 | UnwindData |  |
| 6 | `HidD_GetHidGuid` | `0x49B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `HidP_UsageListDifference` | `0x4A00` | 11 | UnwindData |  |
| 43 | `HidP_SetUsageValueArray` | `0x4B10` | 108 | UnwindData |  |
| 45 | `HidP_TranslateUsagesToI8042ScanCodes` | `0x4DE0` | 42 | UnwindData |  |
| 4 | `HidD_GetConfiguration` | `0x5870` | 106 | UnwindData |  |
| 10 | `HidD_GetMsGenreDescriptor` | `0x58E0` | 55 | UnwindData |  |
| 11 | `HidD_GetNumInputBuffers` | `0x5920` | 59 | UnwindData |  |
| 12 | `HidD_GetPhysicalDescriptor` | `0x5970` | 55 | UnwindData |  |
| 16 | `HidD_Hello` | `0x59B0` | 70 | UnwindData |  |
| 17 | `HidD_SetConfiguration` | `0x5A00` | 102 | UnwindData |  |
| 21 | `HidP_GetButtonArray` | `0x5A70` | 540 | UnwindData |  |
| 25 | `HidP_GetExtendedAttributes` | `0x5CA0` | 320 | UnwindData |  |
| 35 | `HidP_GetVersionInternal` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `HidP_SetButtonArray` | `0x5E10` | 507 | UnwindData |  |
| 40 | `HidP_SetData` | `0x6020` | 241 | UnwindData |  |
