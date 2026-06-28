# Binary Specification: PS5UI.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_b818a930ca84de62\Amd64\PS5UI.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a4d4e7acb668bcdd6da0e1d298cafe721932f5e97d5a657d5db56cbc1e39690f`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 258 | `DevQueryPrintEx` | `0x3720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `DllCanUnloadNow` | `0x3740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `DllGetClassObject` | `0x3760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `DllMain` | `0x3780` | 32 | UnwindData |  |
| 262 | `DrvConvertDevMode` | `0x37B0` | 32 | UnwindData |  |
| 263 | `DrvDeviceCapabilities` | `0x37E0` | 32 | UnwindData |  |
| 264 | `DrvDevicePropertySheets` | `0x3810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `DrvDocumentEvent` | `0x3830` | 55 | UnwindData |  |
| 266 | `DrvDocumentPropertySheets` | `0x3870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `DrvDriverEvent` | `0x3890` | 22 | UnwindData |  |
| 268 | `DrvPrinterEvent` | `0x38B0` | 22 | UnwindData |  |
| 269 | `DrvQueryColorProfile` | `0x38D0` | 42 | UnwindData |  |
| 285 | `DrvQueryJobAttributes` | `0x3900` | 22 | UnwindData |  |
| 254 | `DrvSplDeviceCaps` | `0x3920` | 42 | UnwindData |  |
| 286 | `DrvUpgradePrinter` | `0x3950` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | *Ordinal Only* | `0x3FA0` | 867 | UnwindData |  |
| 279 | *Ordinal Only* | `0x5FE0` | 114 | UnwindData |  |
| 280 | *Ordinal Only* | `0x83D0` | 801 | UnwindData |  |
| 284 | *Ordinal Only* | `0x8A50` | 506 | UnwindData |  |
| 283 | *Ordinal Only* | `0xA1A0` | 1,486 | UnwindData |  |
| 255 | `DrvPopulateFilterServices` | `0xCA90` | 400 | UnwindData |  |
| 256 | `DrvResetConfigCache` | `0x15A70` | 57 | UnwindData |  |
| 274 | *Ordinal Only* | `0x193C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | *Ordinal Only* | `0x193D0` | 2,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | *Ordinal Only* | `0x19CD0` | 651 | UnwindData |  |
| 270 | *Ordinal Only* | `0x1A000` | 858 | UnwindData |  |
| 277 | *Ordinal Only* | `0x1E890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | *Ordinal Only* | `0x1E8A0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | *Ordinal Only* | `0x1EA40` | 59 | UnwindData |  |
| 282 | *Ordinal Only* | `0x20880` | 196 | UnwindData |  |
| 281 | *Ordinal Only* | `0x20C70` | 784 | UnwindData |  |
| 257 | `MxdcGetPDEVAdjustment` | `0x21BF0` | 1,585 | UnwindData |  |
| 273 | *Ordinal Only* | `0x24280` | 1,007 | UnwindData |  |
