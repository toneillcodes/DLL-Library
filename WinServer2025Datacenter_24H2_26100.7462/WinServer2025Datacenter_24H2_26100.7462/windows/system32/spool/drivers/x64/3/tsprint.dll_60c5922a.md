# Binary Specification: tsprint.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\spool\drivers\x64\3\tsprint.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `60c5922a6d808723c9f61447849c38ed5f72ab64c8f38af21251939a5cb50368`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 255 | `DrvConvertDevMode` | `0x2FE0` | 671 | UnwindData |  |
| 256 | `DrvPrinterEvent` | `0x3290` | 710 | UnwindData |  |
| 257 | `MxdcGetPDEVAdjustment` | `0x36D0` | 718 | UnwindData |  |
| 258 | `DevQueryPrintEx` | `0x4570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `DrvDeviceCapabilities` | `0x4580` | 46 | UnwindData |  |
| 263 | `DrvDevicePropertySheets` | `0x45C0` | 811 | UnwindData |  |
| 264 | `DrvDocumentPropertySheets` | `0x4900` | 123 | UnwindData |  |
| 254 | `DrvSplDeviceCaps` | `0x4990` | 754 | UnwindData |  |
| 261 | `DllMain` | `0x6EA0` | 379 | UnwindData |  |
| 259 | `DllCanUnloadNow` | `0x8BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `DllGetClassObject` | `0x8BE0` | 486 | UnwindData |  |
