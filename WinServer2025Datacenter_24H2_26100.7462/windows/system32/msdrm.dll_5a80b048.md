# Binary Specification: msdrm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msdrm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5a80b048675bc5a834d7170853485281ba241a924cd99b191a6c1ec230f31c34`
* **Total Exported Functions:** 95

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DRMAddRightWithUser` | `0x4870` | 277 | UnwindData |  |
| 9 | `DRMClearAllRights` | `0x4990` | 125 | UnwindData |  |
| 12 | `DRMClosePubHandle` | `0x4A20` | 52 | UnwindData |  |
| 21 | `DRMCreateIssuanceLicense` | `0x4A60` | 1,248 | UnwindData |  |
| 23 | `DRMCreateRight` | `0x4F50` | 557 | UnwindData |  |
| 24 | `DRMCreateUser` | `0x5190` | 568 | UnwindData |  |
| 31 | `DRMDuplicatePubHandle` | `0x53D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `DRMGetApplicationSpecificData` | `0x53E0` | 205 | UnwindData |  |
| 45 | `DRMGetIntervalTime` | `0x54C0` | 177 | UnwindData |  |
| 46 | `DRMGetIssuanceLicenseInfo` | `0x5580` | 778 | UnwindData |  |
| 47 | `DRMGetIssuanceLicenseTemplate` | `0x5890` | 208 | UnwindData |  |
| 48 | `DRMGetMetaData` | `0x5970` | 320 | UnwindData |  |
| 49 | `DRMGetNameAndDescription` | `0x5AC0` | 240 | UnwindData |  |
| 50 | `DRMGetOwnerLicense` | `0x5BC0` | 264 | UnwindData |  |
| 52 | `DRMGetRevocationPoint` | `0x5CD0` | 353 | UnwindData |  |
| 53 | `DRMGetRightExtendedInfo` | `0x5E40` | 445 | UnwindData |  |
| 54 | `DRMGetRightInfo` | `0x6010` | 343 | UnwindData |  |
| 57 | `DRMGetSignedIssuanceLicense` | `0x6170` | 1,746 | UnwindData |  |
| 58 | `DRMGetSignedIssuanceLicenseEx` | `0x6850` | 925 | UnwindData |  |
| 64 | `DRMGetUsagePolicy` | `0x6C00` | 484 | UnwindData |  |
| 65 | `DRMGetUserInfo` | `0x6DF0` | 472 | UnwindData |  |
| 66 | `DRMGetUserRights` | `0x6FD0` | 667 | UnwindData |  |
| 67 | `DRMGetUsers` | `0x7280` | 282 | UnwindData |  |
| 77 | `DRMSetApplicationSpecificData` | `0x73A0` | 336 | UnwindData |  |
| 79 | `DRMSetIntervalTime` | `0x7500` | 132 | UnwindData |  |
| 80 | `DRMSetMetaData` | `0x7590` | 762 | UnwindData |  |
| 81 | `DRMSetNameAndDescription` | `0x7890` | 337 | UnwindData |  |
| 82 | `DRMSetRevocationPoint` | `0x79F0` | 564 | UnwindData |  |
| 83 | `DRMSetUsagePolicy` | `0x7C30` | 735 | UnwindData |  |
| 7 | `DRMAttest` | `0x18B90` | 2,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `DRMVerify` | `0x18B90` | 2,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `DllCanUnloadNow` | `0x194D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `DllGetClassObject` | `0x19500` | 309 | UnwindData |  |
| 93 | `DllRegisterServer` | `0x19640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `DllUnregisterServer` | `0x19650` | 193 | UnwindData |  |
| 10 | `DRMCloseEnvironmentHandle` | `0x19AF0` | 288 | UnwindData |  |
| 73 | `DRMRegisterContent` | `0x19C20` | 302 | UnwindData |  |
| 78 | `DRMSetGlobalOptions` | `0x19D60` | 161 | UnwindData |  |
| 1 | `DRMAcquireAdvisories` | `0x1B0F0` | 1,002 | UnwindData |  |
| 3 | `DRMAcquireLicense` | `0x1B4E0` | 1,775 | UnwindData |  |
| 4 | `DRMActivate` | `0x1BBE0` | 934 | UnwindData |  |
| 5 | `DRMAddLicense` | `0x1BF90` | 460 | UnwindData |  |
| 14 | `DRMCloseSession` | `0x1C170` | 68 | UnwindData |  |
| 17 | `DRMCreateClientSession` | `0x1C1C0` | 499 | UnwindData |  |
| 22 | `DRMCreateLicenseStorageSession` | `0x1C3C0` | 788 | UnwindData |  |
| 25 | `DRMDecode` | `0x1C6E0` | 143 | UnwindData |  |
| 28 | `DRMDeleteLicense` | `0x1C780` | 610 | UnwindData |  |
| 32 | `DRMDuplicateSession` | `0x1C9F0` | 83 | UnwindData |  |
| 33 | `DRMEncode` | `0x1CA50` | 263 | UnwindData |  |
| 35 | `DRMEnumerateLicense` | `0x1CB60` | 1,021 | UnwindData |  |
| 42 | `DRMGetClientVersion` | `0x1CF70` | 177 | UnwindData |  |
| 55 | `DRMGetSecurityProvider` | `0x1D030` | 268 | UnwindData |  |
| 56 | `DRMGetServiceLocation` | `0x1D150` | 326 | UnwindData |  |
| 69 | `DRMIsActivated` | `0x1D2A0` | 326 | UnwindData |  |
| 70 | `DRMIsWindowProtected` | `0x1D3F0` | 152 | UnwindData |  |
| 74 | `DRMRegisterProtectedWindow` | `0x1D490` | 312 | UnwindData |  |
| 76 | `DRMRepair` | `0x1D5D0` | 1,690 | UnwindData |  |
| 2 | `DRMAcquireIssuanceLicenseTemplate` | `0x1F3F0` | 349 | UnwindData |  |
| 13 | `DRMCloseQueryHandle` | `0x1F560` | 68 | UnwindData |  |
| 60 | `DRMGetUnboundLicenseAttribute` | `0x1F5B0` | 288 | UnwindData |  |
| 61 | `DRMGetUnboundLicenseAttributeCount` | `0x1F6E0` | 225 | UnwindData |  |
| 62 | `DRMGetUnboundLicenseObject` | `0x1F7D0` | 350 | UnwindData |  |
| 63 | `DRMGetUnboundLicenseObjectCount` | `0x1F940` | 225 | UnwindData |  |
| 72 | `DRMParseUnboundLicense` | `0x1FA30` | 341 | UnwindData |  |
| 95 | `__AddMachineCertToLicenseStore` | `0x3AB60` | 255 | UnwindData |  |
| 15 | `DRMConstructCertificateChain` | `0x3C3D0` | 161 | UnwindData |  |
| 26 | `DRMDeconstructCertificateChain` | `0x3C480` | 408 | UnwindData |  |
| 41 | `DRMGetCertificateChainCount` | `0x3C620` | 347 | UnwindData |  |
| 8 | `DRMCheckSecurity` | `0x51E20` | 101 | UnwindData |  |
| 11 | `DRMCloseHandle` | `0x51E90` | 197 | UnwindData |  |
| 16 | `DRMCreateBoundLicense` | `0x51F60` | 788 | UnwindData |  |
| 18 | `DRMCreateEnablingBitsDecryptor` | `0x52280` | 524 | UnwindData |  |
| 19 | `DRMCreateEnablingBitsEncryptor` | `0x524A0` | 524 | UnwindData |  |
| 20 | `DRMCreateEnablingPrincipal` | `0x52780` | 421 | UnwindData |  |
| 27 | `DRMDecrypt` | `0x52930` | 196 | UnwindData |  |
| 29 | `DRMDuplicateEnvironmentHandle` | `0x52A00` | 144 | UnwindData |  |
| 30 | `DRMDuplicateHandle` | `0x52AA0` | 144 | UnwindData |  |
| 34 | `DRMEncrypt` | `0x52C30` | 191 | UnwindData |  |
| 37 | `DRMGetBoundLicenseAttribute` | `0x52D00` | 313 | UnwindData |  |
| 38 | `DRMGetBoundLicenseAttributeCount` | `0x52E40` | 138 | UnwindData |  |
| 39 | `DRMGetBoundLicenseObject` | `0x52ED0` | 202 | UnwindData |  |
| 40 | `DRMGetBoundLicenseObjectCount` | `0x52FA0` | 138 | UnwindData |  |
| 43 | `DRMGetEnvironmentInfo` | `0x53030` | 38 | UnwindData |  |
| 44 | `DRMGetInfo` | `0x53060` | 314 | UnwindData |  |
| 51 | `DRMGetProcAddress` | `0x531A0` | 157 | UnwindData |  |
| 59 | `DRMGetTime` | `0x53250` | 223 | UnwindData |  |
| 68 | `DRMInitEnvironment` | `0x53340` | 568 | UnwindData |  |
| 71 | `DRMLoadLibrary` | `0x53580` | 233 | UnwindData |  |
| 75 | `DRMRegisterRevocationList` | `0x53670` | 136 | UnwindData |  |
| 85 | `DRMpCloseFile` | `0x567A0` | 41 | UnwindData |  |
| 86 | `DRMpFileInitialize` | `0x567D0` | 679 | UnwindData |  |
| 87 | `DRMpFileIsProtected` | `0x56A80` | 504 | UnwindData |  |
| 88 | `DRMpFileProtect` | `0x56C80` | 859 | UnwindData |  |
| 89 | `DRMpFileUnprotect` | `0x56FF0` | 520 | UnwindData |  |
| 90 | `DRMpFreeMemory` | `0x57200` | 25 | UnwindData |  |
