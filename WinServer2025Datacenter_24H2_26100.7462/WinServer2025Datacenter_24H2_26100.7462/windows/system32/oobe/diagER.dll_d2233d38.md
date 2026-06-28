# Binary Specification: diagER.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\oobe\diagER.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d2233d38f6873112b19c4faf8aae8911205ec7341798f1cff130f0e60a858b75`
* **Total Exported Functions:** 44

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CDwWinER@@QEAA@AEBV0@@Z` | `0x1DD0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0CWfpER@@QEAA@AEBV0@@Z` | `0x1F60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0CWfpER@@QEAA@PEBGW4_DIAG_REPORT_TYPE@@H@Z` | `0x1FC0` | 190 | UnwindData |  |
| 5 | `??0IDiagER@@QEAA@AEBV0@@Z` | `0x2090` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??1CWfpER@@UEAA@XZ` | `0x20E0` | 502 | UnwindData |  |
| 10 | `??4CDiagERFactory@@QEAAAEAV0@$$QEAV0@@Z` | `0x22E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??4CDiagERFactory@@QEAAAEAV0@AEBV0@@Z` | `0x22E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??4CDwWinER@@QEAAAEAV0@AEBV0@@Z` | `0x22F0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??4CWfpER@@QEAAAEAV0@AEBV0@@Z` | `0x23B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??4IDiagER@@QEAAAEAV0@AEBV0@@Z` | `0x2400` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?AddBucketingParameters@CWfpER@@UEAAKPEAPEBGI@Z` | `0x2540` | 417 | UnwindData |  |
| 22 | `?AddFiles@CWfpER@@UEAAKPEAPEBGI@Z` | `0x26F0` | 576 | UnwindData |  |
| 34 | `?Initialize@CWfpER@@UEAAKXZ` | `0x2970` | 824 | UnwindData |  |
| 37 | `?SetHeader@CWfpER@@UEAAKPEBG@Z` | `0x2CB0` | 350 | UnwindData |  |
| 40 | `?Submit@CWfpER@@UEAAKK@Z` | `0x2E20` | 387 | UnwindData |  |
| 2 | `??0CDwWinER@@QEAA@PEBGH@Z` | `0x3AE0` | 205 | UnwindData |  |
| 7 | `??1CDwWinER@@UEAA@XZ` | `0x3E50` | 58 | UnwindData |  |
| 18 | `?AddBucketingParameters@CDwWinER@@UEAAKPEAPEBGI@Z` | `0x43C0` | 731 | UnwindData |  |
| 21 | `?AddFiles@CDwWinER@@UEAAKPEAPEBGI@Z` | `0x46B0` | 660 | UnwindData |  |
| 33 | `?Initialize@CDwWinER@@UEAAKXZ` | `0x5640` | 1,113 | UnwindData |  |
| 36 | `?SetHeader@CDwWinER@@UEAAKPEBG@Z` | `0x6960` | 343 | UnwindData |  |
| 39 | `?Submit@CDwWinER@@UEAAKK@Z` | `0x6E90` | 314 | UnwindData |  |
| 6 | `??0IDiagER@@QEAA@PEBGH@Z` | `0x76E0` | 268 | UnwindData |  |
| 9 | `??1IDiagER@@UEAA@XZ` | `0x7800` | 646 | UnwindData |  |
| 20 | `?AddBucketingParameters@IDiagER@@UEAAKPEAPEBGI@Z` | `0x7A90` | 452 | UnwindData |  |
| 23 | `?AddFiles@IDiagER@@UEAAKPEAPEBGI@Z` | `0x7C60` | 586 | UnwindData |  |
| 24 | `?CreateInstance@CDiagERFactory@@SAKPEBGW4_DIAG_REPORT_TYPE@@HPEAPEAVIDiagER@@@Z` | `0x8010` | 488 | UnwindData |  |
| 32 | `?GetErrorReporter@CDiagERFactory@@SAPEAVIDiagER@@XZ` | `0x85E0` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `?ReleaseInstance@CDiagERFactory@@SAXXZ` | `0x8CD0` | 46 | UnwindData |  |
| 38 | `?SetHeader@IDiagER@@UEAAKPEBG@Z` | `0x8E30` | 197 | UnwindData |  |
| 25 | `DiagERAddBucketingParameters` | `0x9070` | 361 | UnwindData |  |
| 26 | `DiagERAddFiles` | `0x91E0` | 221 | UnwindData |  |
| 27 | `DiagERInitialize` | `0x92D0` | 267 | UnwindData |  |
| 28 | `DiagERSetHeader` | `0x93F0` | 205 | UnwindData |  |
| 29 | `DiagERSubmit` | `0x94D0` | 155 | UnwindData |  |
| 30 | `DiagERSubmitEx` | `0x9580` | 193 | UnwindData |  |
| 31 | `DiagERTerminate` | `0x9650` | 179 | UnwindData |  |
| 16 | `??_7CWfpER@@6B@` | `0xC198` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??_7CDwWinER@@6B@` | `0xC1C8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??_7IDiagER@@6B@` | `0xC1F8` | 19,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `g_WerApi` | `0x11000` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `g_Shell32` | `0x11018` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `g_Kernel32` | `0x11020` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `?m_diagER@CDiagERFactory@@0PEAVIDiagER@@EA` | `0x118A0` | 0 | Indeterminate |  |
