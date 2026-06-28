# Binary Specification: secproc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\secproc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e5ce7a043425fc728e94e10163055009459fd8074f85867ee7b24614988be224`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SPAttest` | `0xA450` | 435 | UnwindData |  |
| 2 | `SPBindLicense` | `0xA610` | 448 | UnwindData |  |
| 3 | `SPCheckEnvironmentSecurity` | `0xA7E0` | 45 | UnwindData |  |
| 4 | `SPCommit` | `0xA820` | 54 | UnwindData |  |
| 5 | `SPCreateDecryptor` | `0xA860` | 428 | UnwindData |  |
| 6 | `SPCreateEnablingPrincipal` | `0xAA20` | 517 | UnwindData |  |
| 7 | `SPCreateEncryptor` | `0xAC30` | 533 | UnwindData |  |
| 8 | `SPCreatePCE` | `0xAE50` | 54 | UnwindData |  |
| 9 | `SPCreateSecurityProcessor` | `0xAE90` | 440 | UnwindData |  |
| 10 | `SPDecrypt` | `0xB050` | 397 | UnwindData |  |
| 11 | `SPDecryptFinal` | `0xB1F0` | 54 | UnwindData |  |
| 12 | `SPDecryptUpdate` | `0xB230` | 54 | UnwindData |  |
| 13 | `SPEnableAndEncrypt` | `0xB270` | 1,153 | UnwindData |  |
| 14 | `SPEnablePublishingLicense` | `0xB700` | 109 | UnwindData |  |
| 15 | `SPEncrypt` | `0xB780` | 385 | UnwindData |  |
| 16 | `SPEncryptFinal` | `0xB910` | 54 | UnwindData |  |
| 17 | `SPEncryptUpdate` | `0xB950` | 54 | UnwindData |  |
| 18 | `SPGetBoundRightKey` | `0xB990` | 350 | UnwindData |  |
| 19 | `SPGetCurrentTime` | `0xBB00` | 344 | UnwindData |  |
| 20 | `SPGetInfo` | `0xBC60` | 473 | UnwindData |  |
| 21 | `SPGetLicenseAttribute` | `0xBE40` | 381 | UnwindData |  |
| 22 | `SPGetLicenseAttributeCount` | `0xBFD0` | 366 | UnwindData |  |
| 23 | `SPGetLicenseObject` | `0xC150` | 441 | UnwindData |  |
| 24 | `SPGetLicenseObjectCount` | `0xC310` | 366 | UnwindData |  |
| 25 | `SPGetProcAddress` | `0xC490` | 503 | UnwindData |  |
| 26 | `SPIsActivated` | `0xC690` | 234 | UnwindData |  |
| 27 | `SPLoadLibrary` | `0xC780` | 398 | UnwindData |  |
| 28 | `SPRegisterRevocationList` | `0xC920` | 344 | UnwindData |  |
| 29 | `SPSign` | `0xCA80` | 387 | UnwindData |  |
| 30 | `SPCloseHandle` | `0xCDD0` | 134 | UnwindData |  |
