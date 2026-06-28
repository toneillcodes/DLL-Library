# Binary Specification: secproc_isv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\secproc_isv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `442981c681b565754dcbf5ce2f96ff7982152184a081a8c9d0794e80876f2615`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SPAttest` | `0xA0C0` | 435 | UnwindData |  |
| 2 | `SPBindLicense` | `0xA280` | 448 | UnwindData |  |
| 3 | `SPCheckEnvironmentSecurity` | `0xA450` | 45 | UnwindData |  |
| 4 | `SPCommit` | `0xA490` | 54 | UnwindData |  |
| 5 | `SPCreateDecryptor` | `0xA4D0` | 428 | UnwindData |  |
| 6 | `SPCreateEnablingPrincipal` | `0xA690` | 517 | UnwindData |  |
| 7 | `SPCreateEncryptor` | `0xA8A0` | 533 | UnwindData |  |
| 8 | `SPCreatePCE` | `0xAAC0` | 54 | UnwindData |  |
| 9 | `SPCreateSecurityProcessor` | `0xAB00` | 447 | UnwindData |  |
| 10 | `SPDecrypt` | `0xACD0` | 397 | UnwindData |  |
| 11 | `SPDecryptFinal` | `0xAE70` | 54 | UnwindData |  |
| 12 | `SPDecryptUpdate` | `0xAEB0` | 54 | UnwindData |  |
| 13 | `SPEnableAndEncrypt` | `0xAEF0` | 1,153 | UnwindData |  |
| 14 | `SPEnablePublishingLicense` | `0xB380` | 109 | UnwindData |  |
| 15 | `SPEncrypt` | `0xB400` | 385 | UnwindData |  |
| 16 | `SPEncryptFinal` | `0xB590` | 54 | UnwindData |  |
| 17 | `SPEncryptUpdate` | `0xB5D0` | 54 | UnwindData |  |
| 18 | `SPGetBoundRightKey` | `0xB610` | 350 | UnwindData |  |
| 19 | `SPGetCurrentTime` | `0xB780` | 344 | UnwindData |  |
| 20 | `SPGetInfo` | `0xB8E0` | 473 | UnwindData |  |
| 21 | `SPGetLicenseAttribute` | `0xBAC0` | 381 | UnwindData |  |
| 22 | `SPGetLicenseAttributeCount` | `0xBC50` | 366 | UnwindData |  |
| 23 | `SPGetLicenseObject` | `0xBDD0` | 441 | UnwindData |  |
| 24 | `SPGetLicenseObjectCount` | `0xBF90` | 366 | UnwindData |  |
| 25 | `SPGetProcAddress` | `0xC110` | 503 | UnwindData |  |
| 26 | `SPIsActivated` | `0xC310` | 234 | UnwindData |  |
| 27 | `SPLoadLibrary` | `0xC400` | 398 | UnwindData |  |
| 28 | `SPRegisterRevocationList` | `0xC5A0` | 344 | UnwindData |  |
| 29 | `SPSign` | `0xC700` | 387 | UnwindData |  |
| 30 | `SPCloseHandle` | `0xCA50` | 134 | UnwindData |  |
