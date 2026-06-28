# Binary Specification: hpbxpsv431.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\hpygid31_v4.inf_amd64_3da19defbde70baa\amd64\hpbxpsv431.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a6d94593279ebec857a0d3408539720d0e9ba764380ee5a57a1aec0e550ba511`
* **Total Exported Functions:** 40

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 35 | `DllCanUnloadNow` | `0x3ACF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `DllGetClassObject` | `0x3AD00` | 586 | UnwindData |  |
| 47 | `PpfTestProcess` | `0x3B040` | 1,958 | UnwindData |  |
| 26 | `ImxCmmDeinit` | `0x3BED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ImxCpuCapsGet` | `0x3BEE0` | 516,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ImxHalftoneDestroy` | `0xBA1B0` | 211,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ImxAlloc` | `0xEDA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ImxCacheFlush` | `0xEDAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ImxCmmInit` | `0xEDAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ImxCmmProfileDestroy` | `0xEDAC0` | 13 | UnwindData |  |
| 42 | `ImxCmmProfileLoad` | `0xEDB20` | 71 | UnwindData |  |
| 41 | `ImxCmmProfileQuery` | `0xEDC50` | 780 | UnwindData |  |
| 28 | `ImxCmmWorldApplyColor` | `0xEDF60` | 276 | UnwindData |  |
| 39 | `ImxCmmWorldApplyColorEx` | `0xEE080` | 398 | UnwindData |  |
| 27 | `ImxCmmWorldApplyImage` | `0xEE210` | 1,013 | UnwindData |  |
| 40 | `ImxCmmWorldApplyImageEx` | `0xEE610` | 1,013 | UnwindData |  |
| 29 | `ImxCmmWorldCreate` | `0xEEA10` | 572 | UnwindData |  |
| 38 | `ImxCmmWorldCreateEx` | `0xEEC50` | 660 | UnwindData |  |
| 30 | `ImxCmmWorldDestroy` | `0xEEEF0` | 82 | UnwindData |  |
| 31 | `ImxCmmWorldLoad` | `0xEEF50` | 444 | UnwindData |  |
| 9 | `ImxFree` | `0xEF110` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ImxHalftoneCreate` | `0xEF330` | 143 | UnwindData |  |
| 17 | `ImxHalftoneLoad` | `0xEF3C0` | 820 | UnwindData |  |
| 19 | `ImxHalftoneTextureColor` | `0xEF700` | 164 | UnwindData |  |
| 18 | `ImxHalftoneTextureImage` | `0xEF7B0` | 558 | UnwindData |  |
| 10 | `ImxJobDataWrite` | `0xEF9E0` | 96 | UnwindData |  |
| 13 | `ImxTextureAlloc` | `0xEFA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `ImxTextureFree` | `0xEFA60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ImxErrDiffConfigure` | `0xEFBA0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ImxErrDiffCreate` | `0xEFC30` | 63 | UnwindData |  |
| 33 | `ImxErrDiffDestroy` | `0xEFD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `ImxErrDiffImage` | `0xEFD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ImxErrDiffLoadConfig` | `0xEFD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ImxJBIGEncoderDeinit` | `0xEFD90` | 89 | UnwindData |  |
| 21 | `ImxJBIGEncoderInit` | `0xEFDF0` | 332 | UnwindData |  |
| 22 | `ImxJBIGImageBandAdd` | `0xEFF40` | 19 | UnwindData |  |
| 23 | `ImxJBIGImageBegin` | `0xEFF60` | 46 | UnwindData |  |
| 24 | `ImxJBIGImageEnd` | `0xEFF90` | 16 | UnwindData |  |
| 44 | `ImxJBIGImageFlush` | `0xEFFA0` | 16 | UnwindData |  |
| 11 | `ImxLogEvent` | `0xEFFB0` | 14 | UnwindData |  |
