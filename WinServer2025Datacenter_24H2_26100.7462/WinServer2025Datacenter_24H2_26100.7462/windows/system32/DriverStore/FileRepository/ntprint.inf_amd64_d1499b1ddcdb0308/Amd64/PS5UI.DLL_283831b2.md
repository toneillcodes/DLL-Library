# Binary Specification: PS5UI.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\DriverStore\FileRepository\ntprint.inf_amd64_d1499b1ddcdb0308\Amd64\PS5UI.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `283831b2e4a0d5ed09b51cdea2772fdb4919b47c4d1d0786d78daa7a39e38ec9`
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
| 286 | `DrvUpgradePrinter` | `0x3950` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | *Ordinal Only* | `0x3EC0` | 960 | UnwindData |  |
| 279 | *Ordinal Only* | `0x6040` | 114 | UnwindData |  |
| 280 | *Ordinal Only* | `0xAC40` | 801 | UnwindData |  |
| 284 | *Ordinal Only* | `0xB2C0` | 506 | UnwindData |  |
| 283 | *Ordinal Only* | `0xCA10` | 1,486 | UnwindData |  |
| 255 | `DrvPopulateFilterServices` | `0xF330` | 400 | UnwindData |  |
| 256 | `DrvResetConfigCache` | `0x18180` | 57 | UnwindData |  |
| 274 | *Ordinal Only* | `0x1B9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | *Ordinal Only* | `0x1B9E0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | *Ordinal Only* | `0x1C2B0` | 651 | UnwindData |  |
| 270 | *Ordinal Only* | `0x1C5E0` | 858 | UnwindData |  |
| 277 | *Ordinal Only* | `0x20EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | *Ordinal Only* | `0x20EF0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | *Ordinal Only* | `0x21090` | 59 | UnwindData |  |
| 282 | *Ordinal Only* | `0x22EA0` | 196 | UnwindData |  |
| 281 | *Ordinal Only* | `0x23290` | 784 | UnwindData |  |
| 257 | `MxdcGetPDEVAdjustment` | `0x24210` | 1,585 | UnwindData |  |
| 273 | *Ordinal Only* | `0x26890` | 1,007 | UnwindData |  |
