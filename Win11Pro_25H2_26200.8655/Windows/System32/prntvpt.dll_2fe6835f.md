# Binary Specification: prntvpt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\prntvpt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2fe6835f6cebc30e54d65f29017b75113bd6eec3236b4028d992b795ea1582e4`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `DllMain` | `0xA540` | 184 | UnwindData |  |
| 7 | `PTMergeAndValidatePrintTicket` | `0xBBB0` | 281 | UnwindData |  |
| 4 | `PTCloseProvider` | `0xBFD0` | 236 | UnwindData |  |
| 9 | `PTConvertDevModeToPrintTicket` | `0xCE30` | 231 | UnwindData |  |
| 6 | `PTGetPrintCapabilities` | `0xD9D0` | 312 | UnwindData |  |
| 17 | `DllCanUnloadNow` | `0xE0C0` | 101 | UnwindData |  |
| 30 | `GetSchemaVersionThunk` | `0x11560` | 33,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `DllGetClassObject` | `0x197B0` | 156 | UnwindData |  |
| 20 | `DllRegisterServer` | `0x19860` | 110 | UnwindData |  |
| 21 | `DllUnregisterServer` | `0x198E0` | 353 | UnwindData |  |
| 8 | `PTConvertPrintTicketToDevMode` | `0x1A050` | 405 | UnwindData |  |
| 11 | `PTGetPrintDeviceCapabilities` | `0x1A1F0` | 310 | UnwindData |  |
| 12 | `PTGetPrintDeviceResources` | `0x1A330` | 326 | UnwindData |  |
| 2 | `PTOpenProvider` | `0x1A480` | 462 | UnwindData |  |
| 3 | `PTOpenProviderEx` | `0x1A660` | 479 | UnwindData |  |
| 1 | `PTQuerySchemaVersionSupport` | `0x1A850` | 242 | UnwindData |  |
| 10 | `PTReleaseMemory` | `0x1A950` | 76 | UnwindData |  |
| 5 | `BindPTProviderThunk` | `0x1AC10` | 207 | UnwindData |  |
| 13 | `ConvertDevModeToPrintTicketThunk` | `0x1ACF0` | 43 | UnwindData |  |
| 14 | `ConvertDevModeToPrintTicketThunk2` | `0x1AD30` | 169 | UnwindData |  |
| 15 | `ConvertPrintTicketToDevModeThunk` | `0x1ADE0` | 68 | UnwindData |  |
| 16 | `ConvertPrintTicketToDevModeThunk2` | `0x1AE30` | 288 | UnwindData |  |
| 22 | `GetDeviceDefaultPrintTicketThunk` | `0x1AF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `GetDeviceNamespacesThunk` | `0x1AF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `GetPrintCapabilitiesThunk` | `0x1AF70` | 38 | UnwindData |  |
| 25 | `GetPrintCapabilitiesThunk2` | `0x1AFA0` | 192 | UnwindData |  |
| 26 | `GetPrintDeviceCapabilitiesThunk` | `0x1B070` | 38 | UnwindData |  |
| 27 | `GetPrintDeviceCapabilitiesThunk2` | `0x1B0A0` | 236 | UnwindData |  |
| 28 | `GetPrintDeviceResourcesThunk` | `0x1B1A0` | 55 | UnwindData |  |
| 29 | `GetPrintDeviceResourcesThunk2` | `0x1B1E0` | 240 | UnwindData |  |
| 31 | `MergeAndValidatePrintTicketThunk` | `0x1B2E0` | 73 | UnwindData |  |
| 32 | `MergeAndValidatePrintTicketThunk2` | `0x1B330` | 254 | UnwindData |  |
| 33 | `UnbindPTProviderThunk` | `0x1B440` | 33,164 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
