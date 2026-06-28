# Binary Specification: prntvpt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\prntvpt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8702fc4aacd7de42363f9677263044f6909e8e9129497ab06aa36cf6d3aeef94`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `DllMain` | `0xA550` | 184 | UnwindData |  |
| 7 | `PTMergeAndValidatePrintTicket` | `0xBC40` | 281 | UnwindData |  |
| 4 | `PTCloseProvider` | `0xC060` | 236 | UnwindData |  |
| 9 | `PTConvertDevModeToPrintTicket` | `0xCEC0` | 231 | UnwindData |  |
| 6 | `PTGetPrintCapabilities` | `0xDA20` | 396 | UnwindData |  |
| 17 | `DllCanUnloadNow` | `0xE480` | 101 | UnwindData |  |
| 30 | `GetSchemaVersionThunk` | `0x118A0` | 30,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `DllGetClassObject` | `0x18F20` | 156 | UnwindData |  |
| 20 | `DllRegisterServer` | `0x18FD0` | 110 | UnwindData |  |
| 21 | `DllUnregisterServer` | `0x19050` | 353 | UnwindData |  |
| 8 | `PTConvertPrintTicketToDevMode` | `0x1B900` | 405 | UnwindData |  |
| 11 | `PTGetPrintDeviceCapabilities` | `0x1BAA0` | 310 | UnwindData |  |
| 12 | `PTGetPrintDeviceResources` | `0x1BBE0` | 326 | UnwindData |  |
| 2 | `PTOpenProvider` | `0x1BD30` | 576 | UnwindData |  |
| 3 | `PTOpenProviderEx` | `0x1BF80` | 594 | UnwindData |  |
| 1 | `PTQuerySchemaVersionSupport` | `0x1C1E0` | 242 | UnwindData |  |
| 10 | `PTReleaseMemory` | `0x1C2E0` | 76 | UnwindData |  |
| 5 | `BindPTProviderThunk` | `0x1C990` | 207 | UnwindData |  |
| 13 | `ConvertDevModeToPrintTicketThunk` | `0x1CA70` | 43 | UnwindData |  |
| 14 | `ConvertDevModeToPrintTicketThunk2` | `0x1CAB0` | 169 | UnwindData |  |
| 15 | `ConvertPrintTicketToDevModeThunk` | `0x1CB60` | 68 | UnwindData |  |
| 16 | `ConvertPrintTicketToDevModeThunk2` | `0x1CBB0` | 288 | UnwindData |  |
| 22 | `GetDeviceDefaultPrintTicketThunk` | `0x1CCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `GetDeviceNamespacesThunk` | `0x1CCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `GetPrintCapabilitiesThunk` | `0x1CCF0` | 38 | UnwindData |  |
| 25 | `GetPrintCapabilitiesThunk2` | `0x1CD20` | 192 | UnwindData |  |
| 26 | `GetPrintDeviceCapabilitiesThunk` | `0x1CDF0` | 38 | UnwindData |  |
| 27 | `GetPrintDeviceCapabilitiesThunk2` | `0x1CE20` | 236 | UnwindData |  |
| 28 | `GetPrintDeviceResourcesThunk` | `0x1CF20` | 55 | UnwindData |  |
| 29 | `GetPrintDeviceResourcesThunk2` | `0x1CF60` | 240 | UnwindData |  |
| 31 | `MergeAndValidatePrintTicketThunk` | `0x1D060` | 73 | UnwindData |  |
| 32 | `MergeAndValidatePrintTicketThunk2` | `0x1D0B0` | 254 | UnwindData |  |
| 33 | `UnbindPTProviderThunk` | `0x1D1C0` | 36,636 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
