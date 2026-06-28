# Binary Specification: ztrace_maps.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ztrace_maps.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a0d77484ce51037be9e16d3f0edbdc46756e9f57ec51950a14338cebe6c61aea`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ZTraceClose` | `0x31E0` | 121 | UnwindData |  |
| 2 | `ZTraceEnabledHelper` | `0x3260` | 60 | UnwindData |  |
| 3 | `ZTraceHelper` | `0x32B0` | 46 | UnwindData |  |
| 4 | `ZTraceHelperNoThis` | `0x32F0` | 47 | UnwindData |  |
| 5 | `ZTraceHelperV` | `0x3330` | 48 | UnwindData |  |
| 6 | `ZTraceHelperVC` | `0x3370` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ZTraceInit` | `0x35F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ZTraceReportIgnore` | `0x3610` | 28 | UnwindData |  |
| 9 | `ZTraceReportIgnoreC` | `0x3640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ZTraceReportIgnoreNoThis` | `0x3650` | 134 | UnwindData |  |
| 11 | `ZTraceReportOrigination` | `0x36E0` | 47 | UnwindData |  |
| 12 | `ZTraceReportOriginationC` | `0x3720` | 44 | UnwindData |  |
| 13 | `ZTraceReportOriginationNoThis` | `0x3760` | 48 | UnwindData |  |
| 14 | `ZTraceReportPropagation` | `0x37A0` | 47 | UnwindData |  |
| 15 | `ZTraceReportPropagationC` | `0x37E0` | 44 | UnwindData |  |
| 16 | `ZTraceReportPropagationNoThis` | `0x3820` | 48 | UnwindData |  |
| 17 | `ZTraceTestCopyTrace` | `0x3860` | 37 | UnwindData |  |
| 18 | `ZTraceTestForceClose` | `0x3890` | 43 | UnwindData |  |
| 19 | `ZTraceTestInit` | `0x38D0` | 0 | Indeterminate |  |
