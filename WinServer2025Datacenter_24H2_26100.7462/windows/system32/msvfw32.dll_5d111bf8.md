# Binary Specification: msvfw32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvfw32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5d111bf8883bab610496c731b0b1602287f662ece5aa695eb7a6c5608c2ddac9`
* **Total Exported Functions:** 47

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `VideoForWindowsVersion` | `0x21E0` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ICClose` | `0x2B60` | 158 | UnwindData |  |
| 23 | `ICCompress` | `0x2C10` | 127 | UnwindData |  |
| 26 | `ICDecompress` | `0x2CA0` | 84 | UnwindData |  |
| 27 | `ICDraw` | `0x2F30` | 71 | UnwindData |  |
| 28 | `ICDrawBegin` | `0x2F80` | 137 | UnwindData |  |
| 29 | `ICGetDisplayFormat` | `0x3010` | 964 | UnwindData |  |
| 30 | `ICGetInfo` | `0x33E0` | 185 | UnwindData |  |
| 33 | `ICInfo` | `0x34A0` | 841 | UnwindData |  |
| 34 | `ICInstall` | `0x37F0` | 569 | UnwindData |  |
| 35 | `ICLocate` | `0x3A30` | 478 | UnwindData |  |
| 37 | `ICOpen` | `0x3C20` | 687 | UnwindData |  |
| 38 | `ICOpenFunction` | `0x3EE0` | 290 | UnwindData |  |
| 39 | `ICRemove` | `0x4010` | 252 | UnwindData |  |
| 40 | `ICSendMessage` | `0x4120` | 126 | UnwindData |  |
| 24 | `ICCompressorChoose` | `0x4E20` | 664 | UnwindData |  |
| 25 | `ICCompressorFree` | `0x68B0` | 344 | UnwindData |  |
| 31 | `ICImageCompress` | `0x6A10` | 1,061 | UnwindData |  |
| 32 | `ICImageDecompress` | `0x6E40` | 926 | UnwindData |  |
| 41 | `ICSeqCompressFrame` | `0x71F0` | 321 | UnwindData |  |
| 42 | `ICSeqCompressFrameEnd` | `0x7340` | 240 | UnwindData |  |
| 43 | `ICSeqCompressFrameStart` | `0x7440` | 800 | UnwindData |  |
| 36 | `ICMThunk32` | `0x84D0` | 575 | UnwindData |  |
| 3 | `DrawDibBegin` | `0x94C0` | 5,653 | UnwindData |  |
| 4 | `DrawDibChangePalette` | `0xAAE0` | 905 | UnwindData |  |
| 5 | `DrawDibClose` | `0xAF70` | 241 | UnwindData |  |
| 6 | `DrawDibDraw` | `0xB070` | 3,489 | UnwindData |  |
| 7 | `DrawDibEnd` | `0xBE20` | 42 | UnwindData |  |
| 8 | `DrawDibGetBuffer` | `0xC1C0` | 78 | UnwindData |  |
| 9 | `DrawDibGetPalette` | `0xC220` | 76 | UnwindData |  |
| 10 | `DrawDibOpen` | `0xC4F0` | 115 | UnwindData |  |
| 12 | `DrawDibRealize` | `0xC7A0` | 253 | UnwindData |  |
| 13 | `DrawDibSetPalette` | `0xC8B0` | 358 | UnwindData |  |
| 14 | `DrawDibStart` | `0xCA20` | 66 | UnwindData |  |
| 15 | `DrawDibStop` | `0xCA70` | 66 | UnwindData |  |
| 16 | `DrawDibTime` | `0xCAC0` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DrawDibProfileDisplay` | `0xD620` | 41 | UnwindData |  |
| 48 | `StretchDIB` | `0xDDA0` | 1,221 | UnwindData |  |
| 17 | `GetOpenFileNamePreview` | `0x10C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `GetOpenFileNamePreviewA` | `0x10C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `GetOpenFileNamePreviewW` | `0x10C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetSaveFileNamePreviewA` | `0x10C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `GetSaveFileNamePreviewW` | `0x10C70` | 6,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MCIWndCreate` | `0x12700` | 173 | UnwindData |  |
| 45 | `MCIWndCreateA` | `0x12700` | 173 | UnwindData |  |
| 46 | `MCIWndCreateW` | `0x127C0` | 281 | UnwindData |  |
| 47 | `MCIWndRegisterClass` | `0x14AF0` | 264 | UnwindData |  |
