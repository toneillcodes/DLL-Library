# Binary Specification: UNIDRVUI.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\spool\drivers\x64\3\UNIDRVUI.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `681910369c4d26c47242651dfbfe801146e622e27ce29dd1c5c0152c8948bf6e`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 258 | `DevQueryPrintEx` | `0x3850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `DllCanUnloadNow` | `0x3870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `DllGetClassObject` | `0x3890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `DllMain` | `0x38B0` | 130 | UnwindData |  |
| 262 | `DrvConvertDevMode` | `0x3940` | 32 | UnwindData |  |
| 263 | `DrvDeviceCapabilities` | `0x3970` | 32 | UnwindData |  |
| 264 | `DrvDevicePropertySheets` | `0x39A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `DrvDocumentEvent` | `0x39C0` | 55 | UnwindData |  |
| 266 | `DrvDocumentPropertySheets` | `0x3A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `DrvDriverEvent` | `0x3A20` | 22 | UnwindData |  |
| 268 | `DrvPrinterEvent` | `0x3A40` | 22 | UnwindData |  |
| 269 | `DrvQueryColorProfile` | `0x3A60` | 42 | UnwindData |  |
| 285 | `DrvQueryJobAttributes` | `0x3A90` | 22 | UnwindData |  |
| 254 | `DrvSplDeviceCaps` | `0x3AB0` | 42 | UnwindData |  |
| 286 | `DrvUpgradePrinter` | `0x3AE0` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | *Ordinal Only* | `0x4050` | 987 | UnwindData |  |
| 279 | *Ordinal Only* | `0x61E0` | 328 | UnwindData |  |
| 280 | *Ordinal Only* | `0xA8F0` | 821 | UnwindData |  |
| 284 | *Ordinal Only* | `0xAF80` | 506 | UnwindData |  |
| 283 | *Ordinal Only* | `0xC720` | 1,480 | UnwindData |  |
| 255 | `DrvPopulateFilterServices` | `0xF030` | 400 | UnwindData |  |
| 256 | `DrvResetConfigCache` | `0x18000` | 57 | UnwindData |  |
| 274 | *Ordinal Only* | `0x1B930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | *Ordinal Only* | `0x1B940` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | *Ordinal Only* | `0x1C200` | 654 | UnwindData |  |
| 270 | *Ordinal Only* | `0x1C4D0` | 831 | UnwindData |  |
| 277 | *Ordinal Only* | `0x20E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | *Ordinal Only* | `0x20E20` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | *Ordinal Only* | `0x21100` | 59 | UnwindData |  |
| 282 | *Ordinal Only* | `0x22FD0` | 196 | UnwindData |  |
| 281 | *Ordinal Only* | `0x233C0` | 943 | UnwindData |  |
| 257 | `MxdcGetPDEVAdjustment` | `0x24530` | 1,708 | UnwindData |  |
| 273 | *Ordinal Only* | `0x26850` | 1,041 | UnwindData |  |
