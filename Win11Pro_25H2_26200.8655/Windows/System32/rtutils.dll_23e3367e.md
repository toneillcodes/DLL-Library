# Binary Specification: rtutils.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rtutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `23e3367ea3bf72e96be6a49fa0c67d7a3719c71fdc483d503346104942180ac1`
* **Total Exported Functions:** 41

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `TraceRegisterExA` | `0x1130` | 110 | UnwindData |  |
| 40 | `TraceVprintfExA` | `0x1710` | 124 | UnwindData |  |
| 32 | `TracePrintfA` | `0x17A0` | 122 | UnwindData |  |
| 33 | `TracePrintfExA` | `0x1820` | 119 | UnwindData |  |
| 25 | `TraceDeregisterExA` | `0x2B00` | 35 | UnwindData |  |
| 28 | `TraceDumpExA` | `0x34C0` | 145 | UnwindData |  |
| 24 | `TraceDeregisterA` | `0x4BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `TraceGetConsoleA` | `0x4BC0` | 166 | UnwindData |  |
| 31 | `TraceGetConsoleW` | `0x4BC0` | 166 | UnwindData |  |
| 36 | `TracePutsExA` | `0x4C70` | 848 | UnwindData |  |
| 26 | `TraceDeregisterExW` | `0x51F0` | 159 | UnwindData |  |
| 27 | `TraceDeregisterW` | `0x52A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `TraceDumpExW` | `0x52B0` | 881 | UnwindData |  |
| 34 | `TracePrintfExW` | `0x5630` | 104 | UnwindData |  |
| 35 | `TracePrintfW` | `0x56A0` | 108 | UnwindData |  |
| 37 | `TracePutsExW` | `0x5720` | 848 | UnwindData |  |
| 39 | `TraceRegisterExW` | `0x5A80` | 573 | UnwindData |  |
| 41 | `TraceVprintfExW` | `0x5CD0` | 124 | UnwindData |  |
| 7 | `RouterAssert` | `0x6190` | 214 | UnwindData |  |
| 1 | `LogErrorA` | `0x92A0` | 178 | UnwindData |  |
| 3 | `LogEventA` | `0x9360` | 159 | UnwindData |  |
| 8 | `RouterGetErrorStringA` | `0x9410` | 249 | UnwindData |  |
| 10 | `RouterLogDeregisterA` | `0x9510` | 27 | UnwindData |  |
| 11 | `RouterLogDeregisterW` | `0x9510` | 27 | UnwindData |  |
| 12 | `RouterLogEventA` | `0x9540` | 117 | UnwindData |  |
| 13 | `RouterLogEventDataA` | `0x95C0` | 83 | UnwindData |  |
| 15 | `RouterLogEventExA` | `0x9620` | 39 | UnwindData |  |
| 17 | `RouterLogEventStringA` | `0x9650` | 307 | UnwindData |  |
| 19 | `RouterLogEventValistExA` | `0x9790` | 1,130 | UnwindData |  |
| 22 | `RouterLogRegisterA` | `0x9C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `LogErrorW` | `0x9C20` | 178 | UnwindData |  |
| 4 | `LogEventW` | `0x9CE0` | 159 | UnwindData |  |
| 9 | `RouterGetErrorStringW` | `0x9D90` | 249 | UnwindData |  |
| 14 | `RouterLogEventDataW` | `0x9E90` | 83 | UnwindData |  |
| 16 | `RouterLogEventExW` | `0x9EF0` | 39 | UnwindData |  |
| 18 | `RouterLogEventStringW` | `0x9F20` | 307 | UnwindData |  |
| 20 | `RouterLogEventValistExW` | `0xA060` | 859 | UnwindData |  |
| 21 | `RouterLogEventW` | `0xA3D0` | 117 | UnwindData |  |
| 23 | `RouterLogRegisterW` | `0xA450` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MprSetupProtocolEnum` | `0xAC60` | 1,209 | UnwindData |  |
| 6 | `MprSetupProtocolFree` | `0xB120` | 60 | UnwindData |  |
